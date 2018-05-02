
print(total_sum)

def find_if_prime(z):
    is_prime = True    
    for i in range(2, z):
        if z%i == 0:
            is_prime = False            
            break
    return is_prime
        
for k in range(2,20000):
    if find_if_prime(k) is True:
        total_sum += k
    
print(total_sum)

"""
worst possible implementation. There's too many steps.
Could get rid of calculations by:
 - getting rid of all the even numbers, as they are never prime
 - get rid of all multiples of 3
 - all multiples of 5..
 - all mlutples of 7.... etc.
 - keep working upwards, until you hit N/2, where N = max number.
 
 - This is the 'Sieve Of Eratosthenes'
 
 BUT will need to keep all those numbers in memory. numpy array probably...
 
 """
