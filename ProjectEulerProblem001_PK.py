"""
Created on Thu Mar 29 10:40:19 2018

@author: krishnap
"""

# Project Euler - Problem 1
# 29/03/18



from datetime import datetime
startTime = datetime.now()


def ProjEul001(n):
    
    total_sum = 0

    for i in range(1,n):
        if i%3 == 0 or i%5 ==0:
            total_sum += i
        else:
            pass
            
    print(total_sum)



ProjEul001(10000000)

print('Time taken: ' + str(datetime.now() - startTime))



# more efficient way to do this: use Arithmetic/Geometric sums.
