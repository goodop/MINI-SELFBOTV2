import json

class Autobots(object):

    '''

        DONT CHANGE OR REMOVE IF YOU ARE NOT SURE WHAT YOU DO :)
        TEMPLATE BY : THE AUTOBOTS CORPORATION (STANDAR DESIGN)

    '''

    def __init__(self):
        self.rname = json.loads(open('Data/settings.json','r').read())["rname"]
        if self.rname != "":
            self.rname = self.rname + " "
        self.pushMsg = "line://app/1655623470-81eDd9kM"
        self.badge = "https://imjustgood.com/img/yellow-logo.png"
        self.branding = "IMJUSTGOOD.COM"
        self.brandingURL = "https://api.imjustgood.com/custom/tools"
        self.hostMenu = "https://imjustgood.com/img/flex"
        print(f"{self.branding} STARTED UP !\n")

    def ERROR(self,data):
        result = {"type": "bubble", "size": "micro", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "ERROR!!", "color": "#e00000", "weight": "bold"}, {"type": "text", "text": f"{data}", "color": "#e00000", "size": "xxs", "wrap": True } ], "backgroundColor": "#000000"} }
        if data == "ERROR" or data == "Not found.":
           if data != "Not found.":
              data = data+"!!"
           result = {"type": "bubble", "size": "nano", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{data.replace('.','').upper()}", "color": "#e00000", "weight": "bold"}, ], "backgroundColor": "#000000"} }
        return result

    def pushText(self,text):
        print(text)
        result = text.replace(' ','%20').replace('\n','%0A')
        return result

    def youtube(self,data):
        author = data["author"]
        duration = data["duration"]
        thumbnail = data["thumbnail"]
        title = data["title"]
        watched = data["watched"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": thumbnail, "aspectRatio": "2:1", "aspectMode": "cover", "size": "full"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "YOUTUBE", "weight": "bold", "color": "#ff0000", "size": "xxs"} ], "position": "absolute", "backgroundColor": "#ffffff", "paddingAll": "5px"} ], "flex": 0 }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": title, "weight": "bold", "wrap": True, "decoration": "underline", "size": "xs"} ], "paddingTop": "5px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Author", "size": "xs"}, {"type": "text", "text": "Duration", "size": "xs"}, {"type": "text", "text": "Watched", "size": "xs"} ], "paddingEnd": "10px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": author, "size": "xs"}, {"type": "text", "text": duration, "size": "xs"}, {"type": "text", "text": f"{watched}x", "size": "xs"} ], "paddingEnd": "15px", "flex": 2 } ], "backgroundColor": "#ffffff", "paddingTop": "5px"} ], "paddingAll": "10px", "cornerRadius": "10px"} }
        return result

    def joox(self,data):
        artist = data["singer"]
        duration = data["duration"]
        thumbnail = data["thumbnail"]
        title = data["title"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": thumbnail, "aspectRatio": "1:1", "aspectMode": "cover", "align": "start"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "JOOX", "weight": "bold", "color": "#28a745", "size": "xxs"} ], "position": "absolute", "backgroundColor": "#141414", "paddingAll": "5px"} ], "flex": 0 }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": title, "color": "#ffffff", "weight": "bold", "wrap": True, "maxLines": 2 }, {"type": "text", "text": artist, "size": "xs", "color": "#ffffff"}, {"type": "text", "text": duration, "size": "xs", "color": "#ffffff"} ], "paddingEnd": "10px", "paddingStart": "10px", "justifyContent": "center"} ] } ], "paddingAll": "10px", "cornerRadius": "10px"}, "styles": {"body": {"backgroundColor": "#141414"} } }
        return result

    def lyric(self,data):
        artist = data["artist"]
        title = data["title"]
        lyrics = data["lyric"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{title} - {artist}", "weight": "bold", "wrap": True } ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": lyrics, "wrap": True, "size": "xxs"} ], "paddingTop": "8px"} ], "paddingAll": "15px", "paddingStart": "20px", "paddingEnd": "20px", "paddingBottom": "20px"} }
        return result

    def facebook(self,data):
        author = data["author"]
        caption = data["caption"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Facebook", "weight": "bold", "color": "#ffffff", "size": "lg"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": author, "size": "sm"}, {"type": "separator", "margin": "xs"}, {"type": "text", "text": caption+" ", "wrap": True, "size": "xxs", "style": "italic", "margin": "sm", "color": "#00000088"} ], "backgroundColor": "#ffffff", "paddingAll": "5px"} ], "paddingAll": "5px", "paddingStart": "10px", "paddingEnd": "10px", "paddingBottom": "10px"}, "styles": {"body": {"backgroundColor": "#255e9a"} } }
        return result

    def instagram(self,data):
        pict = data["picture"]
        fullname = data["fullname"]
        if fullname == "" or fullname is None:
            fullname = data["username"]
        biography = data["biography"]
        post = data["post"]
        follower = data["follower"]
        following = data["following"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Instagram Profile", "weight": "bold", "size": "lg"} ], "paddingBottom": "5px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pict, "aspectRatio": "1:1", "aspectMode": "cover", "align": "start", "action": {"type": "uri", "uri": pict } } ], "cornerRadius": "100px", "width": "100px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": fullname, "size": "sm", "weight": "bold"}, {"type": "separator", "margin": "xs"}, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "margin": "md", "contents": [{"type": "span", "text": f"{post} "}, {"type": "span", "text": "Post", "weight": "bold"} ] }, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "margin": "sm", "contents": [{"type": "span", "text": f"{follower} "}, {"type": "span", "text": "Followers", "weight": "bold"} ] }, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "margin": "sm", "contents": [{"type": "span", "text": f"{following} "}, {"type": "span", "text": "Following", "weight": "bold"} ] } ], "backgroundColor": "#ffffff", "paddingAll": "5px", "paddingStart": "15px"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": biography+" ", "size": "xxs", "color": "#00000088", "wrap": True} ], "paddingTop": "10px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px"} }
        return result

    def instapost(self,data):
        picture = data["picture"]
        fullname = data["fullname"]
        if fullname == "" or fullname is None:
            fullname = data["username"]
        caption = data["caption"]
        created = data["created"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Instagram Post", "weight": "bold", "size": "lg"} ], "paddingBottom": "5px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": picture, "aspectRatio": "1:1", "aspectMode": "cover", "align": "start", "action": {"type": "uri", "uri": picture }, "size": "xs"} ], "width": "60px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": fullname, "size": "sm", "weight": "bold"}, {"type": "separator", "margin": "xs"}, {"type": "text", "text": created, "color": "#00000088", "size": "xs", "margin": "md"} ], "backgroundColor": "#ffffff", "paddingAll": "5px", "paddingStart": "15px"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{caption} ", "size": "xxs", "color": "#00000088", "wrap": True } ], "paddingTop": "10px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px"} }
        return result

    def instastory(self,data,count):
        picture = data["picture"]
        fullname = data["fullname"]
        if fullname == "" or fullname is None:
            fullname = data["username"]
        created = data["stories"][count]["created"]
        playUrl = data["stories"][count]["url"]
        stories = f"https://instagram.com/stories/{data['username']}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Instagram Stories", "weight": "bold", "size": "lg"} ], "paddingBottom": "5px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": picture, "aspectRatio": "1:1", "aspectMode": "cover", "align": "start", "action": {"type": "uri", "uri": picture }, "size": "sm"} ], "flex": 0 }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": fullname, "weight": "bold"}, {"type": "separator", "margin": "xs"}, {"type": "text", "text": created, "size": "xs", "margin": "sm"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "STORY", "size": "xxs", "color": "#ffffff", "weight": "bold", "decoration": "underline", "align": "center"} ], "paddingBottom": "6px", "background": {"type": "linearGradient", "angle": "0deg", "startColor": "#ff0000", "endColor": "#e83e8c"}, "paddingTop": "2px", "action": {"type": "uri", "uri": stories } }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "PLAY", "size": "xxs", "color": "#ffffff", "weight": "bold", "decoration": "underline", "align": "center"} ], "paddingBottom": "6px", "background": {"type": "linearGradient", "angle": "0deg", "startColor": "#ff0000", "endColor": "#e83e8c"}, "paddingTop": "2px", "offsetStart": "5px", "action": {"type": "uri", "uri": playUrl }, "paddingEnd": "5px"} ], "paddingTop": "5px"} ], "backgroundColor": "#ffffff", "paddingAll": "5px", "paddingStart": "10px", "paddingTop": "0px"} ] } ], "paddingAll": "5px", "paddingStart": "10px", "paddingEnd": "10px", "paddingBottom": "10px"} }
        return result

    def twitter(self,data):
        avatar = data["avatar"]
        fullname = data["fullname"]
        if fullname == "" or fullname is None:
            fullname = data["username"]
        biography = data["biography"]
        tweet = data["tweet"]
        followers = data["follower"]
        following = data["following"]
        result= {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Twitter Profile", "weight": "bold", "size": "lg", "color": "#ffffffee"} ], "paddingBottom": "5px"}, {"type": "separator"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": avatar, "aspectRatio": "1:1", "aspectMode": "cover", "align": "start", "action": {"type": "uri", "uri": avatar } } ], "width": "100px", "paddingAll": "10px", "flex": 0, "paddingStart": "0px", "paddingBottom": "8px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": fullname, "weight": "bold", "color": "#ffffffee"}, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "contents": [{"type": "span", "text": f"{tweet} "}, {"type": "span", "text": "Tweet", "weight": "bold", "color": "#ffffffee"} ], "color": "#ffffffcc", "margin": "sm"}, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "margin": "sm", "contents": [{"type": "span", "text": f"{followers} "}, {"type": "span", "text": "Followers", "weight": "bold", "color": "#ffffffee"} ], "color": "#ffffffcc"}, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "margin": "sm", "contents": [{"type": "span", "text": f"{following} "}, {"type": "span", "text": "Following", "weight": "bold", "color": "#ffffffee"} ], "color": "#ffffffcc"} ], "paddingAll": "10px", "paddingStart": "0px", "paddingTop": "8px"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{biography} ", "size": "xxs", "color": "#ffffffcc", "wrap": True, "style": "italic"} ], "paddingTop": "0px", "paddingAll": "10px", "paddingStart": "0px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px"}, "styles": {"body": {"backgroundColor": "#182226"} } }
        return result

    def tiktok(self,data):
        picture = data["pictureUrl"]
        fullname = data["fullname"]
        if fullname == "" or fullname is None:
            fullname = data["username"]
        biography = data["biography"]
        vids = data["videos"]
        like = data["likes"]
        followers = data["followers"]
        following = data["following"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Justgood", "weight": "bold", "size": "lg", "contents": [{"type": "span", "text": "TikTok "}, {"type": "span", "text": "Profile", "color": "#ff0060"} ] } ], "paddingBottom": "5px"}, {"type": "separator"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": picture, "aspectRatio": "1:1", "aspectMode": "cover", "align": "start", "action": {"type": "uri", "uri": picture } } ], "paddingAll": "10px", "flex": 0, "paddingStart": "0px", "paddingBottom": "8px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": fullname, "weight": "bold"}, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "margin": "sm", "contents": [{"type": "span", "text": f"{followers} "}, {"type": "span", "text": "Followers", "weight": "bold"} ] }, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "margin": "sm", "contents": [{"type": "span", "text": f"{following} "}, {"type": "span", "text": "Following", "weight": "bold"} ] }, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "contents": [{"type": "span", "text": f"{vids} "}, {"type": "span", "text": "Videos", "weight": "bold"} ], "margin": "sm"}, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "contents": [{"type": "span", "text": f"{like} "}, {"type": "span", "text": "Likes", "weight": "bold"} ], "margin": "sm"} ], "paddingAll": "10px", "paddingStart": "0px", "paddingTop": "8px"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{biography} ", "size": "xxs", "wrap": True, "style": "italic"} ], "paddingTop": "0px", "paddingAll": "10px", "paddingStart": "0px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px"} }
        return result

    def smule(self,data):
        avatar = data["pictureUrl"]
        username = data["username"]
        album = f"ID : {data['accountId']}"
        album += f"\nFullname : {data['fullname']}"
        album += f"\nUsername : {data['username']}"
        album += f"\nVIP : {data['vip']}"
        album += f"\nVerified : {data['verified']}"
        album += f"\nLocation : {data['location']}"
        album += f"\nFollowers : {data['followers']}"
        album += f"\nFollowing : {data['following']}"
        album += f"\nRecording : {data['recording']}"
        album += f"\nBiography : {data['biography']}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Smule", "weight": "bold", "size": "xxs", "color": "#3ac927"} ], "position": "absolute", "borderWidth": "1px", "borderColor": "#3ac927", "cornerRadius": "50px", "paddingTop": "2px", "paddingBottom": "3px", "paddingAll": "10px", "offsetTop": "15px", "offsetStart": "15px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": avatar, "aspectRatio": "1:1", "aspectMode": "cover", "action": {"type": "uri", "uri": avatar }, "align": "center"} ], "cornerRadius": "100px"} ], "alignItems": "center", "paddingTop": "40px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": username, "weight": "bold", "align": "center", "color": "#ffffffcc"} ], "paddingTop": "5px", "paddingBottom": "20px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Recording", "weight": "bold", "color": "#ffffffcc", "size": "sm"} ], "paddingTop": "5px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": album[:-1], "size": "xxs", "color": "#ffffffcc", "wrap": True } ], "paddingAll": "10px", "paddingTop": "5px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px"}, "styles": {"body": {"backgroundColor": "#121212"} } }
        return result

    def github(self,data):
        avatar = data["avatar"]
        fullname = data["fullname"]
        if fullname == "" or fullname is None:
            fullname = data["username"]
        biography = data["bio"]
        repo = data["repositories"]
        followers = data["followers"]
        following = data["following"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "GitHub", "size": "lg", "weight": "bold", "color": "#ffffffdd"} ], "paddingBottom": "5px"}, {"type": "separator"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": avatar, "aspectRatio": "1:1", "aspectMode": "cover", "align": "start", "action": {"type": "uri", "uri": avatar }, "size": "sm"} ], "paddingAll": "10px", "flex": 0, "paddingStart": "0px", "paddingBottom": "8px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": fullname, "weight": "bold", "color": "#ffffffdd"}, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "margin": "sm", "contents": [{"type": "span", "text": f"{followers} "}, {"type": "span", "text": "Followers", "weight": "bold", "color": "#ffffffdd"} ], "color": "#ffffffaa"}, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "margin": "sm", "contents": [{"type": "span", "text": f"{following} "}, {"type": "span", "text": "Following", "weight": "bold", "color": "#ffffffdd"} ], "color": "#ffffffaa"}, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "contents": [{"type": "span", "text": f"{repo} "}, {"type": "span", "text": "Repositories", "weight": "bold", "color": "#ffffffdd"} ], "margin": "sm", "color": "#ffffffaa"} ], "paddingAll": "10px", "paddingStart": "0px", "paddingTop": "8px"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{biography} ", "size": "xxs", "color": "#ffffffdd", "wrap": True, "style": "italic"} ], "paddingTop": "0px", "paddingAll": "10px", "paddingStart": "0px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px"}, "styles": {"body": {"backgroundColor": "#0d1117"} } }
        return result

    def timeline(self,data):
        picture = data["pictureUrl"]
        name = data["displayName"]
        like = data["like"]
        share = data["share"]
        caption = data["caption"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "JUSTGOOD", "size": "lg", "weight": "bold", "contents": [{"type": "span", "text": "LINE ", "color": "#2dda15"}, {"type": "span", "text": "TIMELINE"} ] } ], "paddingBottom": "5px"}, {"type": "separator"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": picture, "aspectRatio": "1:1", "aspectMode": "cover", "align": "start", "action": {"type": "uri", "uri": picture }, "size": "sm"} ], "paddingAll": "10px", "flex": 0, "paddingStart": "0px", "paddingBottom": "0px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{name} ", "weight": "bold"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{caption} ", "size": "xxs", "wrap": True } ], "paddingTop": "5px", "paddingAll": "10px", "paddingStart": "0px", "paddingBottom": "0px"}, {"type": "text", "text": "JUSTGOOD", "size": "xxs", "margin": "md", "contents": [{"type": "span", "text": f"{like} "}, {"type": "span", "text": "Like ", "weight": "bold"}, {"type": "span", "text": f"{share} "}, {"type": "span", "text": "Share", "weight": "bold"} ], "wrap": True } ], "paddingAll": "10px", "paddingStart": "0px", "paddingTop": "8px", "paddingBottom": "0px"} ] } ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "15px"} }
        return result

    def wikipedia(self,data):
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Wikipedia", "weight": "bold", "size": "xl"}, {"type": "text", "text": data, "size": "xxs", "margin": "md", "wrap": True } ], "paddingStart": "20px", "paddingEnd": "20px", "paddingBottom": "20px"} }
        return result

    def urban(self,data):
        definition = data["definition"].replace("[","").replace("]","")
        example = data["example"].replace("[","").replace("]","")
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "RendyTR OK", "weight": "bold", "size": "lg", "contents": [{"type": "span", "text": "Urban ", "color": "#ff0000"}, {"type": "span", "text": "Dictionary", "color": "#ffe400"} ] } ], "backgroundColor": "#081d3f", "paddingAll": "10px", "paddingStart": "13px", "paddingEnd": "13px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "RENDS", "size": "xxs", "wrap": True, "contents": [{"type": "span", "text": "[ DEFINITION ] ", "color": "#ff0000"}, {"type": "span", "text": definition} ] }, {"type": "text", "text": "RENDS", "size": "xxs", "wrap": True, "contents": [{"type": "span", "text": "[ EXAMPLE ] ", "color": "#ff0000"}, {"type": "span", "text": example } ], "margin": "lg"} ] } ], "backgroundColor": "#ffffff", "paddingAll": "20px"} ], "backgroundColor": "#00476455", "paddingAll": "20px"} ], "paddingAll": "0px"} }
        return result

    def kbbi(self,data,query):
        desc = data["desc"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "KBBI", "weight": "bold", "color": "#ff0000", "size": "lg"} ], "flex": 0, "paddingEnd": "15px"}, {"type": "separator"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Kamus Besar", "size": "xxs", "color": "#ffffff"}, {"type": "text", "text": "Bahasa Indonesia", "size": "xxs", "color": "#ffffff"} ], "paddingStart": "15px", "paddingEnd": "15px"} ], "backgroundColor": "#212121", "paddingAll": "13px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": query.upper(), "size": "xs", "weight": "bold", "align": "center", "decoration": "underline"}, {"type": "text", "text": desc, "size": "xxs", "margin": "lg", "wrap": True } ], "backgroundColor": "#ffffff", "paddingAll": "20px", "paddingBottom": "30px"} ], "backgroundColor": "#999999", "paddingAll": "20px"} ], "paddingAll": "0px"} }
        return result

    def zodiac(self,data):
        dateRange = data["date"]
        sign = data["zodiac"]
        imageUrl = data["image"]
        desc = f"Kecocokan : {data['couple']}"
        desc += f"\nWaktu Hoki : {data['time']}"
        desc += f"\nWarna Hoki : {data['color']}"
        desc += f"\nNomor Hoki : {data['number']}"
        desc += f"\n\nUmum : {data['public']}"
        desc += f"\n\nAsmara Jomblo : {data['love']['single']}"
        desc += f"\n\nAsmara Pasangan : {data['love']['couple']}"
        desc += f"\n\nKeuangan : {data['money']}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "ZODIAC", "weight": "bold", "size": "xxs"} ], "position": "absolute", "offsetTop": "15px", "offsetStart": "15px", "borderWidth": "1px", "borderColor": "#000000cc", "cornerRadius": "50px", "paddingStart": "7px", "paddingEnd": "7px", "paddingTop": "2px", "paddingBottom": "2px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": imageUrl, "aspectRatio": "1:1", "aspectMode": "cover", "action": {"type": "uri", "uri": imageUrl } } ], "cornerRadius": "100px"} ], "alignItems": "center", "paddingTop": "20px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": sign.upper(), "weight": "bold"}, {"type": "text", "text": dateRange, "size": "xs"} ], "alignItems": "center", "paddingTop": "10px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": desc, "size": "xxs", "wrap": True } ], "paddingTop": "15px", "paddingBottom": "5px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px"} }
        return result

    def porn(self,data):
        pict = data["thumbnail"]
        title = data["title"].upper()
        duration = data["duration"]
        quality = data["quality"]
        watched = data["watched"]
        vids = data["videoUrl"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pict, "aspectRatio": "2:1.3", "aspectMode": "cover", "action": {"type": "uri", "uri": pict }, "size": "full"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "PORN", "weight": "bold", "size": "xxs", "color": "#ffffff"} ], "position": "absolute", "paddingStart": "15px", "paddingEnd": "15px", "paddingTop": "7px", "paddingBottom": "7px", "backgroundColor": "#212121"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": title, "weight": "bold", "color": "#ffffffcc", "maxLines": 2, "wrap": True, "decoration": "underline"} ], "paddingTop": "10px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "Duration", "size": "xs", "color": "#ffffffcc", "weight": "bold"}, {"type": "text", "text": duration, "size": "xs", "color": "#ffffffcc", "flex": 2 } ], "paddingTop": "5px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "Quality", "size": "xs", "color": "#ffffffcc", "weight": "bold"}, {"type": "text", "text": quality, "size": "xs", "color": "#ffffffcc", "flex": 2 } ] }, {"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "Watched", "size": "xs", "color": "#ffffffcc", "weight": "bold"}, {"type": "text", "text": watched, "size": "xs", "color": "#ffffffcc", "flex": 2 } ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "PLAY", "color": "#ffffffcc", "decoration": "underline", "weight": "bold"} ], "position": "absolute", "offsetEnd": "10px", "background": {"type": "linearGradient", "angle": "30deg", "startColor": "#900000", "endColor": "#ff0000", "centerColor": "#900000"}, "paddingAll": "12px", "offsetBottom": "10px", "cornerRadius": "10px", "action": {"type": "uri", "uri": vids } } ], "paddingAll": "10px"}, "styles": {"body": {"backgroundColor": "#212121"} } }
        return result

    def pornstar(self,data):
        lonte = data["pornstar"].upper()
        biodata = f"Gender : {data['gender']}"
        biodata += f"\nBirth : {data['birth']}"
        biodata += f"\nCountry : {data['country']}"
        biodata += f"\nHeight : {data['height']}"
        if data['gender'] == "male":
            biodata += f"\nDick : {data['dick']}"
        if data['gender'] == "female":
            biodata += f"\nTits : {data['tits']}"
            biodata += f"\nBreast : {data['breast']}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Pornstars", "weight": "bold", "color": "#eea60b"} ], "flex": 0, "paddingEnd": "15px", "justifyContent": "center", "paddingStart": "5px"} ], "backgroundColor": "#141414", "paddingAll": "13px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": lonte, "size": "xs", "weight": "bold", "wrap": True, "color": "#ffffff"}, {"type": "text", "text": biodata, "size": "xxs", "margin": "lg", "wrap": True, "color": "#ffffff"} ], "backgroundColor": "#000000cc", "paddingAll": "20px", "paddingBottom": "30px"} ], "backgroundColor": "#ee8b0b", "paddingAll": "20px"} ], "paddingAll": "0px"} }
        return result

    def kamasutra(self,data):
        pic = data["thumbnail"]
        gaya = data["style"]
        info = data["description"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pic, "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "action": {"type": "uri", "uri": pic } }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "KAMASUTRA", "size": "xxs", "color": "#ff0000"} ], "position": "absolute", "borderWidth": "1px", "borderColor": "#ff0000", "paddingStart": "5px", "paddingEnd": "5px", "paddingTop": "1px", "paddingBottom": "1px", "cornerRadius": "5px", "offsetTop": "5px", "offsetStart": "5px", "backgroundColor": "#00000011"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{gaya}".upper(), "weight": "bold", "wrap": True }, {"type": "text", "text": f"{info}", "wrap": True, "size": "xxs", "margin": "sm"} ], "paddingTop": "5px", "paddingEnd": "10px", "paddingStart": "10px"} ], "paddingAll": "0px", "paddingBottom": "13px"} }
        return result

    def dick(self,data,query):
        col = ["#000000","#ff0000","#ffffffcc","#ffffffcc"]
        pic = data["picture"]
        title = data["dick"]
        info = f"Ukuran : {data['size']}"
        info += f"\nKekuatan : {data['ability']}"
        info += f"\nKekerasan : {data['flexibility']}"
        info += f"\n\n{data['description']}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pic, "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "action": {"type": "uri", "uri": pic } }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{query}".upper(), "size": "xxs", "color": "#ff0000"} ], "position": "absolute", "borderWidth": "1px", "borderColor": col[1], "paddingStart": "5px", "paddingEnd": "5px", "paddingTop": "1px", "paddingBottom": "1px", "cornerRadius": "5px", "offsetTop": "5px", "offsetStart": "5px", "backgroundColor": "#00000011"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{title}".upper(), "weight": "bold", "wrap": True, "color": col[2] }, {"type": "text", "text": f"{info}", "wrap": True, "size": "xxs", "margin": "sm", "color": col[3] } ], "paddingTop": "5px", "paddingEnd": "10px", "paddingStart": "10px"} ], "paddingAll": "0px", "paddingBottom": "13px", "backgroundColor": col[0] } }
        return result

    def vagina(self,data,query):
        col = ["#fdbcb8","#ff0000","#ff0000","#ff0000"]
        pic = data["picture"]
        title = data["vagina"]
        info = f"Kedalaman : {data['depth']}"
        info += f"\nCengkraman : {data['grip']}"
        info += f"\nKelembapan : {data['humidity']}"
        info += f"\nElastisitas : {data['elasticity']}"
        info += f"\n\n{data['description']}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pic, "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "action": {"type": "uri", "uri": pic } }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{query}".upper(), "size": "xxs", "color": "#ff0000"} ], "position": "absolute", "borderWidth": "1px", "borderColor": col[1], "paddingStart": "5px", "paddingEnd": "5px", "paddingTop": "1px", "paddingBottom": "1px", "cornerRadius": "5px", "offsetTop": "5px", "offsetStart": "5px", "backgroundColor": "#ffffff"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{title}".upper(), "weight": "bold", "wrap": True, "color": col[2] }, {"type": "text", "text": f"{info}", "wrap": True, "size": "xxs", "margin": "sm", "color": col[3] } ], "paddingTop": "5px", "paddingEnd": "10px", "paddingStart": "10px"} ], "paddingAll": "0px", "paddingBottom": "13px", "backgroundColor": col[0] } }
        return result

    def tits(self,data,query):
        col = ["#ffffff","#ff0000","#000000","#000000"]
        pic = data["picture"]
        title = data["tits"]
        info = f"Ukuran : {data['size']} | {data['cup']}"
        info += f"\nPuting : {data['nipple']}"
        info += f"\nLingkar Puting : {data['aerola']}"
        info += f"\n\n{data['description']}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pic, "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "action": {"type": "uri", "uri": pic } }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{query}".upper(), "size": "xxs", "color": "#ff0000"} ], "position": "absolute", "borderWidth": "1px", "borderColor": col[1], "paddingStart": "5px", "paddingEnd": "5px", "paddingTop": "1px", "paddingBottom": "1px", "cornerRadius": "5px", "offsetTop": "5px", "offsetStart": "5px", "backgroundColor": "#ffffff"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{title}".upper(), "weight": "bold", "wrap": True, "color": col[2] }, {"type": "text", "text": f"{info}", "wrap": True, "size": "xxs", "margin": "sm", "color": col[3] } ], "paddingTop": "5px", "paddingEnd": "10px", "paddingStart": "10px"} ], "paddingAll": "0px", "paddingBottom": "13px", "backgroundColor": col[0] } }
        return result

    def cctvList(self,data):
        infos = ""
        for i in data:
            infos += f"\n{i}. {data[i]}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "STREETVIEW CODE", "weight": "bold", "size": "lg", "align": "center", "color": "#ff0000"} ], "paddingBottom": "5px"}, {"type": "separator"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": infos[1:], "size": "xxs", "wrap": True } ], "paddingAll": "10px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px"} }
        return result

    def cctvGet(self,data):
        query = f"{data['area']} - {data['wilayah']}"
        infos = data['camera']
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": query.upper(), "weight": "bold", "size": "xs", "wrap": True} ], "paddingBottom": "5px"}, {"type": "separator"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": infos, "size": "xxs", "wrap": True } ], "paddingAll": "10px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px"} }
        return result

    def quotes(self,data):
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [], "width": "15px", "height": "15px", "position": "absolute", "backgroundColor": "#f22424", "cornerRadius": "100px", "offsetTop": "12px", "offsetStart": "15px"}, {"type": "box", "layout": "vertical", "contents": [], "width": "15px", "height": "15px", "position": "absolute", "backgroundColor": "#f4e972", "cornerRadius": "100px", "offsetTop": "12px", "offsetStart": "40px"}, {"type": "box", "layout": "vertical", "contents": [], "width": "15px", "height": "15px", "position": "absolute", "backgroundColor": "#5ef661", "cornerRadius": "100px", "offsetTop": "12px", "offsetStart": "70px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "MOVIE QUOTES", "size": "xxs", "weight": "bold", "color": "#ffffffcc", "decoration": "underline"} ], "position": "absolute", "backgroundColor": "#ffffff44", "cornerRadius": "2.5px", "offsetTop": "10px", "offsetStart": "100px", "width": "150px", "paddingStart": "8px", "paddingEnd": "8px", "height": "20px", "justifyContent": "center"} ], "height": "40px", "backgroundColor": "#212121"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": data, "size": "xxs", "color": "#ffffffcc", "wrap": True } ], "paddingAll": "15px", "backgroundColor": "#ffffff22"} ], "paddingAll": "25px", "backgroundColor": "#000000cc", "paddingBottom": "35px"} ], "backgroundColor": "#ffffff", "paddingAll": "0px"} }
        return result

    def manga(self,data):
        title = data['title']
        pic = data['thumbnail']
        rating = data['rating']
        status = data['status']
        info = f"Author : {data['author']}"
        info += f"\nGenre : {data['genre']}"
        info += f"\nType : {data['type']}"
        info += f"\nRelease : {data['release']}"
        info += f"\nUpdated : {data['updated']}"
        info += f"\n\n{data['updated']}"
        info += "\n\nList Chapter :"
        num = 0;infos = ""
        for i in data["manga"]:
            num += 1
            infos += f"\n{num}. Chapter {i['chapter']}"
        result = [{"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pic, "size": "full", "aspectMode": "cover"} ] }, {"type": "separator", "color": "#000000cc"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"Status : {status}", "size": "xxs", "weight": "bold", "align": "center"} ], "paddingStart": "15px", "paddingEnd": "15px", "paddingTop": "5px", "paddingBottom": "5px"}, {"type": "separator", "color": "#000000cc"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"Rating : {rating}", "size": "xxs", "weight": "bold", "align": "center"} ], "paddingStart": "15px", "paddingEnd": "15px", "paddingTop": "5px", "paddingBottom": "5px"} ] }, {"type": "separator", "color": "#000000cc"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": title, "weight": "bold", "wrap": True }, {"type": "text", "text": info, "wrap": True, "size": "xxs", "margin": "sm"} ], "paddingAll": "15px"} ], "paddingAll": "0px"} },{"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "CHAPTER", "weight": "bold", "size": "lg", "align": "center", "color": "#ff0000"} ], "paddingBottom": "5px"}, {"type": "separator"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": infos[1:], "size": "xxs", "wrap": True } ], "paddingAll": "10px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px"} }]
        return result

    def movie(self,data):
        pic = data["poster"]
        title = f"{data['title']} ({data['year']})"
        review = f"Runtime : {data['runtime']}"
        review += f"\nRelease : {data['release']}"
        review += f"\nDVD Release : {data['dvd']}"
        review += f"\nGenre : {data['genre']}"
        review += f"\nDirector : {data['director']}"
        review += f"\nProduction : {data['production']}\n"
        review += f"\nActors : {data['actors']}\n"
        review += f"\nSynopsis :\n{data['synopsis']}\n"
        review += f"\nAwards : {data['awards']}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": title, "weight": "bold", "align": "center", "color": "#ffffffcc"} ], "paddingAll": "10px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pic, "size": "full", "aspectMode": "cover"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": review, "wrap": True, "size": "xxs", "color": "#ffffffcc"} ], "paddingAll": "20px"} ], "paddingAll": "0px", "backgroundColor": "#212121"} }
        return result

    def cinemaSearch(self,data):
        num = 0
        info = ""
        query = data['city']
        for i in data["data"]:
            num += 1
            info += f"\n{num}. {i['cinema']}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"CINEMA {query.upper()}", "weight": "bold", "size": "lg", "align": "center", "color": "#ff0000"} ], "paddingBottom": "5px"}, {"type": "separator"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": info[1:], "size": "xxs", "color": "#ffffffcc", "weight": "bold", "wrap": True } ], "paddingAll": "5px", "paddingTop": "10px", "paddingBottom": "10px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px", "backgroundColor": "#212121"} }
        return result

    def cinemaInfo(self,data):
        query = data["cinema"]
        pic = data["studioImage"]
        address = data["address"]
        num = 0
        info = ""
        for i in data["nowPlaying"]:
            num += 1
            info += f"\n{num}. {i['movie'].split('(')[0]}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": query.upper(), "weight": "bold", "size": "lg", "align": "center", "color": "#ff0000"}, {"type": "text", "text": address, "size": "xxs", "color": "#ffffffcc", "align": "center", "wrap": True } ], "paddingBottom": "10px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pic, "size": "full", "aspectMode": "cover", "aspectRatio": "2:1.5"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "NOW PLAYING", "color": "#ff0000", "weight": "bold"}, {"type": "text", "text": info[1:], "size": "xxs", "color": "#ffffffcc", "wrap": True } ], "paddingAll": "5px", "paddingTop": "10px", "paddingBottom": "10px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px", "backgroundColor": "#212121"} }
        return result

    def cinemaShow(self,data):
        title = data["movie"]
        pic = data["poster"]
        duration = data["duration"]
        price = data["price"]
        synopsis = data["synopsis"]
        timePlay = ""
        for i in data["showtime"]:
            timePlay += f" , {i}"
        info = f"\nShowtime:\n{timePlay[3:]}"
        info += f"\n\nGenre:\n{data['genre']}"
        info += f"\n\nDirector:\n{data['director']}"
        info += f"\n\nActor:\n{data['actor']}"
        result = {"type": "carousel", "contents": [{"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "NOW PLAYING", "weight": "bold", "align": "center", "size": "lg", "color": "#ff0000"} ], "paddingAll": "10px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pic, "size": "full", "aspectMode": "fit"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": price, "size": "xxs", "weight": "bold", "color": "#ffffff"} ], "backgroundColor": "#900000", "paddingStart": "5px", "paddingEnd": "5px", "paddingTop": "2px", "paddingBottom": "2px", "position": "absolute", "offsetTop": "53px", "offsetStart": "5px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": duration, "size": "xxs", "color": "#ffffff", "weight": "bold"} ], "backgroundColor": "#900000", "paddingStart": "5px", "paddingEnd": "5px", "paddingTop": "2px", "paddingBottom": "2px", "position": "absolute", "offsetTop": "78px", "offsetStart": "5px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": title, "weight": "bold", "wrap": True, "color": "#ffffffcc"}, {"type": "text", "text": info, "wrap": True, "size": "xs", "margin": "xs", "color": "#ffffffcc"} ], "paddingAll": "20px"} ], "paddingAll": "0px"}, "styles": {"body": {"backgroundColor": "#212121"} } },{"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "SYNOPSIS", "weight": "bold", "size": "lg", "align": "center", "color": "#ff0000"} ], "paddingBottom": "5px"}, {"type": "separator"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": synopsis, "color": "#ffffffcc", "size": "xxs", "wrap": True } ], "paddingAll": "15px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "10px", "backgroundColor": "#212121"} }]}
        return result

    def playstore(self,data):
        pic = data["thumbnail"]
        title = data["title"]
        downloads = data["pageUrl"]
        info = f"Developer : {data['developer']}"
        info += f"\n\n{data['developer']}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "weight": "bold", "wrap": True, "text": title } ], "paddingAll": "10px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pic, "size": "full", "aspectMode": "fit"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": info, "wrap": True, "size": "xxs"} ], "paddingAll": "20px", "paddingBottom": "2px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "INSTALL", "weight": "bold", "size": "xs", "color": "#ffffff", "decoration": "underline"} ], "paddingAll": "5px", "paddingStart": "10px", "paddingEnd": "10px", "action": {"type": "uri", "uri": downloads }, "borderWidth": "1px", "borderColor": "#39d135", "backgroundColor": "#05c100"} ], "paddingBottom": "15px", "alignItems": "flex-end", "paddingEnd": "15px"} ], "paddingAll": "0px"} }
        return result

    def topnews(self,data):
        main = []
        for i in range(10):
            title = data[i]["title"]
            pages = data[i]["url"]
            source = data[i]["source"]
            info = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "RENDY TAMPAN", "contents": [{"type": "span", "text": "TOP ", "color": "#ff0000"}, {"type": "span", "text": "NEWS", "color": "#ffffffcc"} ], "weight": "bold", "flex": 1, "gravity": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": source.upper(), "color": "#000000cc", "weight": "bold", "align": "center", "size": "xxs"} ], "backgroundColor": "#ffffff99", "paddingTop": "2px", "paddingBottom": "2px", "paddingStart": "6px", "paddingEnd": "6px", "justifyContent": "center"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "backgroundColor": "#212121"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": title, "size": "sm", "wrap": True } ], "paddingAll": "15px", "paddingBottom": "0px"} ], "paddingAll": "0px"}, "footer": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Selengkapnya", "size": "xxs", "decoration": "underline", "align": "end", "color": "#ffffff", "action": {"type": "uri", "uri": pages }, "weight": "bold"} ], "backgroundColor": "#ff0000", "paddingTop": "2px", "paddingBottom": "2px", "paddingStart": "5px", "paddingEnd": "5px"} ], "paddingAll": "10px", "paddingStart": "15px", "paddingEnd": "15px", "paddingBottom": "15px", "alignItems": "flex-end", "backgroundColor": "#00000011"}, "styles": {"body": {"backgroundColor": "#00000011"} } }
            main.append(info)
        result = {"type": "carousel", "contents": main} 
        return result

    def adzan(self,data):
        waktu = data["tanggal"]
        city = data["wilayah"]
        imsyak = data["adzan"]["imsyak"]
        subuh = data["adzan"]["subuh"]
        terbit = data["adzan"]["terbit"]
        dhuha = data["adzan"]["dhuha"]
        dzuhur = data["adzan"]["dzuhur"]
        ashar = data["adzan"]["ashar"]
        maghrib = data["adzan"]["maghrib"]
        isya = data["adzan"]["isya"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://api.imjustgood.com/img/masjid.jpg", "aspectRatio": "2:1.3", "aspectMode": "cover", "size": "full"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": waktu, "color": "#ffffff", "size": "sm"} ], "position": "absolute", "offsetTop": "10px", "offsetEnd": "10px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": city, "color": "#ffffff", "size": "sm", "wrap": True, "maxLines": 2 } ], "position": "absolute", "offsetTop": "10px", "offsetStart": "10px", "width": "100px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Imsyak", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": imsyak, "size": "sm", "align": "center"} ], "paddingAll": "5px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Subuh", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": subuh, "size": "sm", "align": "center"} ], "paddingAll": "5px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Terbit", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": terbit, "size": "sm", "align": "center"} ], "paddingAll": "5px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Dhuha", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": dhuha, "size": "sm", "align": "center"} ], "paddingAll": "5px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Dzuhur", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": dzuhur, "size": "sm", "align": "center"} ], "paddingAll": "5px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Ashar", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ashar, "size": "sm", "align": "center"} ], "paddingAll": "5px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Maghrib", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": maghrib, "size": "sm", "align": "center"} ], "paddingAll": "5px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Isya", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "justifyContent": "center", "paddingBottom": "7px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": isya, "size": "sm", "align": "center"} ], "paddingAll": "5px"} ] } ], "paddingAll": "0px"} }
        return result

    def cuaca(self,data):
        place = data["location"]
        weather = data["description"]
        temperature = data["temperature"]
        humidity = data["humidity"]
        wind = data["wind"]
        result = {"type": "bubble", "size": "micro", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": place, "size": "sm", "weight": "bold", "wrap": True }, {"type": "separator", "margin": "sm"}, {"type": "text", "text": weather, "size": "xxs", "weight": "bold", "wrap": True, "margin": "sm", "align": "center"}, {"type": "separator", "margin": "sm"} ], "paddingAll": "10px", "paddingTop": "5px", "paddingBottom": "5px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "Temperature", "size": "xxs"}, {"type": "text", "text": temperature, "size": "xxs", "align": "center"} ], "paddingStart": "10px", "paddingEnd": "10px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "Humidity", "size": "xxs"}, {"type": "text", "text": humidity, "size": "xxs", "align": "center"} ], "paddingStart": "10px", "paddingEnd": "10px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "Wind Speed", "size": "xxs"}, {"type": "text", "text": wind, "size": "xxs", "align": "center"} ], "paddingStart": "10px", "paddingEnd": "10px"} ], "paddingBottom": "8px", "paddingStart": "5px", "paddingEnd": "5px"} ], "paddingAll": "0px"} }
        return result

    def bmkg(self,data):
        tanggal = data["tanggal"]
        pukul = data["pukul"]
        kekuatan = data["kekuatan"]
        kordinat = data["kordinat"]
        kedalaman = data["kedalaman"]
        lokasi = data["lokasi"]
        wilayah = data["wilayah"]
        arahan = data["arahan"]
        saran = data["saran"]
        shakemap = f"{self.pushMsg}?type=foimage&img={data['skema']}&label={self.branding}&act={self.brandingURL}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "RENDYTR ITU MANTAP", "color": "#ff0000", "weight": "bold", "contents": [{"type": "span", "text": "INFO GEMPA ", "color": "#000000cc"}, {"type": "span", "text": "BMKG"} ], "align": "center"} ], "paddingAll": "10px", "backgroundColor": "#00000033"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Tanggal", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "width": "100px", "justifyContent": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": tanggal, "size": "sm", "color": "#ff0000"} ], "paddingAll": "10px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Pukul", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "width": "100px", "justifyContent": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": pukul, "size": "sm", "color": "#ff0000"} ], "paddingAll": "10px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Kekuatan", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "width": "100px", "justifyContent": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": kekuatan, "size": "sm", "color": "#ff0000"} ], "paddingAll": "10px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Kordinat", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "width": "100px", "justifyContent": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": kordinat, "size": "sm", "color": "#ff0000"} ], "paddingAll": "10px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Kedalaman", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "width": "100px", "justifyContent": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": kedalaman, "size": "sm", "color": "#ff0000"} ], "paddingAll": "10px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Lokasi", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "width": "100px", "justifyContent": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": lokasi, "size": "xxs", "color": "#ff0000", "wrap": True } ], "paddingAll": "10px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Wilayah", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "width": "100px", "justifyContent": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": wilayah, "size": "xxs", "color": "#ff0000", "wrap": True } ], "paddingAll": "10px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Arahan", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "justifyContent": "center", "paddingBottom": "7px", "width": "100px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": arahan, "size": "xxs", "color": "#ff0000", "wrap": True } ], "paddingAll": "10px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Saran", "size": "sm"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "justifyContent": "center", "paddingBottom": "7px", "width": "100px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": saran, "size": "xxs", "color": "#ff0000", "wrap": True } ], "paddingAll": "10px"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "SHAKEMAP", "color": "#ffffff", "size": "sm", "decoration": "underline", "align": "center", "weight": "bold"} ], "backgroundColor": "#900000", "paddingAll": "10px"} ], "paddingAll": "10px", "backgroundColor": "#00000033", "action": {"type": "uri", "uri": shakemap } } ], "paddingAll": "0px"} }
        return result

    def corona(self,data):
        case1 = data["world"]["case"]
        rip1 = data["world"]["rip"]
        fit1 = data["world"]["fit"]
        case2 = data["indonesia"]["case"]
        rip2 = data["indonesia"]["rip"]
        fit2 = data["indonesia"]["fit"]
        result = {"type": "bubble", "size": "micro", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "COVID-19", "size": "sm", "weight": "bold", "contents": [{"type": "span", "text": "INFO "}, {"type": "span", "text": "COVID-19", "color": "#ff0000"} ] }, {"type": "separator", "margin": "sm"}, {"type": "text", "text": "WORLD", "size": "xxs", "weight": "bold", "margin": "sm", "align": "center"}, {"type": "separator", "margin": "sm"} ], "paddingAll": "10px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "Case", "size": "xxs"}, {"type": "text", "text": case1, "size": "xxs", "color": "#ffba00", "flex": 2} ], "paddingStart": "10px", "paddingEnd": "10px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "RIP", "size": "xxs"}, {"type": "text", "text": rip1, "size": "xxs", "color": "#ff0000", "flex": 2} ], "paddingStart": "10px", "paddingEnd": "10px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "FIT", "size": "xxs"}, {"type": "text", "text": fit1, "size": "xxs", "color": "#13ca06", "flex": 2} ], "paddingStart": "10px", "paddingEnd": "10px"} ], "paddingBottom": "5px", "paddingStart": "5px", "paddingEnd": "5px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "separator", "margin": "sm"}, {"type": "text", "text": "INDONESIA", "size": "xxs", "weight": "bold", "margin": "sm", "align": "center"}, {"type": "separator", "margin": "sm"} ], "paddingTop": "0px", "paddingBottom": "5px", "paddingAll": "10px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "Case", "size": "xxs"}, {"type": "text", "text": case2, "size": "xxs", "color": "#ffba00", "flex": 2} ], "paddingStart": "10px", "paddingEnd": "10px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "RIP", "size": "xxs"}, {"type": "text", "text": rip2, "size": "xxs", "color": "#ff0000", "flex": 2} ], "paddingStart": "10px", "paddingEnd": "10px"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "text", "text": "FIT", "size": "xxs"}, {"type": "text", "text": fit2, "size": "xxs", "color": "#13ca06", "flex": 2} ], "paddingStart": "10px", "paddingEnd": "10px"} ], "paddingBottom": "10px", "paddingStart": "5px", "paddingEnd": "5px"} ], "paddingAll": "0px"} }
        return result

    def karir(self,data):
        info,num = "",0
        for i in data:
            num += 1
            info += f"\n{num}. {i['perusahaan'].split('(')[0]}"
        info = info[1:]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "INFO KARIR", "weight": "bold", "contents": [{"type": "span", "text": "INFO "}, {"type": "span", "text": "KARIR", "color": "#ff0000"} ], "align": "center"}, {"type": "separator", "margin": "md", "color": "#00000022"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": info, "size": "xxs", "margin": "md", "wrap": True } ], "paddingAll": "10px"} ] } }
        return result

    def karirInfo(self,data):
        perusahaan = data["perusahaan"]
        lokasi = data["lokasi"]
        sumber = data["sumber"]
        info = f"Gaji : {data['gaji']}"
        info += f"\n\nProfesi :\n{data['profesi']}"
        info += f"\n\nBagian :\n{data['bagian']}"
        info += f"\n\nJabatan :\n{data['jabatan']}"
        info += f"\n\nPendidikan :\n{data['pendidikan']}"
        info += f"\n\nPengalaman :\n{data['pengalaman']}"
        info += f"\n\nSyarat :\n{data['syarat']}"
        info += f"\n\nDeskripsi :\n{data['deskripsi']}"
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": perusahaan, "weight": "bold", "wrap": True }, {"type": "text", "text": lokasi, "size": "xxs", "wrap": True }, {"type": "separator", "margin": "md", "color": "#00000022"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": info, "size": "xxs", "margin": "md", "wrap": True } ], "paddingAll": "10px"}, {"type": "separator", "margin": "md", "color": "#00000022"}, {"type": "text", "text": "SUMBER", "margin": "md", "align": "end", "decoration": "underline", "size": "xxs", "color": "#0000ff", "action": {"type": "uri", "uri": sumber } } ] } }
        return result

    def cellularSearch(self,data):
        info,num = "",0
        for i in data:
            num += 1
            info += f"\n{num}. {i['brands']}"
        info = info[1:]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "RESULT", "weight": "bold", "contents": [{"type": "span", "text": "INFO "}, {"type": "span", "text": "CELLULAR", "color": "#ff0000"} ], "align": "center"}, {"type": "separator", "margin": "md", "color": "#00000022"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": info, "size": "xxs", "margin": "md", "wrap": True } ], "paddingAll": "10px"} ] } }
        return result

    def cellularSpecs(self,data):
        pic = data["thumbnail"]
        merk = data["brands"]
        source = data["pageUrl"]
        info = "\nRelease : {}".format(data["release"])
        info += "\nRam : {}".format(data["ram"])
        info += "\nStorage : {}".format(data["storage"])
        info += "\nChipset : {}".format(data["chipset"])
        info += "\nBattery : {}".format(data["battery"])
        info += "\nDisplay : {}".format(data["display"])
        info += "\nScreen : {}".format(data["screen"])
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": merk, "weight": "bold"} ], "paddingAll": "10px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": pic, "size": "full", "aspectMode": "fit", "aspectRatio": "1:1"} ] }, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": info, "wrap": True, "size": "xxs"} ], "paddingAll": "10px"}, {"type": "separator", "color": "#00000022"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Selengkapnya", "align": "end", "decoration": "underline", "size": "xs", "color": "#0000ff", "action": {"type": "uri", "uri": source }, "weight": "bold"} ], "paddingAll": "10px"} ], "paddingAll": "0px"} }
        return result

    def lahir(self,data):
        lahirs = data["lahir"]
        zodiak = data["zodiak"]
        hari = data["hari"]
        ultah = data["ultah"]
        usia = data["usia"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "RENDYTR ITU MANTAP", "color": "#ff0000", "weight": "bold", "contents": [{"type": "span", "text": lahirs, "color": "#000000"} ], "align": "center"} ], "paddingAll": "10px", "backgroundColor": "#00000033"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Zodiak", "size": "sm", "weight": "bold"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "width": "100px", "justifyContent": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": zodiak, "size": "sm"} ], "paddingAll": "10px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Hari", "size": "sm", "weight": "bold"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "width": "100px", "justifyContent": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": hari, "size": "sm"} ], "paddingAll": "10px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Ultah", "size": "sm", "weight": "bold"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "width": "100px", "justifyContent": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ultah, "size": "sm"} ], "paddingAll": "10px"} ] }, {"type": "separator", "color": "#00000055"}, {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "Usia", "size": "sm", "weight": "bold"} ], "paddingAll": "5px", "backgroundColor": "#00000022", "paddingStart": "15px", "width": "100px", "justifyContent": "center"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": usia, "size": "sm", "wrap": True } ], "paddingAll": "10px"} ] } ], "paddingAll": "0px"} }
        return result

    def jadian(self,data):
        title = data["date"]
        deskripsi = data["description"]
        karakter = data["related"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "The Autobots Corp", "weight": "bold", "wrap": True, "contents": [{"type": "span", "text": title.upper(), "color": "#ffff00"} ], "color": "#ffffff"} ], "paddingAll": "10px", "paddingStart": "20px", "paddingEnd": "20px", "backgroundColor": "#00000077"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "JUSTGOOD", "wrap": True, "size": "xxs", "contents": [{"type": "span", "text": "KARAKTER : ", "weight": "bold"}, {"type": "span", "text": karakter } ], "color": "#ffffffcc"}, {"type": "text", "text": "JUSTGOOD", "wrap": True, "size": "xxs", "contents": [{"type": "span", "text": "DESKRIPSI : ", "weight": "bold"}, {"type": "span", "text": deskripsi } ], "margin": "xl", "color": "#ffffffcc"} ], "paddingAll": "15px", "paddingStart": "20px", "paddingEnd": "20px"} ], "paddingAll": "0px", "paddingBottom": "10px", "backgroundColor": "#ff006c"} }
        return result

    def nama(self,data):
        query = data["name"]
        karakter = data["definition"]
        deskripsi = data["description"]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "The Autobots Corp", "weight": "bold", "wrap": True, "contents": [{"type": "span", "text": "ARTI NAMA "}, {"type": "span", "text": query.upper(), "color": "#ff0000"} ], "color": "#ffffffcc"} ], "paddingAll": "10px", "backgroundColor": "#00000044", "paddingStart": "20px", "paddingEnd": "20px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "JUSTGOOD", "wrap": True, "size": "xxs", "contents": [{"type": "span", "text": "KARAKTER : ", "weight": "bold"}, {"type": "span", "text": karakter } ], "color": "#ffffffcc"}, {"type": "text", "text": "JUSTGOOD", "wrap": True, "size": "xxs", "contents": [{"type": "span", "text": "DESKRIPSI : ", "weight": "bold"}, {"type": "span", "text": deskripsi } ], "margin": "xl", "color": "#ffffffcc"} ], "paddingAll": "15px", "paddingStart": "20px", "paddingEnd": "20px"} ], "paddingAll": "0px", "paddingBottom": "10px", "backgroundColor": "#000000aa"} }
        return result

    def mimpi(self,data,query):
        info = ""
        for a in data:
            info += f"\n{a['dream'].upper()}"
            info += f"\n{a['meaning'].lower()}\n"
        info = info[1:]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "The Autobots Corp", "weight": "bold", "wrap": True, "contents": [{"type": "span", "text": "ARTI MIMPI "}, {"type": "span", "text": query.upper(), "color": "#ffff00"} ], "color": "#ffffff"} ], "paddingAll": "10px", "backgroundColor": "#00000044", "paddingStart": "20px", "paddingEnd": "20px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "RESULT", "wrap": True, "size": "xxs", "contents": [{"type": "span", "text": info } ], "color": "#ffffffcc"} ], "paddingAll": "15px", "paddingStart": "20px", "paddingEnd": "20px"} ], "paddingAll": "0px", "paddingBottom": "10px", "backgroundColor": "#0000ffaa"} }
        return result

    def acaratv(self,data):
        info = ""
        for a in data:
            for b in a:
                info += f"\n\n{b.upper()}"
                for c in a[b]:
                    info += f"\n{c}"
        info = info[2:]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "The Autobots Corp", "weight": "bold", "contents": [{"type": "span", "text": "ACARA TV"} ], "color": "#000000"} ], "paddingAll": "10px", "paddingStart": "20px", "paddingEnd": "20px", "backgroundColor": "#00000077"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "justgood", "wrap": True, "size": "xxs", "contents": [{"type": "span", "text": info } ]} ], "paddingAll": "15px", "paddingStart": "20px", "paddingEnd": "20px"} ], "paddingAll": "0px", "paddingBottom": "10px", "backgroundColor": "#00000044"} }
        return result

    def channel(self,data,channel):
        info = ""
        for a in data:
            info += f"\n{a}"
        info = info[1:]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "The Autobots Corp", "weight": "bold", "wrap": True, "contents": [{"type": "span", "text": "ACARA "}, {"type": "span", "text": channel.upper(), "color": "#ff0000"} ], "color": "#ffffffcc"} ], "paddingAll": "10px", "paddingStart": "20px", "paddingEnd": "20px", "backgroundColor": "#00000077"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "JUSTGOOD", "wrap": True, "size": "xxs", "contents": [{"type": "span", "text": info } ], "color": "#ffffffcc"} ], "paddingAll": "15px", "paddingStart": "20px", "paddingEnd": "20px"} ], "paddingAll": "0px", "paddingBottom": "10px", "backgroundColor": "#000000aa"} }
        return result

    def resi(self,data):
        courier = data['courier']
        info = "Resi : {}".format(data["code"])
        info += "\nStatus : {}".format(data["status"])
        info += "\nJenis : {}".format(data["service"])
        info += "\nBerat : {}".format(data["weight"])
        info += "\nHarga : {}".format(data["price"])
        info += "\nPukul : {}".format(data["time"])
        info += "\nTanggal : {}".format(data["date"])
        info += "\n\nDeskripsi :\n{}".format(data["desc"])
        info += "\n\nPengirim :\n{} - {}".format(data["sender"]["name"],data["sender"]["city"])
        info += "\n\nPenerima :\n{} - {}".format(data["receiver"]["name"],data["receiver"]["city"])
        if data["timeExpress"] != []:
           info += "\n\n{}".format(data["timeExpress"][0]["desc"].replace("[","").replace("]","").replace(" | ","\n"))
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "The Autobots Corp", "weight": "bold", "wrap": True, "contents": [{"type": "span", "text": courier.upper() } ], "color": "#ffffff"} ], "paddingAll": "10px", "paddingStart": "20px", "paddingEnd": "20px", "backgroundColor": "#00000077"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "JUSTGOOD", "wrap": True, "size": "xxs", "contents": [{"type": "span", "text": info } ], "color": "#000000"} ], "paddingAll": "15px", "paddingStart": "20px", "paddingEnd": "20px", "backgroundColor": "#ffffffaa"} ], "paddingAll": "0px", "backgroundColor": "#ff0000", "borderWidth": "10px", "borderColor": "#850000"} }
        return result

    def checkIP(self,data):
        address = data["ip_address"]
        info = ""
        for a in data:
            if a != "ip_address" and a != "languages" and data[a] is not None:
               info += "\n{} : {}".format(a.upper(),data[a])
        info = info[1:]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "The Autobots Corp", "weight": "bold", "wrap": True, "contents": [{"type": "span", "text": address } ], "color": "#ffffff"} ], "paddingAll": "10px", "paddingStart": "20px", "paddingEnd": "20px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "JUSTGOOD", "wrap": True, "size": "xxs", "contents": [{"type": "span", "text": info } ], "color": "#000000"} ], "paddingAll": "15px", "paddingStart": "20px", "paddingEnd": "20px", "backgroundColor": "#ffffffaa"} ], "paddingAll": "0px", "backgroundColor": "#ff5500", "borderWidth": "10px", "borderColor": "#ff5500"} }
        return result

    def linever(self,data):
        info = ""
        for a in data:
            info += "\n{} ( {} )".format(a.upper(),data[a])
        info = info[1:]
        result = {"type": "bubble", "size": "kilo", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "The Autobots Corp", "weight": "bold", "wrap": True, "contents": [{"type": "span", "text": "LINE VERSION"} ], "color": "#ffffff"} ], "paddingBottom": "5px", "paddingStart": "5px", "paddingEnd": "5px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "JUSTGOOD", "wrap": True, "size": "xxs", "contents": [{"type": "span", "text": info } ], "color": "#000000"} ], "paddingAll": "15px", "paddingStart": "20px", "paddingEnd": "20px", "backgroundColor": "#ffffff"} ], "paddingAll": "0px", "backgroundColor": "#2cc237", "borderWidth": "10px", "borderColor": "#2cc237"} }
        return result
