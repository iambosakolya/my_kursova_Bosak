from System_user import SystemUser

class Client(SystemUser):
    def __init__(self, firm_name, address, phone_number, pib):
        super().__init__(firm_name, address, phone_number, pib)
        self.contracts = {}

    # унаслідовані віртуальні методи від SystemUser

    def log_in(self):
        print(f"You entered the system as a client.")

    def log_out(self):
        print(f"You logged out of the system as a client.")




