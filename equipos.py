from usuarios import user
class equipment:
    max_id:int = 0
    user_in_posesion : user

    def __init__(self, name, category, actual_state = "available", registration_date = "xx/xx/xxxx", id = -1):
        self.name = name
        self.category = category
        self.actual_state = actual_state
        self.registration_date= registration_date
        self.id = id if id!=-1 else equipment.max_id
        if equipment.max_id <= self.id:
            equipment.max_id = self.id+1
            
    def lend_equipment(self, user:user)->bool:
        if self.actual_state == "available":
            self.actual_state = "borrowed"
            self.user_in_posesion = user
            return True
        else:
            print(f"The equipment can't be lend, since is {self.actual_state}")
            return False
    def return_equipment(self, state)->bool:
        if self.actual_state == "borrowed":
            self.actual_state = state
            if state == "damaged":
                return True
            else:
                self.user_in_posesion = None
                return True
        return False
    
