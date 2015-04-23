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


import urllib,urllib2,re, os
import xbmcplugin,xbmcgui,xbmcaddon
addon=xbmcaddon.Addon()
def getSet(id,d=''): 
    try: return addon.getSetting(id)
    except: return d

NAME = 'beeg.com plugin'



class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False



def CATEGORIES():
        addDir('Most Recent', 'http://beeg.com/section/home/1/', 'getIndex', '', '1')
        addDir('Categories', 'http://beeg.com/section/home/1/', 'getSiteCategories', '', '1')
        addDir('Long Videos', 'http://beeg.com/section/long-videos/1/', 'getIndex', '', '1')
        addDir('Search', 'http://beeg.com/search?q=', 'getSearch', '', '1')
        
        
        
        

def SITE_CATEGORIES():
		addDir('18', 'http://beeg.com/tag/18/1/', 'getIndex', '', '1')
		addDir('20', 'http://beeg.com/tag/20/1/', 'getIndex', '', '1')
		addDir('30', 'http://beeg.com/tag/30/1/', 'getIndex', '', '1')
		addDir('40', 'http://beeg.com/tag/40/1/', 'getIndex', '', '1')
		addDir('50', 'http://beeg.com/tag/50/1/', 'getIndex', '', '1')
		addDir('69', 'http://beeg.com/tag/69/1/', 'getIndex', '', '1')
		addDir('Abuse', 'http://beeg.com/tag/abuse/1/', 'getIndex', '', '1')
		addDir('Aggressive', 'http://beeg.com/tag/aggressive/1/', 'getIndex', '', '1')
		addDir('American', 'http://beeg.com/tag/american/1/', 'getIndex', '', '1')
		addDir('Anal dildo', 'http://beeg.com/tag/anal+dildo/1/', 'getIndex', '', '1')
		addDir('Anal fingering', 'http://beeg.com/tag/anal+fingering/1/', 'getIndex', '', '1')
		addDir('Anal fisting', 'http://beeg.com/tag/anal+fisting/1/', 'getIndex', '', '1')
		addDir('Analingus', 'http://beeg.com/tag/analingus/1/', 'getIndex', '', '1')
		addDir('Arab', 'http://beeg.com/tag/arab/1/', 'getIndex', '', '1')
		addDir('Army', 'http://beeg.com/tag/army/1/', 'getIndex', '', '1')
		addDir('Asian', 'http://beeg.com/tag/asian/1/', 'getIndex', '', '1')
		addDir('Ass lick', 'http://beeg.com/tag/ass+lick/1/', 'getIndex', '', '1')
		addDir('Babe', 'http://beeg.com/tag/babe/1/', 'getIndex', '', '1')
		addDir('Bath', 'http://beeg.com/tag/bath/1/', 'getIndex', '', '1')
		addDir('Bathroom', 'http://beeg.com/tag/bathroom/1/', 'getIndex', '', '1')
		addDir('Bdsm', 'http://beeg.com/tag/bdsm/1/', 'getIndex', '', '1')
		addDir('Beach', 'http://beeg.com/tag/beach/1/', 'getIndex', '', '1')
		addDir('Beautiful', 'http://beeg.com/tag/beautiful/1/', 'getIndex', '', '1')
		addDir('Beautiful ass', 'http://beeg.com/tag/beautiful+ass/1/', 'getIndex', '', '1')
		addDir('Beautiful body', 'http://beeg.com/tag/beautiful+body/1/', 'getIndex', '', '1')
		addDir('Beautiful face', 'http://beeg.com/tag/beautiful+face/1/', 'getIndex', '', '1')
		addDir('Beautiful legs', 'http://beeg.com/tag/beautiful+legs/1/', 'getIndex', '', '1')
		addDir('Bed', 'http://beeg.com/tag/bed/1/', 'getIndex', '', '1')
		addDir('Bedroom', 'http://beeg.com/tag/bedroom/1/', 'getIndex', '', '1')
		addDir('Bend over', 'http://beeg.com/tag/bend+over/1/', 'getIndex', '', '1')
		addDir('Big ass', 'http://beeg.com/tag/big+ass/1/', 'getIndex', '', '1')
		addDir('Bikini', 'http://beeg.com/tag/bikini/1/', 'getIndex', '', '1')
		addDir('Bisexual', 'http://beeg.com/tag/bisexual/1/', 'getIndex', '', '1')
		addDir('Black', 'http://beeg.com/tag/black/1/', 'getIndex', '', '1')
		addDir('Black cock', 'http://beeg.com/tag/black+cock/1/', 'getIndex', '', '1')
		addDir('Blonde', 'http://beeg.com/tag/blonde/1/', 'getIndex', '', '1')
		addDir('Blue eyes', 'http://beeg.com/tag/blue+eyes/1/', 'getIndex', '', '1')
		addDir('Bondage', 'http://beeg.com/tag/bondage/1/', 'getIndex', '', '1')
		addDir('Boots', 'http://beeg.com/tag/boots/1/', 'getIndex', '', '1')
		addDir('Brazilian', 'http://beeg.com/tag/brazilian/1/', 'getIndex', '', '1')
		addDir('Bride', 'http://beeg.com/tag/bride/1/', 'getIndex', '', '1')
		addDir('British', 'http://beeg.com/tag/british/1/', 'getIndex', '', '1')
		addDir('Brunette', 'http://beeg.com/tag/brunette/1/', 'getIndex', '', '1')
		addDir('Brutal', 'http://beeg.com/tag/brutal/1/', 'getIndex', '', '1')
		addDir('Brutal dildo', 'http://beeg.com/tag/brutal+dildo/1/', 'getIndex', '', '1')
		addDir('Bukkake', 'http://beeg.com/tag/bukkake/1/', 'getIndex', '', '1')
		addDir('Busty teen', 'http://beeg.com/tag/busty+teen/1/', 'getIndex', '', '1')
		addDir('Campus', 'http://beeg.com/tag/campus/1/', 'getIndex', '', '1')
		addDir('Car', 'http://beeg.com/tag/car/1/', 'getIndex', '', '1')
		addDir('Cash', 'http://beeg.com/tag/cash/1/', 'getIndex', '', '1')
		addDir('Casting', 'http://beeg.com/tag/casting/1/', 'getIndex', '', '1')
		addDir('Cfnm', 'http://beeg.com/tag/cfnm/1/', 'getIndex', '', '1')
		addDir('Chair', 'http://beeg.com/tag/chair/1/', 'getIndex', '', '1')
		addDir('Cheat', 'http://beeg.com/tag/cheat/1/', 'getIndex', '', '1')
		addDir('Cheerleader', 'http://beeg.com/tag/cheerleader/1/', 'getIndex', '', '1')
		addDir('Class', 'http://beeg.com/tag/class/1/', 'getIndex', '', '1')
		addDir('Classic', 'http://beeg.com/tag/classic/1/', 'getIndex', '', '1')
		addDir('Classroom', 'http://beeg.com/tag/classroom/1/', 'getIndex', '', '1')
		addDir('Closeup', 'http://beeg.com/tag/closeup/1/', 'getIndex', '', '1')
		addDir('Clothes off', 'http://beeg.com/tag/clothes+off/1/', 'getIndex', '', '1')
		addDir('Club', 'http://beeg.com/tag/club/1/', 'getIndex', '', '1')
		addDir('Cock ride', 'http://beeg.com/tag/cock+ride/1/', 'getIndex', '', '1')
		addDir('Coed', 'http://beeg.com/tag/coed/1/', 'getIndex', '', '1')
		addDir('College girl', 'http://beeg.com/tag/college+girl/1/', 'getIndex', '', '1')
		addDir('Compassionate', 'http://beeg.com/tag/compassionate/1/', 'getIndex', '', '1')
		addDir('Couple', 'http://beeg.com/tag/couple/1/', 'getIndex', '', '1')
		addDir('Creampie', 'http://beeg.com/tag/creampie/1/', 'getIndex', '', '1')
		addDir('Crying', 'http://beeg.com/tag/crying/1/', 'getIndex', '', '1')
		addDir('Curly', 'http://beeg.com/tag/curly/1/', 'getIndex', '', '1')
		addDir('Cute', 'http://beeg.com/tag/cute/1/', 'getIndex', '', '1')
		addDir('Czech', 'http://beeg.com/tag/czech/1/', 'getIndex', '', '1')
		addDir('Dancing', 'http://beeg.com/tag/dancing/1/', 'getIndex', '', '1')
		addDir('Dark', 'http://beeg.com/tag/dark/1/', 'getIndex', '', '1')
		addDir('Decorations', 'http://beeg.com/tag/decorations/1/', 'getIndex', '', '1')
		addDir('Deep throat', 'http://beeg.com/tag/deep+throat/1/', 'getIndex', '', '1')
		addDir('Desk', 'http://beeg.com/tag/desk/1/', 'getIndex', '', '1')
		addDir('Dildo', 'http://beeg.com/tag/dildo/1/', 'getIndex', '', '1')
		addDir('Dirty talk', 'http://beeg.com/tag/dirty+talk/1/', 'getIndex', '', '1')
		addDir('Doctor', 'http://beeg.com/tag/doctor/1/', 'getIndex', '', '1')
		addDir('Doggy', 'http://beeg.com/tag/doggy/1/', 'getIndex', '', '1')
		addDir('Domination', 'http://beeg.com/tag/domination/1/', 'getIndex', '', '1')
		addDir('Dorm', 'http://beeg.com/tag/dorm/1/', 'getIndex', '', '1')
		addDir('Double', 'http://beeg.com/tag/double/1/', 'getIndex', '', '1')
		addDir('Dress', 'http://beeg.com/tag/dress/1/', 'getIndex', '', '1')
		addDir('Drunk', 'http://beeg.com/tag/drunk/1/', 'getIndex', '', '1')
		addDir('Ebony', 'http://beeg.com/tag/ebony/1/', 'getIndex', '', '1')
		addDir('Emotional', 'http://beeg.com/tag/emotional/1/', 'getIndex', '', '1')
		addDir('Erotic', 'http://beeg.com/tag/erotic/1/', 'getIndex', '', '1')
		addDir('Extreme', 'http://beeg.com/tag/extreme/1/', 'getIndex', '', '1')
		addDir('Eyes', 'http://beeg.com/tag/eyes/1/', 'getIndex', '', '1')
		addDir('Face', 'http://beeg.com/tag/face/1/', 'getIndex', '', '1')
		addDir('Facesitting', 'http://beeg.com/tag/facesitting/1/', 'getIndex', '', '1')
		addDir('Family', 'http://beeg.com/tag/family/1/', 'getIndex', '', '1')
		addDir('Fashionable', 'http://beeg.com/tag/fashionable/1/', 'getIndex', '', '1')
		addDir('Fat cock', 'http://beeg.com/tag/fat+cock/1/', 'getIndex', '', '1')
		addDir('Feet', 'http://beeg.com/tag/feet/1/', 'getIndex', '', '1')
		addDir('Female teacher', 'http://beeg.com/tag/female+teacher/1/', 'getIndex', '', '1')
		addDir('Femdom', 'http://beeg.com/tag/femdom/1/', 'getIndex', '', '1')
		addDir('Fetish', 'http://beeg.com/tag/fetish/1/', 'getIndex', '', '1')
		addDir('Fffm', 'http://beeg.com/tag/fffm/1/', 'getIndex', '', '1')
		addDir('Ffm', 'http://beeg.com/tag/ffm/1/', 'getIndex', '', '1')
		addDir('Ffmm', 'http://beeg.com/tag/ffmm/1/', 'getIndex', '', '1')
		addDir('Finger fuck', 'http://beeg.com/tag/finger+fuck/1/', 'getIndex', '', '1')
		addDir('Fingering', 'http://beeg.com/tag/fingering/1/', 'getIndex', '', '1')
		addDir('Fisting', 'http://beeg.com/tag/fisting/1/', 'getIndex', '', '1')
		addDir('Flexible', 'http://beeg.com/tag/flexible/1/', 'getIndex', '', '1')
		addDir('Flirty', 'http://beeg.com/tag/flirty/1/', 'getIndex', '', '1')
		addDir('Floor', 'http://beeg.com/tag/floor/1/', 'getIndex', '', '1')
		addDir('Fmm', 'http://beeg.com/tag/fmm/1/', 'getIndex', '', '1')
		addDir('Fmmm', 'http://beeg.com/tag/fmmm/1/', 'getIndex', '', '1')
		addDir('Food', 'http://beeg.com/tag/food/1/', 'getIndex', '', '1')
		addDir('Foot', 'http://beeg.com/tag/foot/1/', 'getIndex', '', '1')
		addDir('Footjob', 'http://beeg.com/tag/footjob/1/', 'getIndex', '', '1')
		addDir('Foursome', 'http://beeg.com/tag/foursome/1/', 'getIndex', '', '1')
		addDir('French', 'http://beeg.com/tag/french/1/', 'getIndex', '', '1')
		addDir('Fresh', 'http://beeg.com/tag/fresh/1/', 'getIndex', '', '1')
		addDir('From behind', 'http://beeg.com/tag/from+behind/1/', 'getIndex', '', '1')
		addDir('Fucking', 'http://beeg.com/tag/fucking/1/', 'getIndex', '', '1')
		addDir('German', 'http://beeg.com/tag/german/1/', 'getIndex', '', '1')
		addDir('Glamour', 'http://beeg.com/tag/glamour/1/', 'getIndex', '', '1')
		addDir('Glasses', 'http://beeg.com/tag/glasses/1/', 'getIndex', '', '1')
		addDir('Glory hole', 'http://beeg.com/tag/glory+hole/1/', 'getIndex', '', '1')
		addDir('Good cock', 'http://beeg.com/tag/good+cock/1/', 'getIndex', '', '1')
		addDir('Gorgeous', 'http://beeg.com/tag/gorgeous/1/', 'getIndex', '', '1')
		addDir('Granny', 'http://beeg.com/tag/granny/1/', 'getIndex', '', '1')
		addDir('Green eyes', 'http://beeg.com/tag/green+eyes/1/', 'getIndex', '', '1')
		addDir('Grey eyes', 'http://beeg.com/tag/grey+eyes/1/', 'getIndex', '', '1')
		addDir('Hairstyle', 'http://beeg.com/tag/hairstyle/1/', 'getIndex', '', '1')
		addDir('Hairy', 'http://beeg.com/tag/hairy/1/', 'getIndex', '', '1')
		addDir('Handcuffs', 'http://beeg.com/tag/handcuffs/1/', 'getIndex', '', '1')
		addDir('Handjob', 'http://beeg.com/tag/handjob/1/', 'getIndex', '', '1')
		addDir('Hardcore', 'http://beeg.com/tag/hardcore/1/', 'getIndex', '', '1')
		addDir('Heels', 'http://beeg.com/tag/heels/1/', 'getIndex', '', '1')
		addDir('Hidden cam', 'http://beeg.com/tag/hidden+cam/1/', 'getIndex', '', '1')
		addDir('Home video', 'http://beeg.com/tag/home+video/1/', 'getIndex', '', '1')
		addDir('Homemade', 'http://beeg.com/tag/homemade/1/', 'getIndex', '', '1')
		addDir('Horny', 'http://beeg.com/tag/horny/1/', 'getIndex', '', '1')
		addDir('Hospital', 'http://beeg.com/tag/hospital/1/', 'getIndex', '', '1')
		addDir('Hotel', 'http://beeg.com/tag/hotel/1/', 'getIndex', '', '1')
		addDir('Housewife', 'http://beeg.com/tag/housewife/1/', 'getIndex', '', '1')
		addDir('Humiliation', 'http://beeg.com/tag/humiliation/1/', 'getIndex', '', '1')
		addDir('Hungarian', 'http://beeg.com/tag/hungarian/1/', 'getIndex', '', '1')
		addDir('In nature', 'http://beeg.com/tag/in+nature/1/', 'getIndex', '', '1')
		addDir('Indian', 'http://beeg.com/tag/indian/1/', 'getIndex', '', '1')
		addDir('Innocent', 'http://beeg.com/tag/innocent/1/', 'getIndex', '', '1')
		addDir('Interracial', 'http://beeg.com/tag/interracial/1/', 'getIndex', '', '1')
		addDir('Interview', 'http://beeg.com/tag/interview/1/', 'getIndex', '', '1')
		addDir('Italian', 'http://beeg.com/tag/italian/1/', 'getIndex', '', '1')
		addDir('Japanese', 'http://beeg.com/tag/japanese/1/', 'getIndex', '', '1')
		addDir('Jeans', 'http://beeg.com/tag/jeans/1/', 'getIndex', '', '1')
		addDir('Kiss', 'http://beeg.com/tag/kiss/1/', 'getIndex', '', '1')
		addDir('Kitchen', 'http://beeg.com/tag/kitchen/1/', 'getIndex', '', '1')
		addDir('Lady', 'http://beeg.com/tag/lady/1/', 'getIndex', '', '1')
		addDir('Latex', 'http://beeg.com/tag/latex/1/', 'getIndex', '', '1')
		addDir('Latin', 'http://beeg.com/tag/latin/1/', 'getIndex', '', '1')
		addDir('Legs', 'http://beeg.com/tag/legs/1/', 'getIndex', '', '1')
		addDir('Lesbian teen', 'http://beeg.com/tag/lesbian+teen/1/', 'getIndex', '', '1')
		addDir('Lick', 'http://beeg.com/tag/lick/1/', 'getIndex', '', '1')
		addDir('Location', 'http://beeg.com/tag/location/1/', 'getIndex', '', '1')
		addDir('Long hair', 'http://beeg.com/tag/long+hair/1/', 'getIndex', '', '1')
		addDir('Long legs', 'http://beeg.com/tag/long+legs/1/', 'getIndex', '', '1')
		addDir('Maid', 'http://beeg.com/tag/maid/1/', 'getIndex', '', '1')
		addDir('Male strip', 'http://beeg.com/tag/male+strip/1/', 'getIndex', '', '1')
		addDir('Male teacher', 'http://beeg.com/tag/male+teacher/1/', 'getIndex', '', '1')
		addDir('Massage', 'http://beeg.com/tag/massage/1/', 'getIndex', '', '1')
		addDir('Mature', 'http://beeg.com/tag/mature/1/', 'getIndex', '', '1')
		addDir('Medical', 'http://beeg.com/tag/medical/1/', 'getIndex', '', '1')
		addDir('Mexican', 'http://beeg.com/tag/mexican/1/', 'getIndex', '', '1')
		addDir('Mini', 'http://beeg.com/tag/mini/1/', 'getIndex', '', '1')
		addDir('Missionary', 'http://beeg.com/tag/missionary/1/', 'getIndex', '', '1')
		addDir('Mistress', 'http://beeg.com/tag/mistress/1/', 'getIndex', '', '1')
		addDir('Moan', 'http://beeg.com/tag/moan/1/', 'getIndex', '', '1')
		addDir('Mom', 'http://beeg.com/tag/mom/1/', 'getIndex', '', '1')
		addDir('Money', 'http://beeg.com/tag/money/1/', 'getIndex', '', '1')
		addDir('Mother', 'http://beeg.com/tag/mother/1/', 'getIndex', '', '1')
		addDir('Natural', 'http://beeg.com/tag/natural/1/', 'getIndex', '', '1')
		addDir('Natural tits', 'http://beeg.com/tag/natural+tits/1/', 'getIndex', '', '1')
		addDir('New face', 'http://beeg.com/tag/new+face/1/', 'getIndex', '', '1')
		addDir('Next door', 'http://beeg.com/tag/next+door/1/', 'getIndex', '', '1')
		addDir('Nun', 'http://beeg.com/tag/nun/1/', 'getIndex', '', '1')
		addDir('Nurse', 'http://beeg.com/tag/nurse/1/', 'getIndex', '', '1')
		addDir('Nylon', 'http://beeg.com/tag/nylon/1/', 'getIndex', '', '1')
		addDir('Observe', 'http://beeg.com/tag/observe/1/', 'getIndex', '', '1')
		addDir('Office', 'http://beeg.com/tag/office/1/', 'getIndex', '', '1')
		addDir('Office girl', 'http://beeg.com/tag/office+girl/1/', 'getIndex', '', '1')
		addDir('Oiled', 'http://beeg.com/tag/oiled/1/', 'getIndex', '', '1')
		addDir('Old & young', 'http://beeg.com/tag/old+young/1/', 'getIndex', '', '1')
		addDir('Old man', 'http://beeg.com/tag/old+man/1/', 'getIndex', '', '1')
		addDir('On cam', 'http://beeg.com/tag/on+cam/1/', 'getIndex', '', '1')
		addDir('Orgasm', 'http://beeg.com/tag/orgasm/1/', 'getIndex', '', '1')
		addDir('Orgy', 'http://beeg.com/tag/orgy/1/', 'getIndex', '', '1')
		addDir('Oriental', 'http://beeg.com/tag/oriental/1/', 'getIndex', '', '1')
		addDir('Outdoor', 'http://beeg.com/tag/outdoor/1/', 'getIndex', '', '1')
		addDir('Panties', 'http://beeg.com/tag/panties/1/', 'getIndex', '', '1')
		addDir('Panties off', 'http://beeg.com/tag/panties+off/1/', 'getIndex', '', '1')
		addDir('Pantyhose', 'http://beeg.com/tag/pantyhose/1/', 'getIndex', '', '1')
		addDir('Park', 'http://beeg.com/tag/park/1/', 'getIndex', '', '1')
		addDir('Party', 'http://beeg.com/tag/party/1/', 'getIndex', '', '1')
		addDir('Patient', 'http://beeg.com/tag/patient/1/', 'getIndex', '', '1')
		addDir('Peeing', 'http://beeg.com/tag/peeing/1/', 'getIndex', '', '1')
		addDir('Penetration', 'http://beeg.com/tag/penetration/1/', 'getIndex', '', '1')
		addDir('Perky tits', 'http://beeg.com/tag/perky+tits/1/', 'getIndex', '', '1')
		addDir('Petite', 'http://beeg.com/tag/petite/1/', 'getIndex', '', '1')
		addDir('Piercing', 'http://beeg.com/tag/piercing/1/', 'getIndex', '', '1')
		addDir('Pigtails', 'http://beeg.com/tag/pigtails/1/', 'getIndex', '', '1')
		addDir('Pink', 'http://beeg.com/tag/pink/1/', 'getIndex', '', '1')
		addDir('Pissing', 'http://beeg.com/tag/pissing/1/', 'getIndex', '', '1')
		addDir('Plump', 'http://beeg.com/tag/plump/1/', 'getIndex', '', '1')
		addDir('Pool', 'http://beeg.com/tag/pool/1/', 'getIndex', '', '1')
		addDir('Pornstar', 'http://beeg.com/tag/pornstar/1/', 'getIndex', '', '1')
		addDir('Posing', 'http://beeg.com/tag/posing/1/', 'getIndex', '', '1')
		addDir('Pov', 'http://beeg.com/tag/pov/1/', 'getIndex', '', '1')
		addDir('Pregnant', 'http://beeg.com/tag/pregnant/1/', 'getIndex', '', '1')
		addDir('Pretty', 'http://beeg.com/tag/pretty/1/', 'getIndex', '', '1')
		addDir('Public', 'http://beeg.com/tag/public/1/', 'getIndex', '', '1')
		addDir('Punishment', 'http://beeg.com/tag/punishment/1/', 'getIndex', '', '1')
		addDir('Pussy', 'http://beeg.com/tag/pussy/1/', 'getIndex', '', '1')
		addDir('Pussy cumshot', 'http://beeg.com/tag/pussy+cumshot/1/', 'getIndex', '', '1')
		addDir('Quickie', 'http://beeg.com/tag/quickie/1/', 'getIndex', '', '1')
		addDir('Rare face', 'http://beeg.com/tag/rare+face/1/', 'getIndex', '', '1')
		addDir('Rare position', 'http://beeg.com/tag/rare+position/1/', 'getIndex', '', '1')
		addDir('Real', 'http://beeg.com/tag/real/1/', 'getIndex', '', '1')
		addDir('Redhead', 'http://beeg.com/tag/redhead/1/', 'getIndex', '', '1')
		addDir('Retro', 'http://beeg.com/tag/retro/1/', 'getIndex', '', '1')
		addDir('Role', 'http://beeg.com/tag/role/1/', 'getIndex', '', '1')
		addDir('Romantic', 'http://beeg.com/tag/romantic/1/', 'getIndex', '', '1')
		addDir('Rough sex', 'http://beeg.com/tag/rough+sex/1/', 'getIndex', '', '1')
		addDir('Russian', 'http://beeg.com/tag/russian/1/', 'getIndex', '', '1')
		addDir('Scene', 'http://beeg.com/tag/scene/1/', 'getIndex', '', '1')
		addDir('School', 'http://beeg.com/tag/school/1/', 'getIndex', '', '1')
		addDir('Schoolgirl', 'http://beeg.com/tag/schoolgirl/1/', 'getIndex', '', '1')
		addDir('Scream', 'http://beeg.com/tag/scream/1/', 'getIndex', '', '1')
		addDir('Secretary', 'http://beeg.com/tag/secretary/1/', 'getIndex', '', '1')
		addDir('Seduction', 'http://beeg.com/tag/seduction/1/', 'getIndex', '', '1')
		addDir('Sex', 'http://beeg.com/tag/sex/1/', 'getIndex', '', '1')
		addDir('Shaved', 'http://beeg.com/tag/shaved/1/', 'getIndex', '', '1')
		addDir('Shaving', 'http://beeg.com/tag/shaving/1/', 'getIndex', '', '1')
		addDir('Shemale', 'http://beeg.com/tag/shemale/1/', 'getIndex', '', '1')
		addDir('Short hose', 'http://beeg.com/tag/short+hose/1/', 'getIndex', '', '1')
		addDir('Shower', 'http://beeg.com/tag/shower/1/', 'getIndex', '', '1')
		addDir('Showing off', 'http://beeg.com/tag/showing+off/1/', 'getIndex', '', '1')
		addDir('Shy', 'http://beeg.com/tag/shy/1/', 'getIndex', '', '1')
		addDir('Sister', 'http://beeg.com/tag/sister/1/', 'getIndex', '', '1')
		addDir('Skinny', 'http://beeg.com/tag/skinny/1/', 'getIndex', '', '1')
		addDir('Skirt', 'http://beeg.com/tag/skirt/1/', 'getIndex', '', '1')
		addDir('Slave', 'http://beeg.com/tag/slave/1/', 'getIndex', '', '1')
		addDir('Sleep', 'http://beeg.com/tag/sleep/1/', 'getIndex', '', '1')
		addDir('Slow', 'http://beeg.com/tag/slow/1/', 'getIndex', '', '1')
		addDir('Small tits', 'http://beeg.com/tag/small+tits/1/', 'getIndex', '', '1')
		addDir('Smoke', 'http://beeg.com/tag/smoke/1/', 'getIndex', '', '1')
		addDir('Socks', 'http://beeg.com/tag/socks/1/', 'getIndex', '', '1')
		addDir('Sofa', 'http://beeg.com/tag/sofa/1/', 'getIndex', '', '1')
		addDir('Solo', 'http://beeg.com/tag/solo/1/', 'getIndex', '', '1')
		addDir('Spanish', 'http://beeg.com/tag/spanish/1/', 'getIndex', '', '1')
		addDir('Spanking', 'http://beeg.com/tag/spanking/1/', 'getIndex', '', '1')
		addDir('Spontaneous', 'http://beeg.com/tag/spontaneous/1/', 'getIndex', '', '1')
		addDir('Sporty', 'http://beeg.com/tag/sporty/1/', 'getIndex', '', '1')
		addDir('Spreading', 'http://beeg.com/tag/spreading/1/', 'getIndex', '', '1')
		addDir('Squirt', 'http://beeg.com/tag/squirt/1/', 'getIndex', '', '1')
		addDir('Standing position', 'http://beeg.com/tag/standing+position/1/', 'getIndex', '', '1')
		addDir('Starlet', 'http://beeg.com/tag/starlet/1/', 'getIndex', '', '1')
		addDir('Step-daughter', 'http://beeg.com/tag/step-daughter/1/', 'getIndex', '', '1')
		addDir('Step-mom', 'http://beeg.com/tag/step-mom/1/', 'getIndex', '', '1')
		addDir('Strapon', 'http://beeg.com/tag/strapon/1/', 'getIndex', '', '1')
		addDir('Stretching', 'http://beeg.com/tag/stretching/1/', 'getIndex', '', '1')
		addDir('Strip', 'http://beeg.com/tag/strip/1/', 'getIndex', '', '1')
		addDir('Student', 'http://beeg.com/tag/student/1/', 'getIndex', '', '1')
		addDir('Stupid', 'http://beeg.com/tag/stupid/1/', 'getIndex', '', '1')
		addDir('Submissive', 'http://beeg.com/tag/submissive/1/', 'getIndex', '', '1')
		addDir('Swallow', 'http://beeg.com/tag/swallow/1/', 'getIndex', '', '1')
		addDir('Swedish', 'http://beeg.com/tag/swedish/1/', 'getIndex', '', '1')
		addDir('Swinger', 'http://beeg.com/tag/swinger/1/', 'getIndex', '', '1')
		addDir('Table', 'http://beeg.com/tag/table/1/', 'getIndex', '', '1')
		addDir('Tall', 'http://beeg.com/tag/tall/1/', 'getIndex', '', '1')
		addDir('Tanned', 'http://beeg.com/tag/tanned/1/', 'getIndex', '', '1')
		addDir('Tattoo', 'http://beeg.com/tag/tattoo/1/', 'getIndex', '', '1')
		addDir('Teacher', 'http://beeg.com/tag/teacher/1/', 'getIndex', '', '1')
		addDir('Tease', 'http://beeg.com/tag/tease/1/', 'getIndex', '', '1')
		addDir('Teen', 'http://beeg.com/tag/teen/1/', 'getIndex', '', '1')
		addDir('Teen anal', 'http://beeg.com/tag/teen+anal/1/', 'getIndex', '', '1')
		addDir('Teen hardcore', 'http://beeg.com/tag/teen+hardcore/1/', 'getIndex', '', '1')
		addDir('Threesome', 'http://beeg.com/tag/threesome/1/', 'getIndex', '', '1')
		addDir('Tied', 'http://beeg.com/tag/tied/1/', 'getIndex', '', '1')
		addDir('Tight', 'http://beeg.com/tag/tight/1/', 'getIndex', '', '1')
		addDir('Tight body', 'http://beeg.com/tag/tight+body/1/', 'getIndex', '', '1')
		addDir('Tits cumshot', 'http://beeg.com/tag/tits+cumshot/1/', 'getIndex', '', '1')
		addDir('Tits fuck', 'http://beeg.com/tag/tits+fuck/1/', 'getIndex', '', '1')
		addDir('Toilet', 'http://beeg.com/tag/toilet/1/', 'getIndex', '', '1')
		addDir('Toy', 'http://beeg.com/tag/toy/1/', 'getIndex', '', '1')
		addDir('Transexual', 'http://beeg.com/tag/transexual/1/', 'getIndex', '', '1')
		addDir('Turkish', 'http://beeg.com/tag/turkish/1/', 'getIndex', '', '1')
		addDir('Undressing', 'http://beeg.com/tag/undressing/1/', 'getIndex', '', '1')
		addDir('Unusual', 'http://beeg.com/tag/unusual/1/', 'getIndex', '', '1')
		addDir('Unusual location', 'http://beeg.com/tag/unusual+location/1/', 'getIndex', '', '1')
		addDir('Upskirt', 'http://beeg.com/tag/upskirt/1/', 'getIndex', '', '1')
		addDir('Vintage', 'http://beeg.com/tag/vintage/1/', 'getIndex', '', '1')
		addDir('Virgin', 'http://beeg.com/tag/virgin/1/', 'getIndex', '', '1')
		addDir('Voyeur', 'http://beeg.com/tag/voyeur/1/', 'getIndex', '', '1')
		addDir('Webcam', 'http://beeg.com/tag/webcam/1/', 'getIndex', '', '1')
		addDir('Wet', 'http://beeg.com/tag/wet/1/', 'getIndex', '', '1')
		addDir('White', 'http://beeg.com/tag/white/1/', 'getIndex', '', '1')
		addDir('Wife', 'http://beeg.com/tag/wife/1/', 'getIndex', '', '1')
		addDir('Young', 'http://beeg.com/tag/young/1/', 'getIndex', '', '1')
		addDir('Young & old', 'http://beeg.com/tag/young+old/1/', 'getIndex', '', '1')
		addDir('Young couple', 'http://beeg.com/tag/young+couple/1/', 'getIndex', '', '1')

def SEARCH(url):
        input = ''
        keyboard = xbmc.Keyboard(input, 'Search clip')
        keyboard.doModal()
        if keyboard.isConfirmed():
            input = keyboard.getText().replace(' ','+')            
            if input == None:
                return False
        if not re.match('[A-Za-z0-9 ]', input):     # this part doesn't work for some reason...
            d = xbmcgui.Dialog()
            d.ok(NAME, 'Please use only alphanumeric values')  
            CATEGORIES()
            return False
        INDEX(url + input, 1)


def INDEX(url,page):
        # Grabbing the URL
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (iPad; U; CPU OS OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10')
        response = urllib2.urlopen(req)
        link = response.read()
        response.close()
		
        # Getting all the data from the url
        IDString = re.compile('var tumbid  =\[(.+?)\];').findall(link)
        NamesString = re.compile('var tumbalt =\[(.+?)\];').findall(link)

    
        # Processing data into usable data
        AllIDs = re.split('\,+', IDString[0])
        NamesString[0] = NamesString[0].lstrip('\'')
        NamesString[0] = NamesString[0].rstrip('\'')
        AllNames = re.split('\'\,\'+', NamesString[0])


        DIRPAGER(url, link, page)
        
        # Content loop
        for number, name in zip(AllIDs, AllNames):
            addDownLink(name,number,'getVideo','http://cdn.anythumb.com/236x177/' + number + '.jpg')

        DIRPAGER(url, link, page)
        xbmc.executebuiltin("Container.SetViewMode(500)")
 
def DIRPAGER(url, link, page):

        PageNumbersNormal = re.compile('<a href="/section/(.+?)/([0-9]+)/" target="_self">').findall(link)
        PageNumbersTags = re.compile('<a href="/tag/(.+?)/([0-9]+)/" target="_self">').findall(link)
        PageNumbersSearch = re.compile('<a href="/search\?q=([0-9a-zA-Z ]+)\&page=([0-9]+)" target="_self">').findall(link)
        
        page = int(page)
        PageNumbers = 1
        # Page stuff
        if PageNumbersSearch:
            PageNumbers = PageNumbersSearch[-1][-1]
            url = re.sub('[0-9]+$', '', url)
            if page <= 1:
                url = url + '&page='
            if page < int(PageNumbers):
                addDir('Next page (' + str(page+1) + ')', url + str(page+1), 'getIndex', '', str(page+1))
                return False
            return False
        elif PageNumbersNormal:
            PageNumbers = PageNumbersNormal[-1][-1]
            url = re.sub('[0-9]+/$', '', url)
        elif PageNumbersTags:
            PageNumbers = PageNumbersTags[-1][-1]
            url = re.sub('[0-9]+/$', '', url)
            
        print(PageNumbers)
        if page < int(PageNumbers):
            addDir('Next page (' + str(page+1) + ')', url + str(page+1) + '/', 'getIndex', '', str(page+1))

            
def GetPlayerCore():
	try:
		PlayerMethod=getSet("core-player")
		if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
		elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
		elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
		else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	except: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	return PlayerMeth

def VIDEOLINKS(url,name):
        listitem = xbmcgui.ListItem(name)
        listitem.setInfo('video', {'Title': name, 'Genre': 'Porn'})
        VidRes=getSet('vide-res','480p')
        URL='http://video.beeg.com/speed=9.0/buffer=600/data=pc.US/'+VidRes+'/'+url+'.mp4'
        if VidRes != '480p':
            URLCheck=urllib.urlopen(URL)
            URLCheck.close()
            URLCheck=URLCheck.getcode()
            if URLCheck == 404:
                VidRes='480p'
                URL='http://video.beeg.com/speed=9.0/buffer=600/data=pc.US/'+VidRes+'/'+url+'.mp4'
        xbmc.Player(GetPlayerCore()).play(URL, listitem)
        #xbmc.Player().play('http://video.mystreamservice.com/480p/'+url+'.mp4', listitem)
        #http://video.beeg.com/speed=9.0/buffer=600/data=pc.US/720p/3811109.mp4
        #http://video.beeg.com/speed=9.0/buffer=600/data=pc.US/480p/3811109.mp4
        #http://video.beeg.com/speed=9.0/buffer=600/data=pc.US/240p/3811109.mp4
        #

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
        name = name.replace("\\", "")
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDir(name,url,mode,iconimage,page):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&page="+urllib.quote_plus(page)
        ok=True
        name = name.replace("\\", "")
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


        
def MODESWITCHER():
        params=get_params()
        url=None
        name=None
        mode=None
        page=None

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
                mode=urllib.unquote_plus(params["mode"])
        except:
                pass
        try:
                page=int(params["page"])
        except:
                pass

        print "Mode: "+str(mode)
        print "URL: "+str(url)
        print "Name: "+str(name)
        print "Page: "+str(page)

        
        for case in switch(mode):
            if case('A'): pass
            if case(None):
                print ""
                CATEGORIES()
                break
            if case('getSiteCategories'):
                SITE_CATEGORIES()
                break
            if case('getIndex'):
                INDEX(url, page)
                break
            if case('getVideo'):
                VIDEOLINKS(url,name)
                break
            if case('getSearch'):
                SEARCH(url)
                break
            if case(): # default
                print ""
                CATEGORIES()
                break


MODESWITCHER()
xbmcplugin.endOfDirectory(int(sys.argv[1]))
