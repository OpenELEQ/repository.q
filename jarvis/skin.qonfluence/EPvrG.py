
import xbmc, xbmcgui
import shutil
import urllib2,urllib
import xbmcaddon

addon     = xbmcaddon.Addon('skin.qonfluence')
addonPath = xbmcaddon.Addon('skin.qonfluence').getAddonInfo("path")
image     = os.path.join(addonPath,'notification.png')
language  = addon.getLocalizedString

localtxt1 = language(31221) # EPG en PVR-lists
localtxt2 = language(32922) # Downloaden en uitpakken, moment geduld aub.
localtxt3 = language(32923) # Gedownload
localtxt4 = language(32924) # Download geannuleerd.
localtxt5 = language(32925) # Uitpakken, kan even duren.
localtxt6 = language(32926) # Moment geduld aub.
localtxt7 = language(32041) # Download?
localtxt8 = language(32927) # Install Done
localtxt9 = language(32928) # Enjoy

def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create(localtxt1,localtxt2,'')
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))

def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print localtxt3+str(percent)+'%'
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print localtxt4 # need to get this part working
        dp.close()

class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno(localtxt1, localtxt7):
        url = 'http://bit.ly/1MIoh3h'
        path = xbmc.translatePath(os.path.join('special://home/addons/','packages'))
        lib=os.path.join(path, 'EPvrG.zip')
        DownloaderClass(url,lib)
        folder = xbmc.translatePath(os.path.join('special://profile/addon_data/pvr.iptvsimple',''))
        xbmc.executebuiltin("XBMC.Extract(%s,%s)"%(lib,folder))
        xbmc.executebuiltin("Notification("+localtxt8+","+localtxt9+", 5000, %s)" % (image))
mydisplay = MyClass()
del mydisplay

