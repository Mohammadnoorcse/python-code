class person:
    def __init__(self,person_name: str,year_of_birth: int,ht_inches: int = None):
        self.__name = person_name
        self.__date_of_birth = year_of_birth
        self.__height = ht_inches
    
    def get_year_of_birth(self):
        return self.__date_of_birth
    
    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        if self.__has_any_number(new_name):
            print("Sorry person name can't have number")
        self.__name = new_name
        
        
    
    def __has_any_number(self,string):
        return "0" in string
    
    
    def get_summarY(self):
        return f"Name: {self.__name}, DOB: {self.__date_of_birth}, Height: {self.__height}"
    
        


# a_person = person("Aminur")
# b_person = person("Robot")
# print(a_person.get_name())
# print(b_person.get_name())

# a_person = person("Aminur",1980,6 )
# print(a_person.get_summarY())
# a_person.set_name("Aminur islam")
# print(a_person.get_summarY())
# a_person.set_name("0Aminur")
# print(a_person.get_name())

# person_list = []
# person_list.append(person("Zulkarnine",1990,72))
# person_list.append(person("Foo",1980))
# person_list.append(person("Bar",1993,65))
# person_list.append(person("Baz",2020,80))
# person_list.append(person("Ban",1945))
# person_list.append(person("Ben",1900,72))

# for p in person_list:
#     if p.get_year_of_birth()>=1990:
#         print(p.get_summarY())


class student (person):
    def __init__(self, person_name: str, year_of_birth: int, ht_inches: int = None,email_id:str,student_id:str):
        super().__init__(person_name, year_of_birth, ht_inches)
        self.id = student_id
        self.email = email_id
    
    def get_summarY(self):
        return f"Name: {self.get_name} Email: {self.email}"