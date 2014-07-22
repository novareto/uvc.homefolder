# -*- coding: utf-8 -*-

from .interfaces import IHomefolder, IHomefolders
from cromlech.browser import IRequest, IURL
from cromlech.container.interfaces import IContainer
from cromlech.security.interfaces import IUnauthenticatedPrincipal
from dolmen.container.components import BTreeContainer
from zope.component import getUtility, adapter
from zope.interface import implementer, provider
from zope.securitypolicy.interfaces import IPrincipalRoleManager


@implementer(IContainer, IHomefolder)
class Homefolder(BTreeContainer):
    pass


@implementer(IContainer, IHomefolders)
class Homefolders(BTreeContainer):
    default = Homefolder
    roles = [u'uvc.User', u'uvc.Editor', u'uvc.MasterUser']

    def make_homefolder(self, factory=None):
        klass = factory or self.default
        return klass()

    def write_homefolder(self, uid, homefolder):
        self[uid] = homefolder

    def grant_homefolder_access(self, uid, homefolder, roles=[]):
        principal_roles = IPrincipalRoleManager(homefolder)
        for role in roles:
            principal_roles.assignRoleToPrincipal(role, uid)

    def assign_homefolder(self, uid):
        homefolder = self.make_homefolder()
        self.write_homefolder(uid, homefolder)
        self.grant_homefolder_access(uid, homefolder, roles=self.roles)

    def get_homefolder(self, uid):
        return self.get(uid)
