from abc import ABC, abstractmethod

class SystemUser(ABC):
    def __init__(self, firm_name, address, phone_number, pib):
        self.firm_name = firm_name
        self.address = address
        self.phone_number = phone_number
        self.pib = pib

    def set_firm_name(self, firm_name):
        self.firm_name = firm_name

    def get_firm_name(self):
        return self.firm_name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_pib(self, pib):
        self.pib = pib

    def get_pib(self):
        return self.pib

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    @abstractmethod
    def log_in(self):
        pass

    @abstractmethod
    def log_out(self):
        pass