class cigar:
    
    def types(self,name,cost):
        n = name
        final_cost = cost*13  
        print(f'cigar type {n} cost {final_cost}')
o = cigar()
print(o.types('light',18))