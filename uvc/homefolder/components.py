# -*- coding: utf-8 -*-

from .interfaces import IHomefolder, IHomefolders
from dolmen.container.components import BTreeContainer
from zope.securitypolicy.interfaces import IPrincipalRoleManager
from zope.authentication.interfaces import IUnauthenticatedPrincipal
from zope.traversing.browser.interfaces import IAbsoluteURL
from zope.component import getUtility, adapter
from zope.interface import implementer, provider
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.annotation.interfaces import IAttributeAnnotatable


@implementer(IHomefolder, IAttributeAnnotatable)
class Homefolder(BTreeContainer):
    pass


@implementer(IHomefolders)
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


@adapter(IBrowserRequest)
@provider(IAbsoluteURL)
def homefolder_url(request):
    principal = request.principal
    if IUnauthenticatedPrincipal.providedBy(principal):
        return
    homefolders = getUtility(IHomefolders)
    homefolder = homefolders.get(principal.id)
    return homefolder and IAbsoluteURL(homefolder, request) or None
