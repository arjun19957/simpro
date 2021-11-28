import random
import numpy as np


class process_path_probability():
    
    def __init__(self, variants):
        self.variants = variants
        self.variant_frequencies = []
        
        
    def extract_frequencies(self):
        
        for i in range(len(self.variants)):
            self.variant_frequencies.append(self.variants[i][1])
            
    def variant_cumsum_calculator(self):
        
        self.variant_cumsum = np.cumsum(self.variant_frequencies)
        
    def variant_probability_calculator(self):
        
        self.variant_probability = self.variant_cumsum/self.variant_cumsum[-1]
    
    def run(self):
        
        self.extract_frequencies()
        self.variant_cumsum_calculator()
        self.variant_probability_calculator()
        
        return list(self.variant_probability)
    
    
    
    
    
def process_path_selector(process_path_probabilities):
    
    random_number = round(random.uniform(0,1),2)
    
    for i in range(len(process_path_probabilities)):
        if random_number <= process_path_probabilities[i]:
            return(i)
            break


    

