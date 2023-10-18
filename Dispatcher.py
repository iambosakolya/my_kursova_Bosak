from System_user import SystemUser

class Dispatcher(SystemUser):
    def __init__(self, firm_name, address, phone_number, pib, experience):
        super().__init__(firm_name, address, pib, phone_number)
        self.contract = Contract
        self.experience = experience

    def set_experience(self, experience):
        self.experience = experience

    def get_experience(self):
        return self.experience

    # Унаслідовані віртуальні методи від SystemUser
    def log_in(self):
        print(f"You {self.pib} entered to the system as a dispatcher.")

    def log_out(self):
        print(f"You {self.pib} logged out the system as a dispatcher.")
