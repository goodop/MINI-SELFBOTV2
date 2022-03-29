# -*- coding: utf-8-*-
from Imgood.linepy import *
from Imgood.akad import *
from Imgood.linepy.style import *
from Imgood.linepy.login import *
from justgood import imjustgood
from time import sleep
from gtts import gTTS
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread, active_count
import os,traceback,sys,json,time,ast,requests,re,random,pytz
from Liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
"""
                      **  MINI SELFBOT VERSION 2 ** 

                    BOT TYPE      -  MINI SELFBOT
                    DEVELOPER     -  IMJUSTGOOD.COM/TEAM
                    SOURCE LIB    -  PYPI/LINEPY
                    MEDIA API     -  PYPI/JUSTGOOD
                    PUBLISHED     -  GITHUB.COM/GOODOP/MINI-SELFBOTV2
"""
login = json.loads(open('Data/token.json','r').read())
setting = json.loads(open('Data/settings.json','r').read())
cctv = json.loads(open('Data/cctv.json','r').read())
loger = Login()

if login["email"] == "":
   if login["token"] == "":
      data = loger.logqr(cert=None) #You can put your Crt token here
      client = LINE(idOrAuthToken=data)
      login["token"] = data
      with open('Data/token.json', 'w') as fp:
        json.dump(login, fp, sort_keys=True, indent=4)
   else:
       try:
           client = LINE(idOrAuthToken=login["token"])
       except:
           print("TOKEN EXPIRED");sys.exit()
else:
  client = LINE(login["email"],login["password"])


flex = Autobots()
clPoll = OEPoll(client)
starting = time.time()
mid = client.profile.mid
media = imjustgood(setting["apikey"])
host = "https://{}".format(setting["main"])
oburl = client.server.LINE_OBJECT_URL
protectMax = setting["proMax"]
protectStaff = setting["proStaff"]
read = {
    "addwhitelist":False,
    "delwhitelist":False, 
    "addblacklist":False,
    "delblacklist":False,
    "dual":False,
    "dual2":False,
    "pp":False,
    "gpict":{},
    "cctv":{},
    "imgurl":{},
    "wmessage":{},
    "lmessage": ""
}

"""
                    ** LINE OPERATION FUNCTION ** 

"""
def Oup(op):
       if op.type in [19,133]:
           if op.param3 not in mid:
               if op.param1 in protectStaff:
                   th = Thread(target=prostaff(op,))
                   th.start()
                   th.join()
               elif op.param1 in protectMax:
                   th =Thread(target=promax(op,))
                   th.start()
                   th.join()
           else:kekick(op)       

       if op.type in [13,124]:
           if op.param1 in protectMax:
               th = Thread(target=proinvite(op,))
               th.start()
               th.join()

       if op.type == 55 :
           try:
             target = [ax.mid for ax in client.getGroup(op.param1).members]
             if op.param1 in read["cctv"]:
                if op.param2 in target:
                    if op.param2 not in read["cctv"][op.param1]:
                        user = ["Monyet lu","hai homo sapien","homo sapiens apa kabar?","piye mbakmu ayu ra?"]
                        data = random.choice(user)
                        text = "• @!  {}".format(data)       
                        client.sendMention(op.param1,text,[op.param2])
                        read["cctv"][op.param1][op.param2] = True
             if op.param1 in cctv['readPoint']:
                 timezone = pytz.timezone("Asia/Jakarta")
                 timing = datetime.now(tz=timezone)
                 timer = timing.strftime('%H.%M')
                 if op.param2 in cctv['readPoint'][op.param1]:pass
                 else:
                   cctv['readPoint'][op.param1][op.param2] = True
                   cctv['readMember'][op.param1][op.param2] = "Time: {}".format(timer)
                   with open('Data/cctv.json', 'w') as fp:
                      json.dump(cctv, fp, sort_keys=True, indent=4)
           except:pass

       if op.type in [17,130]:
           if op.param1 in setting["welcome"]:
              if op.param2 not in setting["blacklist"]:
                  jangan = client.getGroup(op.param1)
                  if op.param1 in read["wmessage"]: 
                     text = "Hi @! \nWelcome to " + jangan.name + "\n" + read["wmessage"][op.param1]
                     client.sendMention(op.param1,text,[op.param2])
                     client.sendPage(op.param1)
                  else:
                     text = "Hi @! \nWelcome to " + jangan.name 
                     client.sendMention(op.param1,text,[op.param2])
                     client.sendPage(op.param1)


       if op.type in [15,128]:
          if setting["leave"] == True:
              if op.param2 not in setting["blacklist"]:
                  jangan = client.getGroup(op.param1)
                  if read["lmessage"] !="":
                      mess = read["lmessage"] + " @! "
                      client.sendMention(op.param1,mess,[op.param2])
                  else:
                      mess = "Good bye @! "
                      client.sendMention(op.param1,mess,[op.param2])


       if op.type == 5 :
           if setting["adders"] == True:
               if op.param1 not in setting["blacklist"]:
                   if setting["addmsg"] == "":client.sendMention(op.param1,"Hi @! \nThank u for add me :)",[op.param1])
                   else:
                      text = "Hi @! \n" + setting["addmsg"]
                      client.sendMention(op.param1,text,[op.param1])


       if op.type in [13,17,55,124,130]:
          if op.param2 in setting["blacklist"]:
              try:client.kickoutFromGroup(op.param1,[op.param2])
              except:pass


       if op.type in [32,126]:
           if op.param1 in protectMax:
               if op.param2 not in setting["whitelist"]:
                  setting["blacklist"].append(op.param2)
                  with open('Data/settings.json', 'w') as fp:
                    json.dump(setting, fp, sort_keys=True, indent=4)
                  try:
                     client.kickoutFromGroup(op.param1,[op.param2])                     
                     client.findAndAddContactsByMid(op.param3)
                     client.inviteIntoGroup(op.param1,[op.param3])
                  except:pass                   

       if op.type in [11,122]:
           if op.param1 in protectMax and op.param3 == "4":
               if op.param2 not in setting["whitelist"]:
                   setting["blacklist"].append(op.param2)
                   with open('Data/settings.json', 'w') as fp:
                      json.dump(setting, fp, sort_keys=True, indent=4)
                   hoax = client.getGroup(op.param1)
                   if hoax.preventedJoinByTicket == False:
                      abc = client.getGroup(op.param1)
                      abc.preventedJoinByTicket = True
                      client.updateGroup(abc)
                      try:client.kickoutFromGroup(op.param1,[op.param2])
                      except:pass
               else:
                  hoax = client.getGroup(op.param1)
                  if hoax.preventedJoinByTicket == False:
                     abc = client.getGroup(op.param1)
                     abc.preventedJoinByTicket = True
                     client.updateGroup(abc)                  
      
       if op.type == 11:
           if op.param1 in protectMax and op.param3 == "1":
               if op.param2 not in setting["whitelist"]:
                   setting["blacklist"].append(op.param2)
                   with open('Data/settings.json', 'w') as fp:
                      json.dump(setting, fp, sort_keys=True, indent=4)
                   hoax = client.getGroup(op.param1).name
                   if hoax not in setting["gname"][op.param1]:
                      abc = client.getGroup(op.param1)
                      abc.name = setting["gname"][op.param1]
                      client.updateGroup(abc)
                      try:client.kickoutFromGroup(op.param1,[op.param2])
                      except:pass
               else:
                  abc = client.getGroup(op.param1).name                     
                  setting["gname"][op.param1] = abc
                  with open('Data/settings.json', 'w') as fp:
                     json.dump(setting, fp, sort_keys=True, indent=4)

       if op.type == 25:
            try:
                msg = op.message
                txt = msg.text
                if msg.toType in [0,2]:
                   to = msg.to
                   ids = msg.id
                   msg.to = msg.to
                   if msg.contentType == 0:
                      if None == txt:
                          return
                      cmd = txt.lower()
                      rname = setting["rname"].lower() + " "
                      link = txt[txt.find(":")+2:]
                      search = txt[txt.find(":")+2:].lower()
                      if cmd== ".help" or cmd== rname + "help":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          menu = "       Media             Stealing\n       Utility              Listing\n       Settings         Protection\n       Groupset       Customing\n       ───────────\n       Use 「 • 」for prefix."
                          client.help(msg.to,label,menu)

                      if cmd== ".media" or cmd== rname + "media":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          menu = open('help/media.txt','r').read()
                          client.help(msg.to,label,menu)

                      if cmd== ".utility" or cmd== rname + "utility":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          menu = open('help/utility.txt','r').read()
                          client.center(msg.to,label,menu)

                      if cmd== ".listing" or cmd== rname + "listing":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          menu = open('help/listing.txt','r').read()
                          client.center(msg.to,label,menu)

                      if cmd== ".stealing" or cmd== rname + "stealing":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          menu = open('help/stealing.txt','r').read()
                          client.help(msg.to,label,menu)

                      if cmd== ".groupset" or cmd== rname + "groupset":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          menu = open('help/groupset.txt','r').read()
                          client.help(msg.to,label,menu)

                      if cmd== ".protection" or cmd== rname + "protection":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          menu = open('help/protect.txt','r').read()
                          client.help(msg.to,label,menu)

                      if cmd== ".customing" or cmd== rname + ".customing":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          menu = open('help/customing.txt','r').read()
                          client.help(msg.to,label,menu)

                      if cmd== ".settings" or cmd== rname + ".settings":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          justgood = "https://imagizer.imageshack.com/img923/8396/vCgPT5.png"
                          data = ""
                          if msg.to not in protectMax and msg.to not in protectStaff:data += "\n\n🔴 ALL PROTECTION"
                          else:
                             if msg.to in protectMax:data += "\n\n🟢 PROTECT MAX"
                             elif msg.to in protectStaff:data += "\n\n🟢 PROTECT STAFF"
                          if setting["ticket"]:data += "\n🟢 JOIN TICKET"
                          else:data += "\n🔴 JOIN TICKET"
                          if msg.to in setting["welcome"]:data += "\n🟢 WELCOME MESSAGE"
                          else:data += "\n🔴 WELCOME MESSAGE"
                          if setting["leave"]:data += "\n🟢 LEAVE MESSAGE"
                          else:data += "\n🔴 LEAVE MESSAGE"
                          if setting["adders"]:data += "\n🟢 ADD MESSAGE"
                          else:data += "\n🔴 ADD MESSAGE"
                          datax = {"type":"bubble","size":"kilo","body":{"type":"box","layout":"vertical","backgroundColor":"#000000","contents":[{"type":"box","layout":"vertical","contents":[{"type":"text","text":"SETTINGS","color":"#FFC300","weight":"bold","size":"xxs"}],"position":"absolute","offsetTop":"15px","offsetStart":"15px","borderWidth":"1px","borderColor":"#FFC300","cornerRadius":"50px","paddingStart":"7px","paddingEnd":"7px","paddingTop":"2px","paddingBottom":"2px"},{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"vertical","contents":[{"type":"image","url":justgood,"aspectRatio":"1:1","aspectMode":"cover","action":{"type":"uri","uri":justgood}}],"cornerRadius":"100px"}],"alignItems":"center","paddingTop":"20px"},{"type":"box","layout":"vertical","contents":[{"type":"text","text":label.upper(),"weight":"bold","size":"md","color":"#FFC300"},{"type":"text","text":"Im Just Good","color":"#FFC300cc","size":"xxs"}],"alignItems":"center","paddingTop":"10px"},{"type":"box","layout":"vertical","contents":[{"type":"text","text":data,"color":"#FFC300","size":"xs","wrap":True}],"paddingTop":"15px","paddingBottom":"5px"}],"paddingAll":"10px","paddingStart":"15px","paddingEnd":"15px","paddingBottom":"10px"}}
                          client.sendFlex(msg.to,datax)


                      '''  ** UTILITY **  ''' 

                      if cmd== ".me" or cmd== rname + "me":
                          client.me(msg.to)

                      if cmd in [".speed","sp","speed",".sp"] or cmd== rname + "speed":                      
                          rend = time.time()
                          client.getProfile() 
                          yosh = time.time() - rend
                          client.sendMention(msg.to, "「   @!   」\nTime: %.4f"%(yosh),[mid])

                      if cmd in ["rname",".rname","mykey",".mykey"] or cmd== rname + "rname":
                          client.sendMessage(msg.to,setting["rname"].title())

                      if cmd== ".kickall" or cmd== rname + "kickall" or cmd == setting["keykick"].lower():
                         if msg.toType == 2:
                            hoax = client.getGroup(msg.to)
                            client.sendMessage(msg.to,"Goodbye Bitch ~")
                            for ax in hoax.members:
                               if ax.mid not in setting["whitelist"]:
                                  client.kickoutFromGroup(msg.to,[ax.mid])
                            client.sendMessage(msg.to,"Rubish has been cleared")

                      if cmd== ".unsend" or cmd== rname + ".unsend":       
                         client.sendMessage(msg.to,"「   Usage 」\n.unsend num")
                      if cmd.startswith(".unsend ") or cmd.startswith(rname + "unsend "):
                         msgid = cmd.split("unsend ")[1]                        
                         if msgid.isdigit():
                            mess = client.getRecentMessagesV2(msg.to,999)                     
                            mes = []
                            for x in mess:
                                if x._from == mid:    
                                   mes.append(x.id)                            
                                   if len(mes) == int(msgid):break                       
                            for b in mes:
                                try:client.unsendMessage(b)
                                except:pass
                         else:client.sendMessage(msg.to,"「   Usage 」\n.unsend num")

                      if cmd== ".runtime" or cmd== rname + "runtime":
                         high = time.time() - starting
                         voltage =  "Selfbot has been running for:\n"+runtime(high)
                         client.sendMessage(msg.to,f"{voltage}")

                      if cmd== ".reboot":
                          client.sendMessage(msg.to,"restarting..")
                          restart()

                      if cmd== ".allowliff":
                         try:
                            liff()
                            client.sendFlexText(msg.to,"Flex enabled.")
                         except:client.sendReplyMessage(ids,to,"Click and allow url to enable flex\nline://app/1602876096-e9QWgjyo")

                      if cmd== ".tagall":
                         group = client.getGroup(msg.to)
                         midMembers = [contact.mid for contact in group.members]
                         midSelect = len(midMembers)//20
                         for mentionMembers in range(midSelect+1):
                             ret_ = "• MENTIONALL\n• IMJUSTGOOD\n• MINI SELFBOT\n"
                             no = 0;dataMid = [];
                             for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                 dataMid.append(dataMention.mid)
                                 ret_ += "\n{}. @!\n".format(str(no))
                                 no = (no+1)
                             ret_ += "\n\n「 Total {} Members 」".format(str(len(dataMid)))
                             client.sendMention(msg.to, ret_, dataMid)

                      '''  ** LISTING **  ''' 

                      if cmd== ".ginfo" or cmd== rname + "ginfo":
                          group = client.getGroup(msg.to)
                          try:gCreator = group.creator.displayName
                          except:gCreator = "Not Found"
                          if group.invitee is None:gPending = "0"
                          else:gPending = str(len(group.invitee))
                          if group.pictureStatus is None:gpict = "https://imagizer.imageshack.com/img923/8396/vCgPT5.png"
                          else:gpict = oburl + group.pictureStatus
                          menu = "\nTotal Members : {}".format(str(len(group.members)))
                          menu += "\nTotal Pending : {}".format(gPending)
                          if group.preventedJoinByTicket == True:menu += "\nGroup QR : Clossed"
                          else:menu += "\nGroup QR: Open"
                          data={"type":"bubble","size":"kilo","body":{"type":"box","layout":"vertical","backgroundColor":"#000000","contents":[{"type":"box","layout":"vertical","contents":[{"type":"text","text":"GROUP INFO","color":"#FFC300","weight":"bold","size":"xxs"}],"position":"absolute","offsetTop":"15px","offsetStart":"15px","borderWidth":"1px","borderColor":"#FFC300","cornerRadius":"50px","paddingStart":"7px","paddingEnd":"7px","paddingTop":"2px","paddingBottom":"2px"},{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"vertical","contents":[{"type":"image","url":gpict,"aspectRatio":"1:1","aspectMode":"cover","action":{"type":"uri","uri":gpict}}],"cornerRadius":"100px"}],"alignItems":"center","paddingTop":"20px"},{"type":"box","layout":"vertical","contents":[{"type":"text","text":group.name,"weight":"bold","size":"md","color":"#FFC300"},{"type":"text","text":"Created By: {}".format(gCreator),"color":"#FFC300cc","size":"xxs"}],"alignItems":"center","paddingTop":"10px"},{"type":"box","layout":"vertical","contents":[{"type":"text","text":menu,"color":"#FFC300","size":"xs","wrap":True}],"paddingTop":"15px","paddingBottom":"5px"}],"paddingAll":"10px","paddingStart":"15px","paddingEnd":"15px","paddingBottom":"10px"}}
                          client.sendFlex(msg.to,data)
                          try:client.sendContact(msg.to,group.creator.mid)
                          except:pass
                          if group.preventedJoinByTicket == False:
                              gqropen = "GROUP URL:\nhttps://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                              try:client.sendMessage(msg.to,gqropen)
                              except:pass

                      if cmd== ".gbirth" or cmd== rname + "gbirth":
                          client.gbirth(msg.id,msg.to)

                      if cmd== ".groups" or cmd== rname + "groups":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          gruplist = client.getGroupIdsJoined()
                          kontak = client.getGroups(gruplist)
                          num=0;menu="Grouplist:\n"
                          for ids in kontak:
                             menu +="\n%i . %s" % (num, ids.name) + " (" + str(len(ids.members)) + ")"
                             num=(num+1)
                          menu +="\n\nTotal : %i Groups." % len(kontak)
                          client.help(msg.to,label,menu)

                      if cmd== ".groupid" or cmd== rname + "groupid":
                          client.sendMessage(msg.to,"{}".format(client.getGroup(msg.to).id))

                      if cmd== ".friendlist" or cmd== rname + "friendlist":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          contactlist = client.getAllContactIds()
                          contacts = client.getContacts(contactlist)
                          num=1;menu="Friendlist:\n"
                          for ids in contacts:
                              menu +="\n%i. %s" % (num, ids.displayName)
                              num=(num+1)
                          menu +="\n\nTotal: %i Friends" % len(contacts)
                          client.help(msg.to,label,menu)

                      if cmd== ".pendinglist" or cmd== rname + "pendinglist":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          pending = client.getGroup(msg.to)
                          if pending.invitee is None:client.sendMessage(msg.to,"Pendinglist empty.")
                          else:
                             pendinglist = [a.mid for a in pending.invitee]
                             num = 1;menu = "Pendinglist:\n"
                             for xx in pendinglist:
                                 menu +="\n%i. %s" % (num, client.getContact(xx).displayName)
                                 num = (num+1)                                 
                             menu +="\n\nTotal: %i pendings." % len(pendinglist)
                             client.help(msg.to,label,menu)

                      if cmd== ".memberlist" or cmd== rname + "pendinglist":
                          if cmd.startswith('.'):label = cmd.replace('.','')
                          else:label = cmd.replace(rname,"")
                          member = client.getGroup(msg.to)
                          members = [a.mid for a in member.members]
                          num = 1;menu = "Memberlist:\n"
                          for xx in members:
                              menu +="\n%i. %s" % (num, client.getContact(xx).displayName)
                              num = (num+1)                                 
                          menu +="\n\nTotal: %i members." % len(members)
                          client.help(msg.to,label,menu)

                      if cmd.startswith(".clear") or cmd.startswith(rname + "clear"):
                          clearing = cmd.split("clear")[1] 
                          if clearing == "blacklist":
                              if setting["blacklist"] == []:
                                  client.sendMessage(msg.to,"Blacklist empty!")
                              else:
                                  setting["blacklist"] = []
                                  with open('Data/settings.json', 'w') as fp:
                                      json.dump(setting, fp, sort_keys=True, indent=4)
                                  client.sendReplyMessage(msg.id,msg.to,"blacklist cleared.")
                          elif clearing == "whitelist":
                              if setting["whitelist"] == []:
                                  client.sendMessage(msg.to,"Whitelist empty!")
                              else:
                                  setting["whitelist"] = []
                                  with open('Data/settings.json', 'w') as fp:
                                      json.dump(setting, fp, sort_keys=True, indent=4)
                                  client.sendReplyMessage(msg.id,msg.to,"Whitelist cleared.")

                      if cmd== ".whitelist" or cmd== rname + "whitelist":
                          listing = setting["whitelist"]
                          no = 1; data = "• Imjustgood\n• Whitelist:\n\n"
                          for x in listing:
                              data +=" {}. @! it, \n".format(no)
                              no += 1
                          data +="\nTotal: {}".format(len(listing))
                          if listing == []:client.sendMessage(msg.to,"Whitelist empty!")
                          else:client.sendReplyMention(msg.id,msg.to,data,"",listing)

                      if cmd== ".blacklist" or cmd== rname + "blackist":
                          listing = setting["blacklist"]
                          no = 1; data = "• Imjustgood\n• Blacklist:\n\n"
                          for x in listing:
                              data +=" {}. @! it, \n".format(no)
                              no += 1
                          data += "\nTotal: {}".format(len(listing))
                          if listing == []:client.sendMessage(msg.to,"Blacklist empty!")
                          else:client.sendReplyMention(msg.id,msg.to,data,"",listing)

                      if cmd== ".findblacklist" or cmd== rname + "findblacklist":
                         if setting["blacklist"] == []:client.sendReplyMessage(msg.id, msg.to,"Blacklist empty!")
                         else:
                            find = client.getGroup(msg.to)
                            finded = []
                            for x in find.members:
                                if x.mid in setting["blacklist"]:
                                   finded.append(x.mid)                                
                            if finded == []:client.sendReplyMessage(ids,to,"No blacklist found\nin '{}'".format(find.name))
                            else:
                               data = [o for o in finded]
                               finding = len(data)//20
                               for gx in range(finding +1): 
                                      result = "• ImJustGood\n• Find Blacklist:\n"
                                      listed = []; no = 1
                                      for ax in data[gx*20:(gx+1)*20]:
                                            result += "\n  {}. @! it,\n".format(no)
                                            no = (no+1)
                                            listed.append(ax)
                                      result += "\nBe alert!「 {} 」here.\nGroup: {}".format(len(listed),find.name)             
                                      client.sendReplyMention(ids,to,result,'',listed)

                      '''    **   GROUPSET   **   ''' 

                      if cmd.startswith(".kick ") or cmd.startswith(rname + "kick "):
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              Mmbers = [a.mid for a in client.getGroup(msg.to).members]
                              hole = []
                              for mention in mentionees:
                                  if mention["M"] not in hole:
                                     if mention['M'] in Mmbers:
                                        hole.append(mention["M"])
                              for mmq in hole:
                                  try:client.kickoutFromGroup(msg.to, [mmq])
                                  except:client.sendMessage(msg.to, "Gagal son.")

                      if cmd.startswith(".invite ") or cmd.startswith(rname + "invite "):
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              Mmbers = [a.mid for a in client.getGroup(msg.to).members]
                              hole = [];
                              for mention in mentionees:
                                  if mention["M"] not in hole:
                                     if mention['M'] not in Mmbers:
                                        hole.append(mention["M"])
                              for mmq in hole:
                                  try:
                                      client.findAndAddContactsByMid(mmq)
                                      client.inviteIntoGroup(msg.to, [mmq])
                                  except:client.sendMessage(msg.to, "Gagal son.")

                      if cmd.startswith(".sleed ") or cmd.startswith(rname + "sleed "):
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              for mention in mentionees:
                                  try:
                                      client.kickoutFromGroup(msg.to, [mention['M']])
                                      client.findAndAddContactsByMid(mention['M'])
                                      client.inviteIntoGroup(msg.to, [mention['M']])
                                      client.cancelGroupInvitation(msg.to, [mention['M']])
                                  except:
                                     client.sendMessage(msg.to, "Gagal son.")

                      if cmd.startswith(".joinurl ") or cmd.startswith(rname + "joinurl "): 
                          mmq = msg.text.split(".joinurl ")[1] 
                          if mmq.startswith("http"):
                             asw = mmq.split("/ti/g/")[1]
                             mmk = client.findGroupByTicket(asw)
                             if mmk.id not in client.getGroupIdsJoined():
                                try:
                                   client.acceptGroupInvitationByTicket(mmk.id,asw)
                                   client.sendMessage(msg.to,"Success join to {}".format(mmk.name))
                                except:pass

                      if '/ti/g/' in cmd and setting["ticket"] == True:
                          data = msg.text.split('/ti/g/')[1]
                          if " " in data:
                             link = data.split(" ")[0]
                          elif "\n" in data:
                             link = data.split("\n")[0]
                          else:link = data
                          mmk = client.findGroupByTicket(link)
                          if mmk.id not in client.getGroupIdsJoined():
                              try:client.acceptGroupInvitationByTicket(mmk.id,link)
                              except:pass


                      if cmd.startswith(".sider ") or cmd.startswith(rname + "sider "):
                          data = cmd.split("sider ")[1]
                          if data == "on":
                              if msg.to in read["cctv"]:
                                  read["cctv"][msg.to] = {}
                                  client.sendMessage(msg.to,"sider restarting.")
                              else:
                                  read["cctv"][msg.to] = {}
                                  client.sendMessage(msg.to,"sider enabled.")
                          if data == "off":
                              if msg.to in read["cctv"]:
                                  del read["cctv"][msg.to]
                                  client.sendMessage(msg.to,"sider disabled.")
                              else:client.sendMessage(msg.to,"already disabled.") 


                      if cmd.startswith(".read") or cmd.startswith(rname + "read"):
                          data = cmd.split("read")[1]
                          if data == " on": 
                              timezone = pytz.timezone("Asia/Jakarta")
                              timeNow = datetime.now(tz=timezone)
                              readTime = "Starting read point\nTime: " + timeNow.strftime('%H:%M:%S')
                              if msg.to in cctv['readPoint']:
                                 cctv['readPoint'][msg.to] = {}
                                 cctv['readMember'][msg.to] = {}
                                 with open('Data/cctv.json', 'w') as fp:
                                    json.dump(cctv, fp, sort_keys=True, indent=4)
                                 client.sendReplyMessage(msg.id,msg.to,"Read point restarting.")
                              else:
                                 cctv['readPoint'][msg.to] = {}
                                 cctv['readMember'][msg.to] = {}
                                 with open('Data/cctv.json', 'w') as fp:
                                     json.dump(cctv, fp, sort_keys=True, indent=4)
                                 client.sendReplyMessage(msg.id, msg.to, readTime)                                       
                          if data == " off":
                              if msg.to not in cctv["readPoint"]:
                                  client.sendReplyMessage(msg.id, msg.to, "already disabled.")
                              else:
                                  del cctv['readPoint'][msg.to]
                                  del cctv['readMember'][msg.to]
                                  with open('Data/cctv.json', 'w') as fp:
                                     json.dump(cctv, fp, sort_keys=True, indent=4)
                                  client.sendReplyMessage(msg.id, msg.to, "read member disabled.")
                          if data == "ing":
                              if msg.to in cctv['readPoint']:
                                   if cctv["readMember"][msg.to].items() == []:
                                      client.sendReplyMessage(msg.id, msg.to,"Reader None")                              
                                   else:
                                      yos = ""; ren= []; ang = '• JustGood\n• Group reader:\n\n'
                                   for com in cctv["readMember"][msg.to]:
                                        heading = "@Goperation\n"
                                        just = str(len(yos)+len(ang))
                                        good = str(len(yos)+len(heading)+len(ang)-1)
                                        im = {'S':just, 'E':good, 'M':com}
                                        ren.append(im)
                                        yos += heading + " {}\n".format(cctv["readMember"][msg.to][com])
                                   text = ang + yos + "\nGroup: " + client.getGroup(msg.to).name
                                   try:client.sendReplyMessage(msg.id, msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(ren).replace(' ','')+'}')}, contentType=0)
                                   except Exception as e:print(e)

                      if cmd.startswith(".join ") or cmd.startswith(rname + "join "):
                          data = cmd.split("join ")[1]
                          if data == "on":
                              if setting["join"]:client.sendMessage(msg.to,"already enabled.")
                              else:
                                  setting["join"] = True
                                  with open('Data/settings.json', 'w') as fp:
                                     json.dump(setting, fp, sort_keys=True, indent=4)
                                  client.sendMessage(msg.to,"join enabled.")
                          if data == "off":
                              if setting["join"] == False:client.sendMessage(msg.to,"already disabled.")
                              else:
                                setting["join"] = False
                                with open('Data/settings.json', 'w') as fp:
                                   json.dump(setting, fp, sort_keys=True, indent=4)
                                client.sendMessage(msg.to,"already disabled.") 


                      if cmd.startswith(".ticket ") or cmd.startswith(rname + "ticket "):
                          data = cmd.split("ticket ")[1]
                          if data == "on":
                              if setting["ticket"]:client.sendMessage(msg.to,"already enabled.")
                              else:
                                  setting["ticket"] = True
                                  with open('Data/settings.json', 'w') as fp:
                                     json.dump(setting, fp, sort_keys=True, indent=4)
                                  client.sendMessage(msg.to,"Join ticket enabled.")
                          if data == "off":
                              if setting["ticket"] == False:client.sendMessage(msg.to,"Join ticket disabled.")
                              else:
                                setting["ticket"] = False
                                with open('Data/settings.json', 'w') as fp:
                                   json.dump(setting, fp, sort_keys=True, indent=4)
                                client.sendMessage(msg.to,"already disabled.")


                      if cmd.startswith(".addmsg ") or cmd.startswith(rname + "addmsg "):
                          data = cmd.split("addmsg ")[1]
                          if data == "on":
                              if setting["adders"]:client.sendMessage(msg.to,"already enabled.")
                              else:
                                  setting["adders"] = True
                                  with open('Data/settings.json', 'w') as fp:
                                     json.dump(setting, fp, sort_keys=True, indent=4)
                                  client.sendMessage(msg.to,"Add msg enabled.")
                          if data == "off":
                              if setting["adders"] == False:client.sendMessage(msg.to,"Already disabled.")
                              else:
                                setting["adders"] = False
                                with open('Data/settings.json', 'w') as fp:
                                   json.dump(setting, fp, sort_keys=True, indent=4)
                                client.sendMessage(msg.to,"add message disabled.")


                      if cmd.startswith(".leave ") or cmd.startswith(rname + "leave "):
                          data = cmd.split("leave ")[1]
                          if data == "on":
                              if setting["leave"]:client.sendMessage(msg.to,"already enabled.")
                              else:
                                  setting["leave"] = True
                                  with open('Data/settings.json', 'w') as fp:
                                     json.dump(setting, fp, sort_keys=True, indent=4)
                                  client.sendMessage(msg.to,"Leave msg enabled.")
                          if data == "off":
                              if setting["leave"] == False:client.sendMessage(msg.to,"already disabled.")
                              else:
                                setting["leave"] = False
                                with open('Data/settings.json', 'w') as fp:
                                   json.dump(setting, fp, sort_keys=True, indent=4)
                                client.sendMessage(msg.to,"leave message disabled.")

                      if cmd.startswith(".welcome ") or cmd.startswith(rname + "welcome "):
                          data = cmd.split("welcome ")[1]
                          if data == "on":
                              if msg.to in setting["welcome"]:client.sendMessage(msg.to,"already enabled.")
                              else:
                                  setting["welcome"][msg.to] = True
                                  with open('Data/settings.json', 'w') as fp:
                                     json.dump(setting, fp, sort_keys=True, indent=4)
                                  client.sendMessage(msg.to,"Welcome msg enabled.")
                          if data == "off":
                              if msg.to not in setting["welcome"]:client.sendMessage(msg.to,"welcome message disabled.")
                              else:
                                 del setting["welcome"][msg.to]
                                 with open('Data/settings.json', 'w') as fp:
                                    json.dump(setting, fp, sort_keys=True, indent=4)
                                 client.sendMessage(msg.to,"welcome message disabled.")


                      ''' ** STEALING ** ''' 

                      if cmd== ".geturl" or cmd== rname + "geturl": 
                         group = client.getGroup(msg.to)
                         if group.preventedJoinByTicket == True:
                            group.preventedJoinByTicket = False
                            client.updateGroup(group)
                            set = client.reissueGroupTicket(msg.to)
                            client.sendFlexText(msg.to, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))
                         else:
                             client.updateGroup(entot)
                             set = client.reissueGroupTicket(msg.to)
                             client.sendFlexText(msg.to, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))                        

                      if cmd== ".gpict" or cmd== rname + ".gpict": 
                          group = client.getGroup(msg.to)                          
                          data =  "{}{}".format(oburl,group.pictureStatus)
                          client.sendFlexImage(msg.to,data)

                      if cmd.startswith(".getpict ") or cmd.startswith(rname + "getpict "):
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              for mention in mentionees:
                                  if mention["M"] not in setting["maker"]:
                                      data = "{}{}".format(oburl,client.getContact(mention["M"]).pictureStatus)
                                      client.sendFlexImage(msg.to,data)
                                  else:client.sendMessage(msg.to,"Permission denied.")

                      if cmd.startswith(".getcover ") or cmd.startswith(rname + "getcover "):
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              for mention in mentionees:
                                  if mention["M"] not in setting["maker"]:
                                      data = client.getProfileCoverURL(mention['M'])
                                      client.sendFlexImage(msg.to,data)
                                  else:client.sendMessage(msg.to,"Permission denied.")

                      if cmd.startswith(".getmid ") or cmd.startswith(rname + "getmid "):
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              for mention in mentionees:
                                  if mention["M"] not in setting["maker"]:
                                      data = client.getContact(mention['M']).mid
                                      client.sendMessage(msg.to,data)
                                  else:client.sendMessage(msg.to,"Permission denied.")


                      if cmd.startswith(".getname ") or cmd.startswith(rname + "getname "):
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              for mention in mentionees:
                                  if mention["M"] not in setting["maker"]:
                                      data = client.getContact(mention['M']).displayName
                                      client.sendMessage(msg.to,"「   Name   」\n{}".format(data))
                                  else:client.sendMessage(msg.to,"Permission denied.")

                      if cmd.startswith(".getbio ") or cmd.startswith(rname + "getbio "):
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              for mention in mentionees:
                                  if mention["M"] not in setting["maker"]:
                                      data = client.getContact(mention['M']).statusMessage
                                      client.sendMessage(msg.to,"「   Bio   」\n{}".format(data))
                                  else:client.sendMessage(msg.to,"Permission denied.")


                      if cmd.startswith(".locate") or cmd.startswith(rname + "locate"):
                          cmdx = cmd.split(' @')[0]
                          if cmd.startswith('.'):label = cmdx.replace('.','')
                          else:label = cmdx.replace(rname,"")
                          gruplist = client.getGroupIdsJoined()
                          kontak = client.getGroups(gruplist)
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              no = 1; detect = [];menu= "Groups Joined:\n\n"
                              for mention in mentionees:
                                  profile = client.getContact(mention['M'])
                                  for xx in range(len(kontak)):
                                     located = [x.mid for x in kontak[xx].members]
                                     if mention['M'] in located:
                                        detect.append(kontak[xx].id)
                                        menu += " {}. {} ({})\n".format(no,kontak[xx].name,len(located))
                                        no = (no+1)
                              if detect == []:client.sendMessage(msg.to,"Nothing found.")
                              else:
                                 menu += "\n\nTotal: {} Groups.".format(len(detect))
                                 data ={"type":"bubble","size":"kilo","body":{"type":"box","layout":"vertical","backgroundColor": "#000000","contents":[{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"vertical","contents":[{"type":"image","url":"{}{}".format(oburl,profile.pictureStatus),"aspectRatio":"1:1","aspectMode":"cover"}],"cornerRadius":"100px"}],"alignItems":"center","paddingTop":"50px"},{"type":"box","layout":"vertical","contents":[{"type":"text","text":"{}".format(profile.displayName),"color":"#FFC300","weight":"bold","align":"center"},{"type":"text","text":"Tetaplah mesum","color":"#FFC300cc","align":"center","size":"xxs"}],"paddingAll":"10px"},{"type":"box","layout":"vertical","contents":[{"type":"text","text":label.upper(),"color":"#FFC300","weight":"bold","size":"xxs"}],"position":"absolute","borderWidth":"1px","borderColor":"#ffffffcc","paddingStart":"8px","paddingEnd":"8px","paddingTop":"5px","paddingBottom":"5px","offsetTop":"10px","offsetStart":"10px","cornerRadius":"20px"},{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"vertical","contents":[{"type":"text","text":menu,"color":"#FFC300","size":"xs","wrap":True}],"paddingAll":"20px","backgroundColor":"#111111"}],"paddingAll":"20px","paddingTop":"5px"}],"paddingAll":"0px"},"styles":{"body":{"backgroundColor":"#161e2b"}}}
                                 client.sendFlex(msg.to,data)

                      ''' ** PROTECTION ** ''' 

                      if cmd.startswith(".addwl ") or cmd.startswith(rname + "addwl "):
                          promote = cmd.split("addwl ")[1]
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              hole = [];white = setting["whitelist"]
                              no=0;data = "Whitelist added:\n"
                              for mention in mentionees:
                                  if mention["M"] not in setting["whitelist"] and mention['M'] not in setting["blacklist"]:
                                     hole.append(mention["M"])
                                     white.append(mention["M"])
                                     with open('Data/settings.json', 'w') as fp:
                                          json.dump(setting, fp, sort_keys=True, indent=4)
                                     data += "\n {}. @! it,".format(no)
                                     no = (no+1)
                                  else:
                                    client.sendMention(msg.to,"@!  already in whitelist or blacklist.",[mention["M"]])
                              datax = data + "\n\nTotal: {} user.".format(len(hole))
                              try:client.sendReplyMention(msg.id,msg.to,datax,"",hole)
                              except:pass
                          if promote == "on":
                                 client.sendMessage(msg.to,"send an contact.")
                                 read["addwhitelist"] = True


                      if cmd.startswith(".delwl ") or cmd.startswith(rname + "delwl "):
                          demote = cmd.split("delwl ")[1]
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              hole = [];white = setting["whitelist"]
                              no=1;data = "Whitelist removed:\n"
                              for mention in mentionees:
                                  if mention["M"] in setting["whitelist"]:
                                     hole.append(mention["M"])
                                     white.remove(mention["M"])
                                     with open('Data/settings.json', 'w') as fp:
                                          json.dump(setting, fp, sort_keys=True, indent=4)
                                     data += "\n{}. @! it,".format(no)
                                     no += 1
                                  else:
                                    client.sendMention(msg.to,"@!  not in whitelist.",[mention["M"]])                                     
                              data += "\n\nTotal: {} user.".format(len(hole))
                              try:client.sendReplyMention(msg.id,msg.to,data,"",hole)
                              except:pass
                          if demote == "on":
                                 client.sendMessage(msg.to,"send an contact.")
                                 read["delwhitelist"] = True



                      if cmd.startswith(".addbl ") or cmd.startswith(rname + "addbl "):
                          promote = cmd.split("addbl ")[1]
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              hole = [];white = setting["blacklist"]
                              no=1;data = "Blacklist added:\n"
                              for mention in mentionees:
                                  if mention["M"] not in setting["blacklist"] and mention['M'] not in setting["whitelist"]:
                                     hole.append(mention["M"])
                                     white.append(mention["M"])
                                     with open('Data/settings.json', 'w') as fp:
                                          json.dump(setting, fp, sort_keys=True, indent=4)
                                     data += "\n {}. @! it,".format(no)
                                     no = (no+1)
                                  else:
                                    client.sendMention(msg.to,"@!  already in whitelist or blacklist.",[mention["M"]])
                              datax = data + "\n\nTotal: {} user.".format(len(hole))
                              try:client.sendReplyMention(msg.id,msg.to,datax,"",hole)
                              except:pass
                          if promote == "on":
                              client.sendMessage(msg.to,"send an contact.")
                              read["addblacklist"] = True


                      if cmd.startswith(".delbl ") or cmd.startswith(rname + "delbl "):
                          demote = cmd.split("delbl ")[1]
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', cmd)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              hole = [];white = setting["blacklist"]
                              no=1;data = "Blacklist removed:\n"
                              for mention in mentionees:
                                  if mention["M"] in setting["blacklist"]:
                                     hole.append(mention["M"])
                                     white.remove(mention["M"])
                                     with open('Data/settings.json', 'w') as fp:
                                          json.dump(setting, fp, sort_keys=True, indent=4)
                                     data += " {}. @! it,\n".format(no)
                                     no += 1
                                  else:
                                    client.sendMention(msg.to,"@!  not in blacklist.",[mention["M"]])                                     
                              data += "\n\nTotal: {} user.".format(len(hole))
                              try:client.sendReplyMention(msg.id,msg.to,data,"",hole)
                              except:pass
                          if demote == "on":
                                 client.sendMessage(msg.to,"send an contact.")
                                 read["delblacklist"] = True

                      if cmd.startswith(".protect ") or cmd.startswith(rname + "protect "):
                          protection = cmd.split("protect ")[1]
                          if protection == "max":
                             if msg.to in protectMax:
                                client.sendMessage(msg.to,"Max protection already enabled.")
                             else:
                                if msg.to in protectStaff:
                                   del setting["proStaff"][msg.to]
                                   setting["proMax"][msg.to] = True
                                   jap = client.getGroup(msg.to)
                                   setting["gname"][msg.to] = jap.name
                                   with open('Data/settings.json', 'w') as fp:
                                       json.dump(setting, fp, sort_keys=True, indent=4)
                                   if client.getGroup(msg.to).preventedJoinByTicket == False:
                                      hoax = client.getGroup(msg.to)
                                      hoax.preventedJoinByTicket = True
                                      client.updateGroup(hoax)
                                      client.sendMessage(msg.to,"Protect max enabled.")
                                   else:client.sendMessage(msg.to,"Protect max enabled.")
                                else:
                                  if msg.to not in protectStaff and msg.to not in protectMax:    
                                      setting["proMax"][msg.to] = True
                                      jap = client.getGroup(msg.to)
                                      setting["gname"][msg.to] = jap.name
                                      if client.getGroup(msg.to).preventedJoinByTicket == False:
                                         hoax = client.getGroup(msg.to)
                                         hoax.preventedJoinByTicket = True
                                         client.updateGroup(hoax)           
                                         client.sendMessage(msg.to,"Protect max enabled.")
                                      else:client.sendMessage(msg.to,"Protect max enabled.")
                          elif protection == "staff":               
                             if msg.to in protectStaff:
                                client.sendMessage(msg.to,"Protect staff already enabled.")
                             elif msg.to in protectMax:
                                    del setting["proMax"][msg.to]
                                    setting["proStaff"][msg.to] = True
                                    jap = client.getGroup(msg.to)
                                    setting["gname"][msg.to] = jap.name
                                    with open('Data/settings.json', 'w') as fp:
                                        json.dump(setting, fp, sort_keys=True, indent=4)
                                    if client.getGroup(msg.to).preventedJoinByTicket == False:
                                       hoax = client.getGroup(msg.to)
                                       hoax.preventedJoinByTicket = True
                                       client.updateGroup(hoax)
                                       client.sendMessage(msg.to,"Protect staff enabled.")
                                    else:client.sendMessage(msg.to,"Protect staff enabled.")
                             else:
                                 setting["proStaff"][msg.to] = True
                                 jap = client.getGroup(msg.to)
                                 setting["gname"][msg.to] = jap.name
                                 with open('Data/settings.json', 'w') as fp:
                                     json.dump(setting, fp, sort_keys=True, indent=4)
                                 if client.getGroup(msg.to).preventedJoinByTicket == False:
                                    hoax = client.getGroup(msg.to)
                                    hoax.preventedJoinByTicket = True
                                    client.updateGroup(hoax)           
                                    client.sendMessage(msg.to,"Protect staff enabled.")
                                 else:client.sendMessage(msg.to,"Protect staff enabled.")
                          elif protection == "none":    
                             if msg.to not in protectStaff and msg.to not in protectMax:
                                client.sendMessage(msg.to,"Protection already disabled.")
                             else:
                                if msg.to in protectMax:
                                    del setting["proMax"][msg.to]
                                    with open('Data/settings.json', 'w') as fp:
                                        json.dump(setting, fp, sort_keys=True, indent=4)
                                    client.sendMessage(msg.to,"Protection disabled.")
                                else:
                                   if msg.to in protectStaff:
                                       del setting["proStaff"][msg.to]
                                       jap = client.getGroup(msg.to)
                                       setting["gname"][msg.to] = jap.name
                                       with open('Data/settings.json', 'w') as fp:
                                           json.dump(setting, fp, sort_keys=True, indent=4)
                                       client.sendMessage(msg.to,"Protection disabled.")

                      ''' ** CUSTOMING '''

                      if cmd == ".apikey" or cmd == rname + "apikey":
                         data = "「  Usage  」\n .apikey: status\n .apikey: YOUR APIKEY"
                         client.sendFlexText(to,data)
                      if cmd.startswith(".apikey: ") or cmd.startswith(rname + "apikey: "):
                          if search == "status":
                              url = f"{host}/status?apikey={setting['apikey']}"
                              head= {"User-Agent":"Mozilla/0.5"}
                              data = json.loads(requests.get(url,headers=head).text)
                              main = data["result"]
                              info = "𝐀𝐏𝐈.𝐈𝐌𝐉𝐔𝐒𝐓𝐆𝐎𝐎𝐃.𝐂𝐎𝐌"
                              info += f"\n\nID : {main['id']}"
                              info += f"\nTYPE : {main['type']}"
                              info += f"\nUSAGE : {main['usage']}"
                              info += f"\nEXPIRED : {main['expired']}"
                              info += f"\nRESTART : {main['restart']}"
                              info += f"\n\nSERVICE : bit.ly/imjustgood-tools"
                              client.sendFlexText(to,info)
                          else:
                             setting["apikey"] = link
                             with open('Data/settings.json', 'w') as fp:
                                 json.dump(setting, fp, sort_keys=True, indent=4)
                             client.sendMessage(to,"Apikey was upgrade.")

                      if cmd.startswith(".upbio: ") or cmd.startswith(rname + "upbio: "):
                          biograp = cmd.split("bio: ")[1]
                          if len(biograp) <= 100:
                              profile = client.getProfile()
                              profile.statusMessage = biograp
                              client.updateProfile(profile)
                              client.sendReplyMessage(msg.id,msg.to, "Status bio updated to:\n{}".format(biograp))
                          else:client.sendReplyMessage(msg.id,msg.to,"Maximum 100 character.")

                      if cmd.startswith(".upname: ") or cmd.startswith(rname + "upname: "):
                          dname = cmd.split("upname: ")[1]
                          if len(dname) <= 100:
                               profile = client.getProfile()
                               profile.displayName = dname.title()
                               client.updateProfile(profile)
                               client.sendReplyMessage(msg.id,msg.to, "Profile name updated to:\n{}".format(dname.title()))
                          else:client.sendReplyMessage(msg.id,msg.to,"Maximum 20 character.")

                      if cmd.startswith(".rname: ") or cmd.startswith(rname + "rname: "):
                          rnamed = cmd.split("name: ")[1] 
                          setting["rname"] = rnamed
                          with open('Data/settings.json', 'w') as fp:
                             json.dump(setting, fp, sort_keys=True, indent=4)
                          client.sendReplyMessage(msg.id,msg.to, "Rname updated to:\n{}".format(rnamed.title()))


                      if cmd == ".keykick" or cmd == rname + "keykick":
                          client.sendFlexText(to,"「   Usage   」\n.keykick: YOUR KEY\n.keykick: reset\n.keykick: cek")
                      if cmd.startswith(".keykick: ") or cmd.startswith(rname + "keykick: "):
                         kicked = cmd.split("kick: ")[1] 
                         if kicked == "reset":
                            setting["keykick"] = ""
                            with open('Data/settings.json', 'w') as fp:
                                json.dump(setting, fp, sort_keys=True, indent=4)
                            client.sendReplyMessage(msg.id,msg.to, "Key reseted")
                         elif kicked == "cek":client.sendReplyMessage(msg.id,msg.to, "Your key: {}".format(setting["keykick"]))
                         else:
                            setting["keykick"] = kicked
                            with open('Data/settings.json', 'w') as fp:
                               json.dump(setting, fp, sort_keys=True, indent=4)
                            client.sendReplyMessage(msg.id,msg.to, "Key updated to:\n{}".format(kicked.title()))


                      if cmd.startswith(".leavemsg: ") or cmd.startswith(rname + "leavemsg: "):
                          data = cmd.split("msg: ")[1]
                          read["lmessage"] = data
                          client.sendMessage(msg.to,"Leave message update to:\n{}".format(data))

                      if cmd.startswith(".welcomsg: ") or cmd.startswith(rname + "welcomsg: "):
                          data = cmd.split("msg: ")[1]
                          if msg.to in setting["welcome"]:
                             read["wmessage"][msg.to] = data
                             client.sendMessage(msg.to,"Welcome message update to:\n{}".format(data))
                          else:client.sendMessage(msg.to,"Welcome message not active\nPlease enabled welcome first.")

                      if cmd.startswith(".gname: ") or cmd.startswith(rname + "gname: "):
                          gname = msg.text.split("name: ")[1] 
                          g = client.getGroup(msg.to)
                          g.name = gname
                          client.updateGroup(g)
                          client.sendReplyMessage(msg.id,msg.to, "Group updated to:\n{}".format(gname))

                      if cmd.startswith(".broadcast: ") or cmd.startswith(rname + "broadcast: "):
                         bc = cmd.split("broadcast: ")[1]
                         groups = client.getGroupIdsJoined()
                         allGc = client.getGroups(groups)
                         youBc = "「   Broadcast Message   」\nSender: @! \nSupport: https://{}\nBroadcasted: {} Groups\n────────────────\n{}".format(host,len(allGc),bc)
                         for x in range(len(allGc)):
                             client.sendMention(allGc[x].id, youBc,[mid])                           
                         client.sendReplyMessage(id,to,"Success Broadcasted on {} groups.".format(len(allGc)))

                      if cmd.startswith(".update") or cmd.startswith(rname + "updatepict"):
                          data = cmd.split("update")[1]                          
                          if data == "pict":
                              read["pp"] = True
                              client.sendMessage(msg.to,"send an image.")
                          elif data == "dual":
                              read["dual"] = True
                              client.sendMessage(msg.to,"send an video.")
                          elif data == "gpict":
                              read["gpict"][msg.to] = True
                              client.sendMessage(msg.to,"send an image.")


                      ''' ** MEDIA FEATURE ** ''' 


                      if cmd.startswith(".joox: ") or cmd.startswith(rname + "joox: "):
                         data = media.joox(search)
                         main = data['result']
                         result = flex.joox(main)
                         client.sendFlex(to,result)
                         client.sendAudioWithURL(to,main["mp3Url"])
                      
                      if cmd.startswith(".youtube") or cmd.startswith(rname + "youtube"):
                         query = cmd.split("youtube")[1]
                         if query.startswith("dl: http"):
                            data = media.youtubedl(link)
                            main = data["result"]
                            result = flex.youtube(main)
                            client.sendFlex(to,result)
                            client.sendFlexVideo(to,main["videoUrl"],main["thumbnail"])
                            client.sendFlexAudio(to,main["audioUrl"])
                         if query.startswith(": "):
                            data = media.youtube(search)
                            main = data['result']
                            result = flex.youtube(main)
                            client.sendFlex(to,result)
                            client.sendFlexVideo(to,main["videoUrl"],main["thumbnail"])
                            client.sendFlexAudio(to,main["audioUrl"])
                     
                      if cmd.startswith(".lyric: ") or cmd.startswith(rname + "lyric: "):
                          data = media.lyric(search)
                          main = data['result']
                          result = flex.lyric(main)
                          client.sendFlex(to,result)

                      if cmd.startswith(".tiktok") or cmd.startswith(rname + "tiktok"):
                          query = cmd.split("tiktok")[1]
                          if query.startswith("dl: http"):
                              client.sendMessage(to,"Downloading..")
                              data = media.tiktokdl(link)
                              result = data['result']['watermark']
                              client.sendVideoWithURL(to,result)
                          if query.startswith(": "):
                              data = media.tiktok(search)
                              main = data['result']
                              result = flex.tiktok(main)
                              client.sendFlex(to,result)

                      if cmd.startswith(".smule") or cmd.startswith(rname + "smule"):
                          query = cmd.split("smule")[1]
                          if query.startswith("dl: http"):
                              client.sendMessage(to,"Downloading..")
                              data = media.smuledl(link)
                              main = data['result']
                              client.sendAudioWithURL(to,main["mp3Url"])
                              if main["type"] == "video":
                                 client.sendFlexVideo(to,main["mp4Url"],main["thumbnail"])
                          if query.startswith(": "):
                              client.sendMessage(to,"Searching..")
                              data = media.smule(search)
                              main = data['result']
                              result = flex.smule(main)
                              client.sendFlex(to,result)

                      if cmd.startswith(".twitter") or cmd.startswith(rname + "twitter"):
                          query = cmd.split("twitter")[1]
                          if query.startswith("dl: http"):
                              client.sendMessage(to,"Downloading..")
                              data = media.twitterdl(link)
                              result = data['result']['videoUrl']
                              client.sendFlexVideo(to,result,"cyan")    
                          if query.startswith(": "):
                              data = media.twitter(search)
                              main = data['result']
                              result = flex.twitter(main)
                              client.sendFlex(to,result)

                      if cmd.startswith(".facebookdl: http") or cmd.startswith(rname + "facebookdl: http"):
                         data = media.facebookdl(link)
                         main = data["result"]
                         result = flex.facebook(main)
                         client.sendFlex(to,result)
                         client.sendFlexVideo(to,main["videoUrl"],"white")
                      
                      if cmd.startswith(".timeline: http") or cmd.startswith(rname + "timeline: http"):
                          data = media.timeline(link)
                          main = data['result']
                          result = flex.timeline(main)
                          client.sendFlex(to,result)
                          for i in main["timeline"]:
                              if i["type"] == "video":
                                 client.sendFlexVideo(to,i["url"],i["thumbnail"])
                              if i["type"] == "image":
                                 client.sendFlexImage(to,i["url"])

                      if cmd.startswith(".github: ") or cmd.startswith(rname + "github: "):
                          data = media.github(search)
                          main = data['result']
                          result = flex.github(main)
                          client.sendFlex(to,result)

                      if cmd.startswith(".instagram: ") or cmd.startswith(rname + "instagram: "):
                          data = media.instagram(search)
                          main = data['result']
                          result = flex.instagram(main)
                          client.sendFlex(to,result)

                      if cmd.startswith(".instapost: ") or cmd.startswith(rname + "instapost: "):
                          data = media.instapost(link)
                          main = data['result']
                          result = flex.instapost(main)
                          client.sendFlex(to,result)
                          if main["postData"] != []:
                             for i in main["postData"]:
                                 if i["type"] == "image":
                                    client.sendFlexImage(to,i["postUrl"])
                                 if i["type"] == "video":
                                    client.sendFlexVideo(to,i["postUrl"],i["poster"])

                      if cmd.startswith(".instastory: ") or cmd.startswith(rname + "instastory: "):
                         query = search.split(" / ")
                         if len(query) == 2:
                            client.sendMessage(to,"Downloading..")
                            data = media.instastory(query[0])
                            main = data['result']['stories'][int(query[1])-1]
                            result = flex.instastory(data['result'],int(query[1])-1)
                            client.sendFlex(to,result)
                            if main["type"] == "video":
                               client.sendFlexVideo(to,main["url"],main["thumbnail"])
                            if main["type"] == "image":
                               client.sendFlexImage(to,main["url"])
                         if len(query) == 1:
                            client.sendMessage(to,"Invalid commands.")
                            client.sendReplyMessage(ids,to,"「   Example   」\n"+f"{text} / number".capitalize())

                      if cmd.startswith(".bitly: ") or cmd.startswith(rname + "bitly: "):
                         data = media.bitly(link)
                         main = data['result']
                         result = "URL Shortened : {}".format(main)
                         client.sendReplyMessage(ids,to,result)

                      if cmd.startswith(".tinyurl: ") or cmd.startswith(rname + "tinyurl: "):
                         data = media.tinyurl(link)
                         main = data['result']
                         result = "URL Shortened : {}".format(main)
                         client.sendReplyMessage(ids,to,result)

                      if cmd.startswith(".movie: ") or cmd.startswith(rname + "movie: "):
                          data = media.movie(search)
                          main = data['result']
                          result = flex.movie(main)
                          client.sendFlex(to,result)

                      if cmd.startswith(".cinema: ") or cmd.startswith(rname + "cinema: "):
                          client.sendMessage(to,"Searching..")
                          query = search.split(" / ")
                          if len(query) == 1:
                             data = media.cinema(search)
                             main = data['result']
                             result = flex.cinemaSearch(main)
                             client.sendFlex(to,result)
                             client.sendMessage(to,f"{text} / number".capitalize())
                          if len(query) == 2:
                             data = media.cinema(query[0])
                             main = data['result']['data'][int(query[1])-1]
                             result = flex.cinemaInfo(main)
                             client.sendFlex(to,result)
                             client.sendMessage(to,f"{cmd} / number".capitalize())
                          if len(query) == 3:
                             data = media.cinema(query[0])
                             main = data['result']['data'][int(query[1])-1]["nowPlaying"][int(query[2])-1]
                             result = flex.cinemaShow(main)
                             client.sendFlex(to,result)


                      if cmd.startswith(".porn: ") or cmd.startswith(rname + "porn: "):
                          data = media.porn(search)
                          main = data['result']
                          result = flex.porn(main)
                          client.sendFlex(to,result)
                          client.sendFlexVideo(to,main["videoUrl"],main["thumbnail"])


                      if cmd.startswith(".zodiac: ") or cmd.startswith(rname + "zodiac: "):
                         data = media.zodiac(search)
                         main = data['result']
                         result = flex.zodiac(main)
                         client.sendFlex(to,result)

                      if cmd.startswith(".urban: ") or cmd.startswith(rname + "urban: "):
                         data = media.urban(search)
                         main = data['result']
                         result = flex.urban(main)
                         client.sendFlex(to,result)

                      if cmd.startswith(".kbbi: ") or cmd.startswith(rname + "kbbi: "):
                         data = media.kbbi(search)
                         main = data['result']
                         result = flex.kbbi(main,search)
                         client.sendFlex(to,result)

                      if cmd.startswith(".image: ") or cmd.startswith(rname + "image: "):
                         data = media.image(search)
                         main = data['result']
                         result = random.choice(main)
                         client.sendFlexImage(to,result)

                      if cmd.startswith(".cuaca: ") or cmd.startswith(rname + "cuaca: "):
                         data = media.cuaca(search)
                         main = data['result']
                         result = flex.cuaca(main)
                         client.sendFlex(to,result)


                      if cmd.startswith(".playstore: ") or cmd.startswith(rname + "playstore: "):
                         client.sendMessage(to,"Searching..")
                         data = media.playstore(search)
                         main = data['result'][0]
                         result = flex.playstore(main)
                         client.sendFlex(to,result)


                      if cmd.startswith(".cctv") or cmd.startswith(rname + "cctv"):
                         query = text.split("cctv")[1]
                         if query == "":
                            data = media.cctv_code()
                            main = data['result']['active']
                            result = flex.cctvList(main)
                            client.sendFlex(to,result)
                            client.sendMessage(to,f"{text}: code".capitalize())
                         if query.startswith(": "):
                            data = media.cctvSearch(search)
                            main = data['result']
                            result = flex.cctvGet(main)
                            client.sendFlexVideo(to,main['video'],main['thumbnail'])
                            client.sendFlex(to,result)

                      if cmd.startswith(".acaratv") or cmd.startswith(rname + "acaratv"):
                          query = cmd.split("acaratv")[1]
                          if query == "":
                             data = media.acaratv()
                             main = data['result']
                             result = flex.acaratv(main)
                             client.sendFlex(to,result)
                             client.sendMessage(to,f"{cmd}: channel".capitalize())
                          if query.startswith(": "):
                             data = media.acaratv_channel(search)
                             main = data['result']
                             result = flex.channel(main,search)
                             client.sendFlex(to,result)

                      if cmd.startswith(".adzan: ") or cmd.startswith(rname + "adzan: "):
                          data = media.adzan(search)
                          main = data['result']
                          result = flex.adzan(main)
                          client.sendFlex(to,result)

                      if cmd.startswith(".wallpaper: ") or cmd.startswith(rname + "wallpaper: "):
                          data = media.wallpaper(search)
                          main = data['result']
                          result = random.choice(main)
                          client.sendFlexImage(to,result)


                      if cmd.startswith(".screenshot: ") or cmd.startswith(rname + "screenshot: "):
                         que = cmd.split("shot: ")[1]
                         if que.startswith("http"):  
                             query = que
                         else:
                             liq = msg.text.split(": ")[1]
                             query = "http://{}".format(liq)
                         data = media.screenshot(query)
                         main = data['result']
                         client.sendFlexImage(to,main["desktop"])
                         client.sendFlexImage(to,main["mobile"])

                      if cmd.startswith(".resi: ") or cmd.startswith(rname + "resi: "):
                         query = link.split()
                         if len(query) == 1:
                            client.sendMessage(to,"Invalid commands.")
                            client.sendReplyMessage(ids,to,"「   Example   」\n"+f"{rname}resi: ".capitalize()+"JNE JT72907133342")
                         if len(query) == 2:
                            data = media.resi(query[0].lower(),query[1])
                            main = data['result']
                            result = flex.resi(main)
                            client.sendFlex(to,result)

                      if cmd.startswith(".gif: ") or cmd.startswith(rname + "gif: "):
                         data = media.gif(search)
                         main = data['result']
                         result = random.choice(main)
                         client.sendGIFWithURL(to,result)


                      if cmd.startswith(".wikipedia: ") or cmd.startswith(rname + "wikipedia: "):
                         data = media.wikipedia(search)
                         main = data['result']               
                         result = flex.wikipedia(main)
                         client.sendFlex(to,result)

                      if cmd.startswith(".artinama: ") or cmd.startswith(rname + "artinama: "):
                        data = media.nama(search)
                        main = data['result']
                        result = flex.nama(main)
                        client.sendFlex(to,result)

                      if cmd.startswith(".artimimpi: ") or cmd.startswith(rname + "artimimpi: "):
                        data = media.mimpi(search)
                        main = data['result']
                        result = flex.mimpi(main,search)
                        client.sendFlex(to,result)


                      if cmd.startswith(".handphone: ") or cmd.startswith(rname + "handphone: "):
                        query = search.split(" / ")
                        if len(query) == 1:
                           data = media.cellular(search)
                           main = data['result']
                           if len(main) == 1:
                              result = flex.cellularSpecs(main[0])
                           else:result = flex.cellularSearch(main)
                           client.sendFlex(to,result)
                        if len(query) == 2:
                           data = media.cellular(query[0])
                           main = data['result'][int(query[1])-1]
                           result = flex.cellularSpecs(main)
                           client.sendFlex(to,result)


                      if cmd.startswith(".birth: ") or cmd.startswith(rname + "birth: "):
                         data = media.lahir(search)
                         main = data['result']
                         result = flex.lahir(main)
                         client.sendFlex(to,result)


                      if cmd.startswith(".anniv: ") or cmd.startswith(rname + "anniv: "):
                          query = cmd.split("anniv: ")[1]
                          if "-" not in query:client.sendMessage(to,"「   Usage   」\n .anniv: 17-02-2013")
                          else:
                             data = media.jadian(search)
                             main = data['result']
                             result = flex.jadian(main)
                             client.sendFlex(to,result)


                      if cmd.startswith(".manga: ") or cmd.startswith(rname + "manga: "):
                         chapter = link.split(" / ")
                         if len(chapter) == 1:
                            data = media.mangaSearch(search)
                            main = data['result']
                            result = flex.manga(main)
                            client.sendFlex(to,result[0])
                            client.sendFlex(to,result[1])
                            client.sendMessage(to,f"{text} / number".capitalize())
                         if len(chapter) == 2:
                            query = int(chapter[1]-1)
                            data = media.mangaSearch(chapter[0])
                            main = data['result']['manga'][query]
                            wibu = media.mangaChapter(main["id"])
                            client.sendMessage(to,wibu["title"])
                            for img in wibu["manga"]:
                                client.sendImageWithURL(to,img)


                      if cmd == ".imagelink" or cmd == rname + "imagelink":
                          read["imgurl"][to] = True
                          client.sendReplyMessage(ids,to,"Send an image.")

                      if cmd == ".covid19" or cmd == rname + "covid19":
                          data = media.corona()
                          main = data['result']
                          result = flex.corona(main)
                          client.sendFlex(to,result)

                      if cmd == ".kamasutra" or cmd == rname + "kamasutra":
                         data = media.kamasutra()
                         main = data['result']
                         result = flex.kamasutra(main)
                         client.sendFlex(to,result)


                      if cmd == ".bmkg" or cmd == rname + "bmkg":
                         data = media.bmkg()
                         main = data['result']
                         result = flex.bmkg(main)
                         client.sendFlex(to,result)


                      if cmd == ".topnews" or cmd == rname + "topnews":
                         data = media.topnews()
                         main = data['result']
                         result = flex.topnews(main)
                         client.sendFlex(to,result)

                      if cmd == ".pornstar" or cmd == rname + "pornstar":
                         data = media.pornstar()
                         main = random.choice(data['result'])
                         result = flex.pornstar(main)
                         client.sendFlex(to,result)
                         client.sendFlexImage(to,main["image"])


                      if cmd == ".quotes" or cmd == rname + "quotes":
                         data = media.movie_quotes()
                         main = data['result']
                         result = flex.quotes(main)
                         client.sendFlex(to,result)


                      if cmd == ".hentai" or cmd == rname + ".hentai":
                         data = media.hentai()
                         main = data['result']
                         result = random.choice(main)
                         client.sendFlexImage(to,result)

                      if cmd.startswith(".karir") or cmd.startswith(rname + "karir"):
                          query = text.split("karir")[1]
                          if query == "":
                             data = media.karir()
                             main = data['result']
                             result = flex.karir(main)
                             client.sendFlex(to,result)
                             client.sendMessage(to,f"{text}: number".capitalize())
                          if query.startswith(": "):
                             data = media.karir()
                             main = data['result'][int(search)-1]
                             result = flex.karirInfo(main)
                             client.sendFlex(to,result)

                      if cmd.startswith(".trans-en: ") or cmd.startswith(rname + "trans-en: "):
                          data = media.translate("en",link)
                          main = data['result']['translate']
                          client.sendReplyMessage(ids,to,f"「   IND - ENG   」\n{main}")

                      if cmd.startswith(".trans-id: ") or cmd.startswith(rname + "trans-id: "):
                         data = media.translate("id",link)
                         main = data['result']['translate']
                         client.sendReplyMessage(ids,to,f"「   ENG - IND   」\n{main}")


                      if cmd.startswith(".fancy: ") or cmd.startswith(rname + "fancy: "):
                          url = f"{host}/fancy?text={link}"
                          head = {"User-Agent": "JustGood/0.5"}
                          data = json.loads(requests.get(url,headers=head).text)
                          main = ""
                          for s in data["result"]:
                              main += "\n{}\n".format(s)
                          client.sendFlexText(to,main[1:])


                      if cmd.startswith(".customlink: ") or cmd.startswith(rname + "customlink: "):
                          query = link.split()
                          if len(query) == 2:
                             url = f"{host}/custom/make"
                             headers = {"label": query[0], "url": query[1],"User-Agent":"JustGood/0.5"}
                             data = json.loads(requests.get(url, headers=headers).text)
                             main = data["result"]
                             result = "URL Shortened : {}".format(main)
                             client.sendReplyMessage(ids,to,result)

                      if cmd.startswith(".checkip: ") or cmd.startswith(rname + "checkip: "):
                          url = f"{host}/ip={link}"
                          head = {"User-Agent": "JustGood/0.5"}
                          data = json.loads(requests.get(url,headers=head).text)
                          main = data['result']
                          result = flex.checkIP(main)
                          client.sendFlex(to,result)

                      if cmd == ".header?" or cmd == rname + "header?":
                          client.sendMessage(to,"loading..")
                          url = f"{host}/line"
                          head = {"User-Agent": "JustGood/0.5"}
                          data = json.loads(requests.get(url,headers=head).text)
                          main = data['result']
                          result = flex.linever(main)
                          client.sendFlex(to,result)


                      if cmd.startswith(".dick ") or cmd.startswith(rname + "dick "):
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                            mention = eval(msg.contentMetadata['MENTION'])
                            users = mention['MENTIONEES'][0]['M']
                            if users != mid:
                                names = f"dick {client.getContact(users).displayName}"
                                data = media.dick()
                                main = data['result']
                                result = flex.dick(main,names)
                                client.sendFlex(to,result)

                      if cmd.startswith(".tits ") or cmd.startswith(rname + "tits "):
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                            mention = eval(msg.contentMetadata['MENTION'])
                            users = mention['MENTIONEES'][0]['M']
                            if users != mid:
                                names = f"tits {client.getContact(users).displayName}"
                                data = media.tits()
                                main = data['result']
                                result = flex.tits(main,names)
                                client.sendFlex(to,result)

                      if cmd.startswith(".vagina ") or cmd.startswith(rname + "vagina "):
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                            mention = eval(msg.contentMetadata['MENTION'])
                            users = mention['MENTIONEES'][0]['M']
                            if users != mid:
                                names = f"vagina {client.getContact(users).displayName}"
                                data = media.vagina()
                                main = data['result']
                                result = flex.vagina(main,names)
                                client.sendFlex(to,result)

                      if cmd.startswith(".meme") or cmd.startswith(rname + "meme"):
                          if cmd.split("meme")[1] == "":client.sendReplyMessage(ids,to,"「   Usage   」\n.meme @Tag / Text1 - Text2")
                          else:
                            text = cmd.split("/ ")[1].split(" - ")[0]
                            text2 = cmd.split("- ")[1]
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                               names = re.findall(r'@(\w+)', cmd)
                               mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                               mentionees = mention['MENTIONEES']
                               for mention in mentionees:
                                   if mention["M"] != mid:
                                      imageurl = "{}{}".format(oburl,client.getContact(mention['M']).pictureStatus)
                                      meme = media.meme(text,text2,imageurl)
                                      data = meme['result']
                                      client.sendFlexImage(msg.to,data)               

                   ''' ** METADATA AND CONTENT TYPE FUNCTION ** '''

                   if msg.contentType == 13:
                      target = msg.contentMetadata["mid"]
                      if read["addwhitelist"]:                      
                          if target != mid and target in setting["whitelist"]:
                              client.sendReplyMessage(msg.to,"Already in whitelist")
                              read["addwhitelist"] = False
                          else:
                             if target not in setting["blacklist"]:
                                setting["whitelist"].append(target)
                                with open('Data/settings.json', 'w') as fp:
                                   json.dump(setting, fp, sort_keys=True, indent=4)
                                client.sendMention(msg.to,"@!  added in whitelist.",[target])
                                read["addwhitelist"] = False                              
                             else:
                                client.sendMention(msg.to,"[Failed!]\n@! in blacklist.",[target])
                                read["addwhitelist"] = False 

                      if read["delwhitelist"]:
                          if target != mid and target in setting["whitelist"]:
                             setting["whitelist"].remove(target)
                             with open('Data/settings.json', 'w') as fp:
                                 json.dump(setting, fp, sort_keys=True, indent=4)
                             client.sendMention(msg.to,"@!  removed from whitelist.",[target])
                             read["delwhitelist"] = False
                          else:
                              client.sendMention(msg.to,"[Failed]\n@! not in whitelist.",[target])
                              read["delwhitelist"] = False      

                      if read["addblacklist"]:                      
                          if target != mid and target in setting["blacklist"]:
                              client.sendReplyMessage(msg.to,"Already in blacklist")
                              read["addblacklist"] = False
                          else:
                             if target not in setting["whitelist"]:
                                setting["blacklist"].append(target)
                                with open('Data/settings.json', 'w') as fp:
                                   json.dump(setting, fp, sort_keys=True, indent=4)
                                client.sendMention(msg.to,"@!  added in  blacklist.",[target])
                                read["addblacklist"] = False                              
                             else:
                                client.sendMention(msg.to,"[Failed!]\n@!  in whitelist.",[target])
                                read["addblacklist"] = False 

                      if read["delblacklist"]:
                          if target != mid and target in setting["blacklist"]:
                             setting["blacklist"].remove(target)
                             with open('Data/settings.json', 'w') as fp:
                                 json.dump(setting, fp, sort_keys=True, indent=4)
                             client.sendMention(msg.to,"@!  removed from blacklist.",[target])
                             read["delblacklist"] = False
                          else:
                              client.sendMention(msg.to,"[Failed]\n@!  not in blacklist.",[target])
                              read["delblacklist"] = False      
                   
                   if msg.contentType == 2:
                      if read['dual']:
                         try:
                            client.downloadObjectMsg(msg.id,'path','video.mp4')
                            client.sendMessage(msg.to, "Send picture to be profiled")
                            read['dual']= False
                            read['dual2']=True
                         except:
                            read['dual']= True
                            client.sendMessage(msg.to, "「  Failed  」\nPlease resend your video.")

                   if msg.contentType == 1:
                      if msg.to in read["imgurl"]:
                           del read["imgurl"][msg.to]
                           try:
                               path = client.downloadObjectMsg(ids)
                               data = media.imgurl(path)
                               main = data['result']
                               result = f"Image was converted :\n{main}"
                               client.sendReplyMessage(ids,to,result)
                           except Exception as e:
                               client.sendReplyMessage(ids,to,f"ERROR : {e}")

                      if read['dual2']:
                         client.downloadObjectMsg(msg.id,'path','foto.jpg')
                         client.updateProfileVideoPicture('video.mp4','foto.jpg')
                         client.sendMessage(msg.to, 'Success change profile video.')
                         client.deleteFile('path')
                         read['dual2']=False

                      if read["pp"]:
                         path = client.downloadObjectMsg(msg.id)
                         read["pp"] = False
                         client.updateProfilePicture(path)
                         client.deleteFile(path)
                         client.sendMessage(msg.to, "Profile image updated.")                                             

                      if msg.to in read["gpict"]:
                         path = client.downloadObjectMsg(msg.id)
                         del read["gpict"][msg.to]
                         client.updateGroupPicture(msg.to, path)
                         client.deleteFile(path)
                         client.sendMessage(msg.to, "Group image updated.")

            except Exception as error:
                ERROR = flex.ERROR(f"{error}")
                client.sendFlex(to,ERROR)
                traceback.print_tb(error.__traceback__)


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def liff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {'on': ['P','CM'],'off': []}
    headers = {'X-Line-Access': client.authToken ,'X-Line-Application': client.server.APP_NAME,'X-Line-ChannelId': '1602876096','Content-Type': 'application/json'}
    requests.post(url, json=data, headers=headers)


def prostaff(op):      
     try:
       if op.param3 in setting["whitelist"]:
           if op.param2 not in setting["whitelist"]:
              client.kickoutFromGroup(op.param1,[op.param2])
              client.findAndAddContactsByMid(op.param3)
              client.inviteIntoGroup(op.param1,[op.param3])               
              if op.param2 not in setting["blacklist"]:
                 setting["blacklist"].append(op.param2)
                 with open('Data/settings.json', 'w') as fp:
                   json.dump(setting, fp, sort_keys=True, indent=4)
     except Exception as error:print(error)

def promax(op):
    try:
       if op.param2 not in setting["whitelist"]:
          client.kickoutFromGroup(op.param1,[op.param2])
          client.findAndAddContactsByMid(op.param3)
          client.inviteIntoGroup(op.param1,[op.param3])
          if op.param2 not in setting["blacklist"]:
             setting["blacklist"].append(op.param2)
             with open('Data/settings.json', 'w') as fp:
               json.dump(setting, fp, sort_keys=True, indent=4)
    except Exception as e:print(e)

def proinvite(op):
     try:
       if op.param2 not in setting["whitelist"]:
           try:client.kickoutFromGroup(op.param1,[op.param2])                                         
           except:pass
           mbul = client.getGroup(op.param1)
           no = 0
           for a in mbul.invitee:
               if a.mid in op.param3:
                   if no > 10:pass
                   else:
                      try:
                        no = (no+1)
                        client.cancelGroupInvitation(op.param1,[a.mid])
                        time.sleep(0.04)
                      except:pass
           for b in mbul.members:
               if b.mid in op.param3:
                   try:client.kickoutFromGroup(op.param1,[b.mid])
                   except:pass
           if op.param2 not in setting["blacklist"]:
              setting["blacklist"].append(op.param2)
              with open('Data/settings.json', 'w') as fp:
                json.dump(setting, fp, sort_keys=True, indent=4)
       else:
           mbul = client.getGroup(op.param1)
           for a in mbul.invitee:
               if a.mid in op.param3:
                   if a.mid in setting["blacklist"]:
                      try:
                         client.cancelGroupInvitation(op.param1,[a.mid])
                         client.sendMessage(msg.to,"Caution!, user in blacklist")
                      except:pass
                   else:pass
           for b in mbul.members:
               if b.mid in op.param3:
                   if b.mid in setting["blacklist"]:
                       try:client.kickoutFromGroup(op.param1,[b.mid])
                       except:pass
     except Exception as e:print(e)

def kekick(op):
       if op.param2 not in setting["whitelist"]:
          if op.param2 not in setting["blacklist"]:
             setting["blacklist"].append(op.param2)
             with open('Data/settings.json', 'w') as fp:
               json.dump(setting, fp, sort_keys=True, indent=4) 

while True:
    try:
        ops = clPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clPoll.setRevision(op.revision)
                t1 = Thread(target=Oup(op,))
                t1.start()
                t1.join()
    except Exception as error:
        client.log("「   ERROR 」\n{}".format(str(error)))
        traceback.print_tb(error.__traceback__)
