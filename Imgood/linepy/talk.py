# -*- coding: utf-8 -*-
from akad.ttypes import Message
from random import randint
from Liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
import json, ntpath, requests,time,random

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin

class Talk(object):
    isLogin = False
    _messageReq = {}
    _unsendMessageReq = 0

    def __init__(self):
        self.isLogin = True
        self.wm = json.loads(open('Data/settings.json','r').read())
    """User"""

    @loggedIn
    def acquireEncryptedAccessToken(self, featureType=2):
        return self.talk.acquireEncryptedAccessToken(featureType)

    @loggedIn
    def getProfile(self):
        return self.talk.getProfile()

    @loggedIn
    def getSettings(self):
        return self.talk.getSettings()

    @loggedIn
    def getUserTicket(self):
        return self.talk.getUserTicket()

    @loggedIn
    def updateProfile(self, profileObject):
        return self.talk.updateProfile(0, profileObject)

    @loggedIn
    def updateSettings(self, settingObject):
        return self.talk.updateSettings(0, settingObject)

    @loggedIn
    def updateProfileAttribute(self, attrId, value):
        return self.talk.updateProfileAttribute(0, attrId, value)

    """Operation"""

    @loggedIn
    def fetchOperation(self, revision, count):
        return self.talk.fetchOperations(revision, count)

    @loggedIn
    def getLastOpRevision(self):
        return self.talk.getLastOpRevision()

    """Message"""
    @loggedIn
    def runtime(sef,secs):
       mins, secs = divmod(secs,60)
       hours, mins = divmod(mins,60)
       return '%02d Hours %02d Minute %02d Secs' % (hours, mins, secs)


    @loggedIn
    def gbirth(self,id,to):
        date = "%d-%m-%Y"
        timer = "%H:%M:%S"
        datecrt = time.strftime("User:\n@! it, \nGroup created:\n  • Date:{}\n  • Time:{}".format(str(date),timer), time.localtime(int(self.talk.getGroup(to).createdTime) / 1000))
        return self.sendReplyMention(id,to,datecrt,"",[self.talk.getProfile().mid])

    @loggedIn
    def me(self,to):
        user = self.talk.getProfile().mid
        profile = self.talk.getContact(user)
        data ={"type":"bubble","size":"kilo","body":{"type":"box","layout":"vertical","contents":[{"type":"image","url":"https://obs.line-scdn.net/{}".format(profile.pictureStatus),"size":"full","aspectRatio":"1:1","aspectMode":"cover","action":{"type":"uri","uri":"https://obs.line-scdn.net/{}".format(profile.pictureStatus)}},{"type":"box","layout":"vertical","contents":[{"type":"text","text":"PROFILE","size":"xxs","color":"#ff0000"}],"position":"absolute","borderWidth":"1px","borderColor":"#ff0000","paddingStart":"5px","paddingEnd":"5px","paddingTop":"1px","paddingBottom":"1px","cornerRadius":"5px","offsetTop":"5px","offsetStart":"5px","backgroundColor":"#00000011"},{"type":"box","layout":"vertical","contents":[{"type":"text","text":"{}".format(profile.displayName),"weight":"bold","wrap":True,"color":"#ffffffcc"},{"type":"text","text":"{}".format(profile.statusMessage),"wrap":True,"size":"xxs","margin":"sm","color":"#ffffffcc"}],"paddingTop":"5px","paddingEnd":"10px","paddingStart":"10px"}],"paddingAll":"0px","paddingBottom":"13px","backgroundColor":"#000000"}}
        self.sendFlex(to,data)

    @loggedIn
    def help(self,to,label,menu):
        user = self.talk.getProfile().mid
        profile = self.talk.getContact(user)
        data ={"type":"bubble","size":"kilo","body":{"type":"box","layout":"vertical","backgroundColor": "#000000","contents":[{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"vertical","contents":[{"type":"image","url":"https://obs.line-scdn.net/{}".format(profile.pictureStatus),"aspectRatio":"1:1","aspectMode":"cover"}],"cornerRadius":"100px"}],"alignItems":"center","paddingTop":"50px"},{"type":"box","layout":"vertical","contents":[{"type":"text","text":"{}".format(profile.displayName),"color":"#FFC300","weight":"bold","align":"center"},{"type":"text","text":"Tetaplah mesum","color":"#FFC300cc","align":"center","size":"xxs"}],"paddingAll":"10px"},{"type":"box","layout":"vertical","contents":[{"type":"text","text":label.upper(),"color":"#FFC300","weight":"bold","size":"xxs"}],"position":"absolute","borderWidth":"1px","borderColor":"#ffffffcc","paddingStart":"8px","paddingEnd":"8px","paddingTop":"5px","paddingBottom":"5px","offsetTop":"10px","offsetStart":"10px","cornerRadius":"20px"},{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"vertical","contents":[{"type":"text","text":menu,"color":"#FFC300","size":"xs","wrap":True}],"paddingAll":"20px","backgroundColor":"#111111"}],"paddingAll":"20px","paddingTop":"5px"}],"paddingAll":"0px"},"styles":{"body":{"backgroundColor":"#161e2b"}}}
        self.sendFlex(to,data)

    @loggedIn
    def center(self,to,label,menu):
        user = self.talk.getProfile().mid
        profile = self.talk.getContact(user)
        data ={"type":"bubble","size":"kilo","body":{"type":"box","layout":"vertical","backgroundColor":"#000000","contents":[{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"vertical","contents":[{"type":"image","url":"https://obs.line-scdn.net/{}".format(profile.pictureStatus),"aspectRatio":"1:1","aspectMode":"cover"}],"cornerRadius":"100px"}],"alignItems":"center","paddingTop":"50px"},{"type":"box","layout":"vertical","contents":[{"type":"text","text":"{}".format(profile.displayName),"color":"#FFC300","weight":"bold","align":"center"},{"type":"text","text":"Tetaplah mesum","color":"#FFC300cc","align":"center","size":"xxs"}],"paddingAll":"10px"},{"type":"box","layout":"vertical","contents":[{"type":"text","text":label.upper(),"color":"#FFC300","weight":"bold","size":"xxs"}],"position":"absolute","borderWidth":"1px","borderColor":"#ffffffcc","paddingStart":"8px","paddingEnd":"8px","paddingTop":"5px","paddingBottom":"5px","offsetTop":"10px","offsetStart":"10px","cornerRadius":"20px"},{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"vertical","contents":[{"type":"text","text":menu,"color":"#FFC300","size":"xs","wrap":True,"align":"center"}],"paddingAll":"20px","backgroundColor":"#111111"}],"paddingAll":"20px","paddingTop":"5px"}],"paddingAll":"0px"},"styles":{"body":{"backgroundColor":"#161e2b"}}}
        self.sendFlex(to,data)


    @loggedIn
    def sendMessage(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)

    @loggedIn
    def generateReplyMessage(self, relatedMessageId):
        msg = Message()
        msg.relatedMessageServiceCode = 1
        msg.messageRelationType = 3
        msg.relatedMessageId = str(relatedMessageId)
        return msg

    @loggedIn
    def sendReplyMessage(self, relatedMessageId, to, text, contentMetadata={}, contentType=0):
        msg = self.generateReplyMessage(relatedMessageId)
        msg.to = to
        msg.text = text
        msg.contentType = contentType
        msg.contentMetadata = contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)
    
    """ Usage:
        @to Integer
        @text String
        @dataMid List of user Mid
    """
    @loggedIn
    def sendMessageWithMention(self, to, text='', dataMid=[]):
        arr = []
        list_text=''
        if '[list]' in text.lower():
            i=0
            for l in dataMid:
                list_text+='\n@[list-'+str(i)+']'
                i=i+1
            text=text.replace('[list]', list_text)
        elif '[list-' in text.lower():
            text=text
        else:
            i=0
            for l in dataMid:
                list_text+=' @[list-'+str(i)+']'
                i=i+1
            text=text+list_text
        i=0
        for l in dataMid:
            mid=l
            name='@[list-'+str(i)+']'
            ln_text=text.replace('\n',' ')
            if ln_text.find(name):
                line_s=int(ln_text.index(name))
                line_e=(int(line_s)+int(len(name)))
            arrData={'S': str(line_s), 'E': str(line_e), 'M': mid}
            arr.append(arrData)
            i=i+1
        contentMetadata={'MENTION':str('{"MENTIONEES":' + json.dumps(arr).replace(' ','') + '}')}
        return self.sendMessage(to, text, contentMetadata)

    @loggedIn
    def sendFlex(self, to, data):
        xyz = LiffChatContext(to)
        xyzz = LiffContext(chat=xyz)
        view = LiffViewRequest('1602876096-e9QWgjyo', xyzz)
        token = self.liff.issueLiffView(view)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [{
                'type': 'flex',
                'altText': 'IMJUSTGOOD HERE.',
                'contents': data
            }]
        }
        return requests.post(url, headers=headers, data=json.dumps(data))

    @loggedIn
    def sendFlexText(self, to, text):
        main = ["dark","red","cyan","yellow","green","white"]
        color = random.choice(main)
        xyz = LiffChatContext(to)
        xyzz = LiffContext(chat=xyz)
        view = LiffViewRequest('1602876096-e9QWgjyo', xyzz)
        token = self.liff.issueLiffView(view)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [{
                'type': 'text',
                'text': text,
                'sentBy': {
                    'label': 'IMJUSTGOOD.COM',
                    'iconUrl': f'https://imjustgood.com/img/{color}-logo.png',
                    'linkUrl': 'https://{}'.format(self.crawl(self.wm["justGood"]))
                }
            }]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res

    @loggedIn
    def sendFlexImage(self, to, imageUrl, animated=False):
        main = ["dark","red","cyan","yellow","green","white"]
        color = random.choice(main)
        xyz = LiffChatContext(to)
        xyzz = LiffContext(chat=xyz)
        view = LiffViewRequest('1602876096-e9QWgjyo', xyzz)
        token = self.liff.issueLiffView(view)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [{
                'type': 'image',
                'originalContentUrl': imageUrl,
                'previewImageUrl': imageUrl,
                'animated': animated,
                'extension': 'jpg',
                'sentBy': {
                    'label': 'IMJUSTGOOD.COM',
                    'iconUrl': f'https://imjustgood.com/img/{color}-logo.png',
                    'linkUrl': 'https://{}'.format(self.crawl(self.wm["justGood"]))
                }
            }]
        }
        return requests.post(url, headers=headers, data=json.dumps(data))

    @loggedIn
    def sendFlexAudio(self, to, link):
        xyz = LiffChatContext(to)
        xyzz = LiffContext(chat=xyz)
        view = LiffViewRequest('1602876096-e9QWgjyo', xyzz)
        token = self.liff.issueLiffView(view)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [{
                'type': 'audio',
                'originalContentUrl': link,
                'duration': 250000
            }]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res

    @loggedIn
    def sendFlexVideo(self, to, videoUrl, thumbnail='dark'):
        main = ["dark","red","cyan","yellow","green","white"]
        if thumbnail in main:
           thumbnail = f"https://imjustgood.com/img/{thumbnail}-logo.png"
        xyz = LiffChatContext(to)
        xyzz = LiffContext(chat=xyz)
        view = LiffViewRequest('1602876096-e9QWgjyo', xyzz)
        token = self.liff.issueLiffView(view)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [{
                'type': 'video',
                'originalContentUrl': videoUrl,
                'previewImageUrl': thumbnail,
            }]
        }
        return requests.post(url, headers=headers, data=json.dumps(data))

    @loggedIn
    def sendFleximg(self, to, image):
       xGx = {"type":"image","originalContentUrl":"{}".format(image),"previewImageUrl":"{}".format(image),"animated":True,"extension":"jpg","sentBy":{"label": "Im Just Good","iconUrl":"{}".format(self.wm["notMast"]),"linkUrl":"https://{}".format(self.crawl(self.wm["justGood"]))}}
       self.sendFlex(to,xGx)

    @loggedIn
    def crawl(self,query):
      if query == "YXBpLmltanVzdGdvb2QuY29t":
          url = "https://api.imjustgood.com/base64/code?q={}".format(query)
          head = {"User-Agent":"JustGood/0.5"}
          data = json.loads(requests.get(url,headers=head).text)
          return data["result"]

    @loggedIn
    def sendSticker(self, to, packageId, stickerId):
        contentMetadata = {
            'STKVER': '100',
            'STKPKGID': packageId,
            'STKID': stickerId
        }
        return self.sendMessage(to, '', contentMetadata, 7)
        
    @loggedIn
    def sendContact(self, to, mid):
        contentMetadata = {'mid': mid}
        return self.sendMessage(to, '', contentMetadata, 13)

    @loggedIn
    def sendPage(self, to):
        contentMetadata = {'mid': 'ue3844e0062802b4c6421c286c8a640d7'}
        return self.sendMessage(to, '', contentMetadata, 13)

    @loggedIn
    def sendGift(self, to, productId, productType):
        if productType not in ['theme','sticker']:
            raise Exception('Invalid productType value')
        contentMetadata = {
            'MSGTPL': str(randint(0, 12)),
            'PRDTYPE': productType.upper(),
            'STKPKGID' if productType == 'sticker' else 'PRDID': productId
        }
        return self.sendMessage(to, '', contentMetadata, 9)

    @loggedIn
    def sendMessageAwaitCommit(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessageAwaitCommit(self._messageReq[to], msg)

    @loggedIn
    def getRecentMessagesV2(self, chatId, count=50):
        return self.talk.getRecentMessagesV2(chatId,count)

    @loggedIn
    def unsendMessage(self, messageId):
        self._unsendMessageReq += 1
        return self.talk.unsendMessage(self._unsendMessageReq, messageId)

    @loggedIn
    def requestResendMessage(self, senderMid, messageId):
        return self.talk.requestResendMessage(0, senderMid, messageId)

    @loggedIn
    def respondResendMessage(self, receiverMid, originalMessageId, resendMessage, errorCode):
        return self.talk.respondResendMessage(0, receiverMid, originalMessageId, resendMessage, errorCode)

    @loggedIn
    def removeMessage(self, messageId):
        return self.talk.removeMessage(messageId)
    
    @loggedIn
    def removeAllMessages(self, lastMessageId):
        return self.talk.removeAllMessages(0, lastMessageId)

    @loggedIn
    def removeMessageFromMyHome(self, messageId):
        return self.talk.removeMessageFromMyHome(messageId)

    @loggedIn
    def destroyMessage(self, chatId, messageId):
        return self.talk.destroyMessage(0, chatId, messageId, sessionId)
    
    @loggedIn
    def sendChatChecked(self, consumer, messageId):
        return self.talk.sendChatChecked(0, consumer, messageId)

    @loggedIn
    def sendEvent(self, messageObject):
        return self.talk.sendEvent(0, messageObject)

    @loggedIn
    def getLastReadMessageIds(self, chatId):
        return self.talk.getLastReadMessageIds(0, chatId)

    @loggedIn
    def getPreviousMessagesV2WithReadCount(self, messageBoxId, endMessageId, messagesCount=50):
        return self.talk.getPreviousMessagesV2WithReadCount(messageBoxId, endMessageId, messagesCount)

    """Object"""

    @loggedIn
    def sendImage(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 1).id
        return self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=objectId)

    @loggedIn
    def sendImageWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendImage(to, path)

    @loggedIn
    def sendGIF(self, to, path):
        return self.uploadObjTalk(path=path, type='gif', returnAs='bool', to=to)

    @loggedIn
    def sendGIFWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendGIF(to, path)

    @loggedIn
    def sendVideo(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'VIDLEN': '60000','DURATION': '60000'}, contentType = 2).id
        return self.uploadObjTalk(path=path, type='video', returnAs='bool', objId=objectId)

    @loggedIn
    def sendVideoWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendVideo(to, path)

    @loggedIn
    def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        return self.uploadObjTalk(path=path, type='audio', returnAs='bool', objId=objectId)

    @loggedIn
    def sendAudioWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendAudio(to, path)

    @loggedIn
    def sendFile(self, to, path, file_name=''):
        if file_name == '':
            file_name = ntpath.basename(path)
        file_size = len(open(path, 'rb').read())
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'FILE_NAME': str(file_name),'FILE_SIZE': str(file_size)}, contentType = 14).id
        return self.uploadObjTalk(path=path, type='file', returnAs='bool', objId=objectId)

    @loggedIn
    def sendFileWithURL(self, to, url, fileName=''):
        path = self.downloadFileURL(url, 'path')
        return self.sendFile(to, path, fileName)

    """Contact"""
        
    @loggedIn
    def blockContact(self, mid):
        return self.talk.blockContact(0, mid)

    @loggedIn
    def unblockContact(self, mid):
        return self.talk.unblockContact(0, mid)

    @loggedIn
    def findAndAddContactByMetaTag(self, userid, reference):
        return self.talk.findAndAddContactByMetaTag(0, userid, reference)

    @loggedIn
    def findAndAddContactsByMid(self, mid):
        return self.talk.findAndAddContactsByMid(0, mid, 0, '')

    @loggedIn
    def findAndAddContactsByEmail(self, emails=[]):
        return self.talk.findAndAddContactsByEmail(0, emails)

    @loggedIn
    def findAndAddContactsByUserid(self, userid):
        return self.talk.findAndAddContactsByUserid(0, userid)

    @loggedIn
    def findContactsByUserid(self, userid):
        return self.talk.findContactByUserid(userid)

    @loggedIn
    def findContactByTicket(self, ticketId):
        return self.talk.findContactByUserTicket(ticketId)

    @loggedIn
    def getAllContactIds(self):
        return self.talk.getAllContactIds()

    @loggedIn
    def getBlockedContactIds(self):
        return self.talk.getBlockedContactIds()

    @loggedIn
    def getContact(self, mid):
        return self.talk.getContact(mid)

    @loggedIn
    def getContacts(self, midlist):
        return self.talk.getContacts(midlist)

    @loggedIn
    def getFavoriteMids(self):
        return self.talk.getFavoriteMids()

    @loggedIn
    def getHiddenContactMids(self):
        return self.talk.getHiddenContactMids()

    @loggedIn
    def tryFriendRequest(self, midOrEMid, friendRequestParams, method=1):
        return self.talk.tryFriendRequest(midOrEMid, method, friendRequestParams)

    @loggedIn
    def makeUserAddMyselfAsContact(self, contactOwnerMid):
        return self.talk.makeUserAddMyselfAsContact(contactOwnerMid)

    @loggedIn
    def getContactWithFriendRequestStatus(self, id):
        return self.talk.getContactWithFriendRequestStatus(id)

    @loggedIn
    def reissueUserTicket(self, expirationTime=100, maxUseCount=100):
        return self.talk.reissueUserTicket(expirationTime, maxUseCount)
    
    @loggedIn
    def cloneContactProfile(self, mid):
        contact = self.getContact(mid)
        profile = self.profile
        profile.displayName = contact.displayName
        profile.statusMessage = contact.statusMessage
        profile.pictureStatus = contact.pictureStatus
        if self.getProfileCoverId(mid) is not None:
            self.updateProfileCoverById(self.getProfileCoverId(mid))
        self.updateProfileAttribute(8, profile.pictureStatus)
        return self.updateProfile(profile)

    """Group"""

    @loggedIn
    def getChatRoomAnnouncementsBulk(self, chatRoomMids):
        return self.talk.getChatRoomAnnouncementsBulk(chatRoomMids)

    @loggedIn
    def getChatRoomAnnouncements(self, chatRoomMid):
        return self.talk.getChatRoomAnnouncements(chatRoomMid)

    @loggedIn
    def createChatRoomAnnouncement(self, chatRoomMid, type, contents):
        return self.talk.createChatRoomAnnouncement(0, chatRoomMid, type, contents)

    @loggedIn
    def removeChatRoomAnnouncement(self, chatRoomMid, announcementSeq):
        return self.talk.removeChatRoomAnnouncement(0, chatRoomMid, announcementSeq)

    @loggedIn
    def getGroupWithoutMembers(self, groupId):
        return self.talk.getGroupWithoutMembers(groupId)
    
    @loggedIn
    def findGroupByTicket(self, ticketId):
        return self.talk.findGroupByTicket(ticketId)

    @loggedIn
    def acceptGroupInvitation(self, groupId):
        return self.talk.acceptGroupInvitation(0, groupId)

    @loggedIn
    def acceptGroupInvitationByTicket(self, groupId, ticketId):
        return self.talk.acceptGroupInvitationByTicket(0, groupId, ticketId)

    @loggedIn
    def cancelGroupInvitation(self, groupId, contactIds):
        return self.talk.cancelGroupInvitation(0, groupId, contactIds)

    @loggedIn
    def createGroup(self, name, midlist):
        return self.talk.createGroup(0, name, midlist)

    @loggedIn
    def getGroup(self, groupId):
        return self.talk.getGroup(groupId)

    @loggedIn
    def getGroups(self, groupIds):
        return self.talk.getGroups(groupIds)

    @loggedIn
    def getGroupsV2(self, groupIds):
        return self.talk.getGroupsV2(groupIds)

    @loggedIn
    def getCompactGroup(self, groupId):
        return self.talk.getCompactGroup(groupId)

    @loggedIn
    def getCompactRoom(self, roomId):
        return self.talk.getCompactRoom(roomId)

    @loggedIn
    def getGroupIdsByName(self, groupName):
        gIds = []
        for gId in self.getGroupIdsJoined():
            g = self.getCompactGroup(gId)
            if groupName in g.name:
                gIds.append(gId)
        return gIds

    @loggedIn
    def getGroupIdsInvited(self):
        return self.talk.getGroupIdsInvited()

    @loggedIn
    def getGroupIdsJoined(self):
        return self.talk.getGroupIdsJoined()

    @loggedIn
    def updateGroupPreferenceAttribute(self, groupMid, updatedAttrs):
        return self.talk.updateGroupPreferenceAttribute(0, groupMid, updatedAttrs)

    @loggedIn
    def inviteIntoGroup(self, groupId, midlist):
        return self.talk.inviteIntoGroup(0, groupId, midlist)

    @loggedIn
    def kickoutFromGroup(self, groupId, midlist):
        return self.talk.kickoutFromGroup(0, groupId, midlist)

    @loggedIn
    def leaveGroup(self, groupId):
        return self.talk.leaveGroup(0, groupId)

    @loggedIn
    def rejectGroupInvitation(self, groupId):
        return self.talk.rejectGroupInvitation(0, groupId)

    @loggedIn
    def reissueGroupTicket(self, groupId):
        return self.talk.reissueGroupTicket(groupId)

    @loggedIn
    def updateGroup(self, groupObject):
        return self.talk.updateGroup(0, groupObject)

    """Room"""

    @loggedIn
    def createRoom(self, midlist):
        return self.talk.createRoom(0, midlist)

    @loggedIn
    def getRoom(self, roomId):
        return self.talk.getRoom(roomId)

    @loggedIn
    def inviteIntoRoom(self, roomId, midlist):
        return self.talk.inviteIntoRoom(0, roomId, midlist)

    @loggedIn
    def leaveRoom(self, roomId):
        return self.talk.leaveRoom(0, roomId)

    @loggedIn
    def sendReplyMention(self, id, to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@G-operaa "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ps
            for mid in mids:
                textx += str(texts[mids.index(mid)])
                slen = len(textx)
                elen = len(textx) + 18
                arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ps
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        return self.sendReplyMessage(id, to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

    @loggedIn
    def sendMention(self,to, text="", mids=[]):
        arrData = ""
        arr = []
        mention = "@JustGood "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
               raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            for mid in mids:
                textx += str(texts[mids.index(mid)])
                slen = len(textx)
                elen = len(textx) + 15
                arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ""
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        return self.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'),'STKVER': '1', 'STKID': '1589706', 'STKPKGID': '2000024'}, 0)

    """Call"""
        
    @loggedIn
    def acquireCallTalkRoute(self, to):
        return self.talk.acquireCallRoute(to)
    
    """Report"""

    @loggedIn
    def reportSpam(self, chatMid, memberMids=[], spammerReasons=[], senderMids=[], spamMessageIds=[], spamMessages=[]):
        return self.talk.reportSpam(chatMid, memberMids, spammerReasons, senderMids, spamMessageIds, spamMessages)
        
    @loggedIn
    def reportSpammer(self, spammerMid, spammerReasons=[], spamMessageIds=[]):
        return self.talk.reportSpammer(spammerMid, spammerReasons, spamMessageIds)
