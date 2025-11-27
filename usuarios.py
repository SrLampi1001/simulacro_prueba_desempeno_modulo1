import os
import csv
from equipos import Equipment
class User:
    __are_admins = False
    __criptid = ["_","a","6","d","m","7","h","ñ","8","e","i","l","2","j","c","f","v","4","g","b","9","n","y","k","$","5","q","t","r","x","o","1","s","p","u","0","z","3"]
    __users = {} #Dictionay to easy user validation
    users_path = os.path.normpath("csv_archives"+ os.path.pathsep+"users.csv")
    equipment_in_posesion : list[Equipment] #Shoul be a list of Equipments
    
    def __init__(self, user, password, rol, email): #The constructor MUST NOT be called directly to create users
        """
        Constructor
        """
        self.user = user
        self.password = password #Encrypts password
        self.email = email
        self.rol = rol
    
    @classmethod
    def create(cls, user, password, rol, email = ""):
        """
        Class method for creation of users
        Use instead of normal constructor
        Makes verifications, allow user creation if passes all verifications
        Else returns None
        """
        if user in cls.__users: #usernames must be unique (As there no ID)
            print("UserName not avaible, try another")
            return None
        elif password=="":
            print("The password cannot be empty")
            return None
        elif rol=="admin" and cls.__are_admins == False:
            cls.__are_admins = True  #Makes sure to change the User class attribute and not the instance
            return cls(user, cls.encryptPassword(password), rol, email)
        elif rol == "admin" and cls.__are_admins == True:
            print("There is already an admin user, cannot create more")
            return None
        elif rol not in ["Student", "Instructor", "Administrator"]:
            print("Invalid rol, only student, instructor or admin are valid")
            return None
        else:
            return cls(user, cls.encryptPassword(password), rol, email) #returns the construction of the object

    @classmethod
    def encryptPassword(cls, password):
        """
        Encrypts the password with a handmade method
        returns the encrypted password
        """
        encrypted = ""
        new_indexation = lambda x: (x*2)-38
        for ch in password:
            if ch in cls.__criptid:
                i = cls.__criptid.index(ch)
                encrypted += cls.__criptid[new_indexation(i)]
            else:
                encrypted += "*/-"
        return encrypted
    @classmethod
    def login(cls, user, password, tr = 1):
        """
        Classmethod to login as an user
        Verifies if user exist on memory
        returns tuple user, true if login succesfull
        if login unsuccesfull makes a callback to itself, up to 3 times
        if user does not exist or the 3 times are up, returns tuple None, False
        """
        encripted = cls.encryptPassword(password)
        if tr == 4:
            return None, False
        if user in cls.__users:
            if cls.__users == encripted:
                print("Login succesfull")
                return user, True
            else:
                return cls.login(user, password, tr+1)
        else:
            print("No such user in the database")
            return None, False
        
    def save_user(self): 
        """
        Only saves the user on the csv archive
        UPDATE EXPECTED:
        verifies userName and updates the specific row on csv (Prevents duplicate users)
        """
        dir  = os.path.dirname(self.users_path)
        if not os.path.exists(dir):
            self.create_directory(dir)
        with open(self.users_path, "a") as users:
            writer = csv.writer(users)
            writer.writerow(self.get_user())
    
    def isAdmin(self):
        """
        Simple method to verify admin status
        """
        if self.rol == "admin":
            return True
        return False
    
    def get_user(self):
        """
        user getter
        returns list with all user parameters
        """
        return [self.user, self.password, self.rol, self.email]
    
    def get_rol(self):
        """
        rol getter
        returns user's rol
        """
        return self.rol
    
    def get_email(self):
        """
        email getter
        returns user's email
        """
        if self.email=="":
            return None
        return self.email
    
    def create_directory(self, dir):
        """
        Creates the directory for the csv storing
        Creates the csv archive on the path and creates the header row
        """
        try:
            os.mkdir(dir)
            with open(self.users_path, "w") as users:
                writer = csv.writer(users)
                writer.writerow(["user", "password", "rol", "email"])
        except Exception as ex:
            print(f"Error, exception: {ex} creating the {dir} directory to save users")
        
    def return_equipment(self, equipment_id, status)->bool:
        """
        receives status parameter from the user (Damaged or invalid)
        Receives equipment id to return
        Return True if equipment is returned, else False
        """
        valid_status = ["available", "damaged"]
        if status not in valid_status:
            print(f"Error, {status} is not a valid status to return a equipment, only available or damaged")
            return False
        if len(self.equipment_in_posesion)==0:
            return False
        for equipment in self.equipment_in_posesion:
            if equipment.id == equipment_id:
                equipment.return_equipment()
                return True
        return False
    