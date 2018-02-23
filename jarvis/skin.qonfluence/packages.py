import os
import xbmc
import xbmcgui
import xbmcaddon
import shutil

__addon__     = xbmcaddon.Addon('skin.qonfluence')
__addonid__   = __addon__.getAddonInfo('id')
addonPath     = xbmcaddon.Addon('skin.qonfluence').getAddonInfo("path")
image         = os.path.join(addonPath,'notification.png')
dialog        = xbmcgui.Dialog()

def packages():
    path=xbmc.translatePath(os.path.join('special://home/addons/packages',''))
    if dialog.yesno('Delete Packages', 'Are You Sure?'):
        shutil.rmtree(path)
        xbmc.executebuiltin("Notification(Removing Packages,All Done, 5000, %s)" % (image))

packages()