class process_definition():

    def __init__(process_A,process_B,process_C, ):
        self.env = simpy.Environment()
        
        self.process_A_resource = simpy.Resource(env, capacity = 1)
        
        self.process_B_resource = simpy.Resource(env, capacity = 1)
        
        self.process_C_resource = simpy.Resource(env, capacity = 1)
        
    
    
    def process_A:
        yield env.timeout(2) 
    
    def process_B:
        yield env.timeout(2) 
    
    def process_C:
        yield env.timeout(2) 
    