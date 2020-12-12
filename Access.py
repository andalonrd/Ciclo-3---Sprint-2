#Made by Andrés Alonso PhD, Update 12/12/2020
#this file has the definiton of the Access class, which encapsulates any tryout to access the data management system
# it initialises with custom values particulary self.access has been made to be equal 0 denoting that the object, 
# wouldn't be accepted into the system upon creation

class Access:

    def __init__(self,login, password,kind) :
        with open('nPassword.txt','r') as f:
            self.id = int(f.read())+1
        self.login = login 
        self.password = password 
        self.kind = kind
        self.table = "access_control"
        self.access = 0
        with open('nPassword.txt','w') as f:
            f.write(str(self.id))
    
    def check_access(self):
        # this just provides access to the self.access property
        return self.access

    def getId(self):
        # this just provides access to the self.id property
        return self.id    

    def grant_access(self) : 
        # this allows access into the data management system. it checks if the user is within the access database and if one of multiple records are found, 
        # then permits entrance. at the end changes the status of self.access to 1 to indicate that the user has been checked and then granted entrance 
        from DbPeek import query
        sql = "select * from " + self.table + " where ( login = '" + self.login + "' and  password = '" + self.password + "');"
        lock = query(sql)
        if lock[1] == "failure" : 
            return "database error"
        elif len(lock[0]) == 0 :
            return "access denied"
        else:
            self.access = 1
            return "access granted" 
    
    def add(self):
        # this adds the visitor to the user's database
        from DbPeek import do_in_db
        sql = "insert into " + self.table + " values (" + str(self.id) + ",'" + self.login + "','" + self.password + "'," + str(self.kind) + ");"
        flag = do_in_db(sql)
        if flag == "Success" : 
            return "New user added"
        else :
            return "Failure"

#hds = ["id","login","password","kind",]
#tps = ["int","varchar(10)","varchar(10)","int"]
#from DbPeek import create_table
#create_table("access_control",hds,tps) 
#A = Access("MarkT","KittyA",1)
#B = Access("JuneB", "Peachy22",0)
#C = Access("JessieK","Twinkle",0)
#D = Access("MarieH", "Trashy",0)   
#E = Access("Teenie", "Wiggly",0) 
#print(A.add())
#print(B.add())
#print(C.add())
#print(D.add())
#print(A.grant_access())
#print(D.grant_access())
#print(E.grant_access())
#print(D.access)
#print(C.access)




