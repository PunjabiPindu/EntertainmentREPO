# Beats1 XBMC Plugin
# We do not own or publish the content delivered by the plugin
# streams and content is owned by apple beats1

import sys
import xbmcgui
import xbmcplugin
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://itsliveradio.apple.com/streams/hub01/session01/256k/prog.m3u8'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]Beats 1 Radio[/B][/COLOR]  [COLOR red](Audio Stream 256k)[/COLOR]  [COLOR lime](((LIVE)))[/COLOR] >>', iconImage='http://i-cdn.phonearena.com/images/article/70211-image/Apple-Music-streaming-service-is-official-adds-Beats-1-curated-radio-station.jpg', thumbnailImage= 'http://i-cdn.phonearena.com/images/article/70211-image/Apple-Music-streaming-service-is-official-adds-Beats-1-curated-radio-station.jpg')
li.setProperty('fanart_image', 'http://i2.wp.com/stagedoor.fm/wp-content/uploads/2015/06/Apple-Beats-1-logo.jpg?resize=981%2C552')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://itsliveradio.apple.com/streams/hub01/session01/128k/prog.m3u8'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]Beats 1 Radio[/B][/COLOR]  [COLOR red](Audio Stream 128k)[/COLOR]  [COLOR lime](((LIVE)))[/COLOR] >>', iconImage='http://i-cdn.phonearena.com/images/article/70211-image/Apple-Music-streaming-service-is-official-adds-Beats-1-curated-radio-station.jpg', thumbnailImage= 'http://i-cdn.phonearena.com/images/article/70211-image/Apple-Music-streaming-service-is-official-adds-Beats-1-curated-radio-station.jpg')
li.setProperty('fanart_image', 'http://i2.wp.com/stagedoor.fm/wp-content/uploads/2015/06/Apple-Beats-1-logo.jpg?resize=981%2C552')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://itsliveradio.apple.com/streams/hub01/session01/58k/prog.m3u8'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]Request a Song[/B][/COLOR] : [COLOR blue] To leave a request to hear your favorite song on Beats 1, call us on one of these numbers: [/COLOR]', iconImage='http://s21.postimg.org/qlde6m78n/image.png', thumbnailImage= 'http://s21.postimg.org/qlde6m78n/image.png')
li.setProperty('fanart_image', 'http://s7.postimg.org/ikjfpei0b/download.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)

