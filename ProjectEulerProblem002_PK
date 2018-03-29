"""
Created on Thu Mar 29 19:40:19 2018

@author: krishnap
"""

# Project Euler - Problem 2
# 29/03/18



from datetime import datetime
startTime = datetime.now()


list1 = [0]
n = 4000000


def ProjEul002(n):
    
    global sum_total
    global b
    
    a = 0
    b = 1
    sum_total = 0
    while b<n:
        a, b = b, a + b
        if b%2 ==0:    
            sum_total += b
            
    return sum_total


print(ProjEul002(n))

print('Time taken: ' + str(datetime.now() - startTime))
