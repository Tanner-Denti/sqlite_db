class Timesheet:
    def __init__(self, time_id, representative_id, customer_id, project_id, clock_in, clock_out):
        self.time_id = time_id
        self.representative_id = representative_id
        self.customer_id = customer_id
        self.project_id = project_id
        self.clock_in = clock_in
        self.clock_out = clock_out
    
    @property
    def session_time(self):
        return f'{self.clock_out - self.clock_in}'