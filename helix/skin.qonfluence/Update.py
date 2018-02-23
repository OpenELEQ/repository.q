
import xbmc, xbmcgui
import shutil
import urllib2,urllib
import xbmcaddon

addon = xbmcaddon.Addon('skin.qonfluence')

msg1 = addon.getLocalizedString(32921) # OpenELEQ installeren.
msg2 = addon.getLocalizedString(32922) # Downloaden en uitpakken, moment geduld aub.
msg3 = addon.getLocalizedString(32923) # Gedownload
msg4 = addon.getLocalizedString(32924) # Download geannuleerd.
msg5 = addon.getLocalizedString(32925) # Uitpakken, kan even duren.
msg6 = addon.getLocalizedString(32926) # Moment geduld aub.

def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create(msg1,msg2,'')
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))

def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print msg3+str(percent)+'%'
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print msg4 # need to get this part working
        dp.close()

class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("", msg1):
        url = 'http://bit.ly/1BAvIWV'
        path = xbmc.translatePath(os.path.join('special://home/addons/','packages'))
        lib=os.path.join(path, 'update.zip')
        DownloaderClass(url,lib)
        folder = xbmc.translatePath(os.path.join('special://home',''))
        xbmc.executebuiltin("XBMC.Extract(%s,%s)"%(lib,folder))
     
    
   	xbmc.executebuiltin("Notification('msg5','msg6')")
      
mydisplay = MyClass()
del mydisplay

