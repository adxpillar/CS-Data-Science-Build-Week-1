import math 

# Implementing a decision tree 
# Classification tree using entropy for best split 
# entropy is weighted sum of average for each class of split
# formula p*log(p)

# entropy function 
def entropy_function(c, n):
    """
    args = split and number of observations
    returns = entropy value i.e p*log(p)
    
    """
    return -(c*1.0/n)*math.log(c*1.0/n,2)

# Calculate the entropy of two subset of data 
def entropy_calculation(c1, c2):
    """
    args: two subsets 
    returns: combined entropy value of two subsets

    """
    if c1 == 0 or c2 == :
        return 0
    return entropy_function(c1,c1+c2) + entropy_function(c2,c1+c2) 



