class Contract:
    def __init__(self, contract_id, dep_st, arr_st, insurance_sum, cargo_type, delivery_time, weight, date, cost):
        self.contract_id = contract_id
        self.dep_st = dep_st
        self.arr_st = arr_st
        self.insurance_sum = insurance_sum
        self.cargo_type = cargo_type
        self.delivery_time = delivery_time
        self.weight = weight
        self.date = date
        self.cost = cost

    def set_insurance_sum(self, insurance_sum):
        self.insurance_sum = insurance_sum

    def get_insurance_sum(self):
        return self.insurance_sum

    def set_cargo_type(self, cargo_type):
        self.cargo_type = cargo_type

    def get_cargo_type(self):
        return self.cargo_type

    def set_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time

    def get_delivery_time(self):
        return self.delivery_time

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_contract_id(self, contract_id):
        self.contract_id = contract_id

    def get_contract_id(self):
        return self.contract_id
