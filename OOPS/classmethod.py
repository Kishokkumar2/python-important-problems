class Company:

    # class variable
    Company_name="ZOHO"    
    def __init__(self,name=Company_name):
        self.name=name
        


    # class method is sused to update class variable
    @classmethod
    def change_company_name(cls,new_name):
        cls.Company_name=new_name
        print("new company name",cls.Company_name)


com=Company()
print("old",com.name)
com.change_company_name("wIbro")


