class Representative:
    def __init__(self, representative_id, first_name, last_name, rank, wage, street_address, city, state):

        self.representative_id = representative_id
        self.first_name = first_name
        self.last_name = last_name
        self.rank = rank
        self.wage = wage
        self.street_address = street_address
        self.city = city
        self.state = state

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@rgblandscapedesigns.com'
    
    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def full_address(self):
        return f'{self.street_address} {self.city}, {self.state}'
