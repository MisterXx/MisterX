#    Copyright (C) 2013 MisterX
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see [http://www.gnu.org/licenses/].


import urllib,urllib2,re
#import sys
import xbmcplugin,xbmcgui

def CATEGORIES():
        addDir("Most Recent", "http://beeg.com", 1, "")
        addDir("College Rules", "http://beeg.com/search?q=College+Rules", 1, "")



def INDEX(url):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (iPad; U; CPU OS OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		IDString=re.compile('var tumbid  =\[(.+?)\];').findall(link)
		NamesString=re.compile('var tumbalt =\[(.+?)\];').findall(link)
		AllIDs=re.split('\,+', IDString[0])
		NamesString[0]=NamesString[0].lstrip('\'')
		NamesString[0]=NamesString[0].rstrip('\'')
		AllNames=re.split('\'\,\'+', NamesString[0])
		#print(len(AllIDs))
		#print(len(AllNames))
		for number, name in zip(AllIDs, AllNames):
			addDownLink(name,number,2,'http://cdn.anythumb.com/236x177/' + number + '.jpg')



def VIDEOLINKS(url,name):
		listitem = xbmcgui.ListItem(name)
		listitem.setInfo('video', {'Title': name, 'Genre': 'Porn'})
		xbmc.Player().play('http://video.mystreamservice.com/480p/'+url+'.mp4', listitem)

def get_params():
        param=[]
        try:
                paramstring=sys.argv[2]
                if len(paramstring)>=2:
                        params=sys.argv[2]
                        cleanedparams=params.replace('?','')
                        if (params[len(params)-1]=='/'):
                                params=params[0:len(params)-2]
                        pairsofparams=cleanedparams.split('&')
                        param={}
                        for i in range(len(pairsofparams)):
                                splitparams={}
                                splitparams=pairsofparams[i].split('=')
                                if (len(splitparams))==2:
                                        param[splitparams[0]]=splitparams[1]
        except:
                pass
                               
        return param




def addDownLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

		
params=get_params()
url=None
name=None
mode=None


# Populate url, name & mode vars, if not, take default "None"
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)


# Mode 0 = Default mode (just list categories)
# Mode 1 = List content of category
# Mode 2 = Open video

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        INDEX(url)
       
elif mode==2:
        print ""+url
        VIDEOLINKS(url,name)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
