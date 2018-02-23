import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys
AddonID="skin.qonfluence"
AddonName="[COLOR FF8ABEE2]Q[/COLOR]onfluence"
dialog=xbmcgui.Dialog()
dialog.ok(AddonName+" Add-on Requires Update","This add-on may still be in the process of the updating so we recommend waiting a few minutes to see if it updates naturally. If it hasn't updated after 5mins please try reinstalling via the Community Portal add-on")
xbmcplugin.endOfDirectory(int(sys.argv[1]))