from five import grok
from zope.interface import Interface
from zope.component import getMultiAdapter
from plone.app.layout.viewlets.interfaces import IPortalFooter


class InfoBarViewlet(grok.Viewlet):
    grok.name('faust.blog.InfoBarViewlet')
    grok.context(Interface)
    grok.require('zope2.View')
    grok.viewletmanager(IPortalFooter)

    def update(self):
        pstate = getMultiAdapter((self.context, self.request),
                                 name="plone_portal_state")
        self.portal_url = pstate.portal_url()
