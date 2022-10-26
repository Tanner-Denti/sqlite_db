class Project:
    def __init__(self, project_id, representative_id, customer_id, homeowner, street_address, city, state, hours_worked):
        self.project_id = project_id
        self.representative_id = representative_id
        self.customer_id = customer_id
        self.homeowner = homeowner
        self.street_address = street_address
        self.city = city
        self.state = state
        self.hours_worked = hours_worked
    
    @property
    def full_address(self):
        return f'{self.street_address} {self.city}, {self.state}'
       