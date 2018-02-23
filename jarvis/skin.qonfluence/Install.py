
import xbmc, xbmcgui
import shutil
import urllib2,urllib
import xbmcaddon
import time

__addon__ = xbmcaddon.Addon('skin.qonfluence')
__addonid__ = __addon__.getAddonInfo('id')

def language(id):
	san = __addon__.getLocalizedString(id).encode( 'utf-8', 'ignore' )
	return san
	
msg1 = __addon__.getLocalizedString(32921)  # OpenELEQ installeren.
msg2 = __addon__.getLocalizedString(32922)  # Downloaden en uitpakken, moment geduld aub.
msg3 = __addon__.getLocalizedString(32923)  # Gedownload
msg4 = __addon__.getLocalizedString(32924)  # Download geannuleerd.
msg5 = __addon__.getLocalizedString(32925)  # Uitpakken, kan even duren.
msg6 = __addon__.getLocalizedString(32926)  # Moment geduld aub.
msg7 = __addon__.getLocalizedString(32927)  # Installatie klaar,
msg8 = __addon__.getLocalizedString(32928)  # veel plezier!
msg9 = __addon__.getLocalizedString(32929)  # Enorm bedankt dat u
msg10 = __addon__.getLocalizedString(32930) # voor OpenELEQ heeft gekozen.
msg11 = __addon__.getLocalizedString(32931) # Suggesties en/of donaties
msg12 = __addon__.getLocalizedString(32932) # zijn altijd welkom.
msg13 = __addon__.getLocalizedString(32933) # Mijn paypal is
msg14 = __addon__.getLocalizedString(32934) # dan_q_wel@hotmail.com
msg15 = __addon__.getLocalizedString(32935) # OpenELEQ installeren?
	
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create(language(32921),language(32922),'')
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))

def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print language(32923)+str(percent)+'%'
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print language(32924) # need to get this part working
        dp.close()

class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno(language(32921),language(32935)):
        url = 'http://bit.ly/1tN9aMX'
        path = xbmc.translatePath(os.path.join('special://home/addons/packages',''))
        lib=os.path.join(path, 'OpenELEQ.zip')
        DownloaderClass(url,lib)
        folder = xbmc.translatePath(os.path.join('special://home',''))
	xbmc.executebuiltin('Notification(%s,%s,%i,special://profile/addon_data/pvr.iptvsimple/icoontjes/OpenELEQ.png)' % (language(32925),language(32926),10000))
        xbmc.executebuiltin("XBMC.Extract(%s,%s)"%(lib,folder))
    
	xbmc.executebuiltin('Notification(%s,%s,%i,special://profile/addon_data/pvr.iptvsimple/icoontjes/OpenELEQ.png)' % (language(32927),language(32928),10000))
        time.sleep(10)
	xbmc.executebuiltin('Notification(%s,%s,%i,special://profile/addon_data/pvr.iptvsimple/icoontjes/OpenELEQ.png)' % (language(32929),language(32930),10000))
        time.sleep(10)	
	xbmc.executebuiltin('Notification(%s,%s,%i,special://profile/addon_data/pvr.iptvsimple/icoontjes/OpenELEQ.png)' % (language(32931),language(32932),10000))
        time.sleep(10)	
	xbmc.executebuiltin('Notification(%s,%s,%i,special://profile/addon_data/pvr.iptvsimple/icoontjes/OpenELEQ.png)' % (language(32933),language(32934),10000))
        time.sleep(10)	
		
mydisplay = MyClass()
del mydisplay
