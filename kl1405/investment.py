import numpy as np

# author: Kaiwen Liu

class invest:

    def __init__(self, positions, num_trials):

        self.positions = positions
        self.num_trials = num_trials

    def investment(self):
        '''
        to simulate with positions: a list of the number of shares to buy in parallel, and num_trails: how many times to repeat
        '''
        #an empty results dict
        results={}
        
        for num_position in self.positions:
            daily_ret=[] #create a new daily_ret list
            position_value=1000/num_position #the position_value function
            for trail in range(1,self.num_trials):
                #simulate
                expect_prob=np.random.choice([-1,1],num_position,p=[0.49,0.51])
                cumu_ret=position_value*np.sum(expect_prob + 1) # the return from the investments
                daily_retu=(cumu_ret/1000.)-1 # result of each day as the daily_retu
                daily_ret.append(daily_retu) # append each daily_return value onto the daily_ret list
            if (results.has_key(num_position)):
                results[num_position].append(daily_ret)
            else:
                results[num_position]=daily_ret #write the daily_ret to results dictionary
    
        return results