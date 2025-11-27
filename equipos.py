class Equipment:
    __max_id:int = 0

    @classmethod
    def set_max_id(cls, id):
        cls.__max_id = id
    
    def __init__(self, name, category, actual_state = "available", registration_date = "xx/xx/xxxx", id = -1):
        self.name = name
        self.category = category
        self.actual_state = actual_state
        self.registration_date= registration_date
        self.id = id if id!=-1 else Equipment.__max_id
        if Equipment.__max_id <= self.id:
            Equipment.__max_id = self.id+1
    
    def lend_equipment(self)->bool:
        if self.actual_state == "available":
            self.actual_state = "borrowed"
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
    def repair_equipment(self, date_return):
        pass
