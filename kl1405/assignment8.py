import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from pylab import *
from investment import *

# author : Kaiwen Liu

def assignment8():

    ''' this module saves statistics info in the results.txt and generates the return histograms for each position'''

    positions=raw_input('a list of number of shares to buy in parallel: ') # ask for user input
    # split the elements in from the user input and to be used as an integer
    positions=positions.split(',')
    positions[0]=positions[0][1:]
    positions[-1]=positions[-1][:-1]
    positions=[int(i) for i in positions]

    # takes the input num_trails
    num_trials=int(raw_input('how many times to randomly reepat the test: '))

    a = invest(positions, num_trials)
    # get the results using the investment function
    results=a.investment()
    result=open("results.txt",'w') #for writing
    for num_position in positions:
        #to get the mean and standard deviation
        mean=str(np.mean(results[num_position]))
        std=str(np.std(results[num_position]))
        # write the txt file with each position and corresponding mean and standard deviation
        result.write('position = '+str(num_position)+ '\n' 'Mean: '+mean+ ' and Standard deviation:'+std+'\n')
        result.flush()
        plt.figure()
        # plot and save the histograms for each num_position 
        plt.hist(results[num_position],100, range=[-1,1])    
        plt.savefig('histogram_{0:0>4}_pos.pdf'.format(num_position))   
    result.close()
if __name__ == '__main__':
    try:
        assignment8()

    except KeyboardInterrupt, ValueError:
        print "\n Interrupted!"
    except TypeError:
        print "\n type error!"
    except ZeroDivisionError:
        print "\n mathematical error"
    except ArithmeticError, OverflowError:
        print "\n mathematical error!"
    except EOFError:
        print "\n Interrupted!"