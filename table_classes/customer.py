
class Customer:
    def __init__(self, customer_id, first_name, last_name, pay_rate, city, state):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.pay_rate = pay_rate
        self.city = city
        self.state = state
        
    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'