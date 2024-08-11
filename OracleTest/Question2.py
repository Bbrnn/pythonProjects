#A fucntion that returns all odd numbers that fall
#between two numbers,l and r in form of an array
def oddNumbers(l, r):
    # Write your code here
    
    odd_numbers = []
    
    for num in range(l, r+1):
        if num % 2 != 0:
            odd_numbers.append(num)
            
    return odd_numbers
        
        
l = 3
r = 10
print(oddNumbers(l, r))
    

if __name__ == '__main__':
