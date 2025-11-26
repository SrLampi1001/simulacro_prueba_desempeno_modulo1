import os
import csv
from equipos import equipment
class user:
    users_path = os.path.normpath("csv_archives"+ os.path.pathsep+"users.csv")
    criptid = ["_","a","6","d","m","7","h","ñ","8","e","i","l","2","j","c","f","v","4","g","b","9","n","y","k","$","5","q","t","r","x","o","1","s","p","u","0","z","3"]
    equipment_in_posesion : list[equipment] #Only accepts list of equipment class objects
    
    def __init__(self, user, password, rol, email = ""):
        self.user = user
        self.password = self.encryptPassword(password) #Encrypts password
        self.email = email
        self.rol = rol
    
    def isAdmin(self):
        if self.rol == "admin":
            return True
        return False
    def get_user(self):
        return [self.user, self.password, self.rol, self.email]
    def get_rol(self):
        return self.rol
    def get_email(self):
        if self.email=="":
            return None
        return self.email
    def save_user(self): 
        dir  = os.path.dirname(self.users_path)
        if not os.path.exists(dir):
            self.create_directory(dir)
        with open(self.users_path, "a") as users:
            writer = csv.writer(users)
            writer.writerow(self.get_user())        
    def create_directory(self, dir):        
        try:
            os.mkdir(dir)
            with open(self.users_path, "w") as users:
                writer = csv.writer(users)
                writer.writerow(["user", "password", "rol", "email"])
        except Exception as ex:
            print(f"Error, exception: {ex} creating the {dir} directory to save users")
    def encryptPassword(self):
        """
        Encrypts the password with a handmade method
        returns the encrypted password
        """
        encrypted = ""
        new_indexation = lambda x: (x*2)-38
        for ch in self.password:
            if ch in self.criptid:
                i = self.criptid.index(ch)
                encrypted += self.criptid[new_indexation(i)]
            else:
                encrypted += "*/-"
        return encrypted
    def return_equipment(self, name, status)->bool:
        valid_status = ["available", "damaged"]
        if status not in valid_status:
            print(f"Error, {status} is not a valid status to return a equipment, only available or damaged")
            return False
        if len(self.equipment_in_posesion)==0:
            return False
        for equipment in self.equipment_in_posesion:
            if equipment.name == name:
                equipment.return_equipment()
                return True
        return False
