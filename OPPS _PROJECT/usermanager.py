from register import User
class Usermanager:

    __USERS=[]
    @classmethod
    def adduser(cls,user):

        if isinstance(user,User):
           cls.__USERS.append(user)
        else:
            print("Invalid User")
    


    @classmethod 
    def finduser(cls,email,password):
        for user in cls.__USERS:
            if user.email == email and user.password==password:
                return user
            else:
                return None
            
            

