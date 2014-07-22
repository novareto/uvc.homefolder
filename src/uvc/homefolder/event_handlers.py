# -*- coding: utf-8 -*-

from uvclight.events import IApplicationInitializedEvent
from zope.component.interfaces import ISite
from grokcore.component import subscribe
from .components import Homefolders
from .interfaces import IHomefolders


from zope.interface import Interface
@subscribe(Interface, IApplicationInitializedEvent)
def register_homefolders(site, event):
    homefolders = site['homefolders'] = Homefolders()
    sm = site.getSiteManager()
    sm.registerUtility(homefolders, IHomefolders)
    print "Homefolders registered !!"
