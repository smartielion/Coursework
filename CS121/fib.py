#Assignment Number 3
#Fibonnaci sequence
#Casey Gilray

def fib(N,depth):
    #sets up number of spaces for depth output
    space = " "
    #base case
    if N == 1 or N == 2:
        print space*depth, '1 : Base case'
        return (1)
    else:
        #recursive addition, 
        #print what it is finding
        print space*depth, (N-1), ' and  ',(N-2) 
        return((fib((N-1),(depth+1)) + (fib((N-2),(depth + 2)))))
    
    
    

def test():
    #make assertions for base case
    assert fib(1,1) == 1
    assert fib (2,1) == 1
    #make assertions for other known cases
    assert fib(5,1) == 5
    assert fib(7,1) == 13
    assert fib(9,1) == 34
    return


    
