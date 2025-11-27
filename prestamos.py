from usuarios import User; from equipos import Equipment; from reportes import reports_and_time;
class Borrow:
    __borrow_record = []
    
    def __init__(self, equipment: Equipment, user:User):
        self.equipment = equipment
        self.user = user

    @classmethod
    def calculateBorrowTime(cls, user:User, equipment:Equipment):
        pass