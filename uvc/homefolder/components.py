# -*- coding: utf-8 -*-

from dolmen.container.components import BTreeContainer
from zope.securitypolicy.interfaces import IPrincipalRoleManager
from zope.security.interfaces import IUnauthenticatedPrincipal
from zope.traversing.browser.interfaces import IAbsoluteURL
from zope.component import getUtility
from .interfaces import IHomefolder, IHomefolders


@implementer(IHomefolder)
class HomeFolder(BTreeContainer):
    pass
    

@implementer(IHomefolders)
class Homefolders(BTreeContainer):
    default = HomeFolder
    roles = [u'uvc.User', u'uvc.Editor', u'uvc.MasterUser']
    
    def make_homefolder(self, factory=None)
        klass= factory or self.default
        return klass()

    def write_homefolder(self, uid, homefolder):
        self[uid] = homefolder
    
    def grant_homefolder_access(self, uid, homefolder, roles=None):
        principal_roles = IPrincipalRoleManager(homefolder)
        for role in roles:
            principal_roles.assignRoleToPrincipal(role, principalId)

    def assign_homefolder(self, uid):
        homefolder = make_homefolder()
        write_homefolder(uid, homefolder)
        grant_homefolder_access(uid, homefolder, roles=self.roles)

    def get_homefolder(self, uid):
        return self.get(uid)
        

@adapter(IBrowserRequest)
@provider(IAbsoluteURL)
def homefolder_url(request):
    principal = self.request.principal
    if IUnauthenticatedPrincipal.providedBy(principal):
        return
    homefolders = getUtility(IHomeFolders)
    homefolder = homefolders.get(principal.id)
    return homefolder and IAbsoluteURL(homefolder, request) or None