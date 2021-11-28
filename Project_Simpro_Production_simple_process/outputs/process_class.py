import simpy

class process_definition():

    def __init__(self,env):
        self.env = env
        self.log_list = []
        
        self.register_request_resource = simpy.Resource(env, capacity = 1)
        
        self.examine_casually_resource = simpy.Resource(env, capacity = 1)
        
        self.check_ticket_resource = simpy.Resource(env, capacity = 1)
        
        self.decide_resource = simpy.Resource(env, capacity = 1)
        
        self.reinitiate_request_resource = simpy.Resource(env, capacity = 1)
        
        self.examine_thoroughly_resource = simpy.Resource(env, capacity = 1)
        
        self.pay_compensation_resource = simpy.Resource(env, capacity = 1)
        
        self.reject_request_resource = simpy.Resource(env, capacity = 1)
        
    
    
    def register_request(self):
            yield self.env.timeout(2) 
    
    def examine_casually(self):
            yield self.env.timeout(2) 
    
    def check_ticket(self):
            yield self.env.timeout(2) 
    
    def decide(self):
            yield self.env.timeout(2) 
    
    def reinitiate_request(self):
            yield self.env.timeout(2) 
    
    def examine_thoroughly(self):
            yield self.env.timeout(2) 
    
    def pay_compensation(self):
            yield self.env.timeout(2) 
    
    def reject_request(self):
            yield self.env.timeout(2) 
    