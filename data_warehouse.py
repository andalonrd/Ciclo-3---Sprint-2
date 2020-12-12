class Document:

# Made by Andres Alonso Rodríghez PhD, 12/12/2020
# This is a class to represent documents in a file management system. It also offers basic functionality to store files 
# within a repository
# documents will be stored according to following folder scheme : root/warehouse/userId/
# where root is the folder where the application #is being kept    

    def __init__(self,Access,name):
        #input parameters:
        #Access: is an access objects that represents the owner of the file
        #name: file's name. 

        # imports functions from the database management tool 
        from DbPeek import query  
        from DbPeek import date_from_db 
        from datetime import date

        self.db = "data_warehouse"
        sql = "select * from " + self.db + " where ( owner = " + str(Access.getId()) + " and name = '" + name + "' and status = 1 );"
        
        # check to see if the file to be created is already in the files database
        found = query(sql)
    
        #if it doesn't exists, creates a basic object to be filled latter
        if found[1] == "Success" :
            if len(found[0]) == 0 :
                with open("nFile.txt","r") as f:
                    self.id = int(f.read()) + 1
                self.name = name
                self.owner = Access.getId()
                self.in_date = date.today()
                self.status = 1
                self.exp_date = date(2000,1,1)
                self.solved = 0
                with open("nFile.txt","w") as f:
                    f.write(str(self.id))

        #if the document is already in the document database, creates it representing object by retrieving data from the 
        #database
            else:
                self.id = found[0][0]
                self.name = found[0][1]
                self.owner = found[0][2]
                self.in_date = date_from_db(found[0][3])
                self.status = 1
                self.exp_date = date_from_db(found[0][5])
                self.solved = date_from_db(found[0][6])
        else:
            print("Db or Query Failure")
            raise SystemExit 
    
    # stuff to do if a file becomes expired
    def expired(self):
        from datetime import date
        import os 
        from DbPeek import do_in_db
        if self.exp_date >  date.today():
            exp_date_s = str(self.exp_date)
            sql = "update " + self.db + " set exp_date = " + exp_date_s + " where id = " + str(self.id) + ";"  
            do_in_db(sql)
            self.status = 0 
            if os.path.exists(".\\warehouse\\" + self.owner + "\\" + self.name) :
                os.remove(".\\warehouse\\" + self.owner + "\\" + self.name)
            return "file expired"


        else: 
            self.status = 1
            return "file is still valid"
    
    #picks up a file from the given path and stores in the dataWarehouse 
    def retrieve(self,path):
        from shutil import copy
        if self.status == 1:
            copy(".\\warehouse\\" + str(self.owner)+ "\\" + self.name,path)
            return "File " + self.name + " was retrieved"
        else: return "File not found"

    #puts a file in the dataWarehouse. It looks for the file in path and sets a time span before expiration
    def store(self,path,span):
        from DbPeek import do_in_db
        import os
        from shutil import copy
        from datetime import timedelta 
        self.exp_date = self.in_date + timedelta(days = span) 
        in_date_s = str(self.in_date)
        exp_date_s = str(self.exp_date)
        sql = "insert into "+ self.db +" values (" + str(self.id) + "," + str(self.owner) + ",'" + self.name + "','" + in_date_s + "','" + exp_date_s + "'," + str(self.status) + "," + str(self.solved)+");"
        sqlout = do_in_db(sql)
        if sqlout != "Success":
            raise SystemExit
        end_path = ".\\warehouse\\" + str(self.owner)
        if os.path.exists(end_path):
            copy(path,end_path + "\\" + self.name) 
        else: 
            os.makedirs(end_path)
            copy(path + self.name,end_path) 
        return "file stored"

    # increases the lifespan of the document by more_span time in days
    def update_exp_date (self,more_span):
        from DbPeek import do_in_db
        from datetime import timedelta 
        self.exp_date += more_span
        exp_date_s = str(self.exp_date) +timedelta(days=more_span)
        sql = "update " + self.db + " set exp_date = " + exp_date_s + " where id = " + str(self.id) + ";" 
        do_in_db(sql)

    def solved (self):
        from DbPeek import do_in_db
        self.solved = 1
        sql =  "update " + self.db + " set solved = " + str(self.solved) + " where id = " + str(self.id) + ";"
        do_in_db(sql) 
    
# this is a set of implementations done to set up the document system. they should be commented in the final version. 
#table="data_warehouse"
#headings = ["id","owner","name","in_date","exp_date","status","solved"]
#types = ["int","int","varchar(25)","varchar(12)","varchar(12)","int","int"]
#from DbPeek import create_table
#from Access import Access 
#a = create_table(table,headings,types)
#b = Access("MarkT","KittyA","A")
#print (b.getId())
#c = Document(b,"Memorando.docx")
#inpath = "C:\\Users\\Andres Alonso\\Desktop\\OnGoing\\MinTic 2020\\Software Development\\Documents\\"
#d = c.store(inpath,15)
#outpath = "C:\\Users\\Andres Alonso\\Desktop"
#e = c.retrieve(outpath)       
#print(d)
#print(e)

#Note : THE EXPIRE OPTIONS HAVEN'T YET BEEN TESTED (taking as reference the postmark date on top of this file)
    










