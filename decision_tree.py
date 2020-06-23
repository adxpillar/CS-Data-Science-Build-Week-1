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

# Calculate the entropy of two classes  
def entropy_calculation(c1, c2):
    """
    args: two diff classes
    returns: combined entropy value of two subsets

    """
    # confirm that indeed have two classes
    if c1 == 0 or c2 == 0:
        return 0
    return entropy_function(c1,c1+c2) + entropy_function(c2,c1+c2) 

# calculate entropy of subset of data 

def entropy_of_one_subset(subset):
    """
    args: subset of data
    returns: len of subset and entropy value of subset
    data may have multiple subsets
    """
    # iterator 
    i = 0
    n = len(subset)
    # unique subsets
    subsets = set(subset)
    # for each subset
    for sub in subsets:
        # summation of each subset 
        summation = sum(subset==sub)
        # calculate entropy iteratively 
        weighted_avg_entropy = summation*1.0/n * entropy_calculation(sum(subset==sub),sum(subset!=sub))
        i += weighted_avg_entropy
    return i, n

# get entropy of combined split
def get_entropy(y_predict,y_real):
    """
    args: predicted y value of True or False, real y value (can be multiclass)
    returns: total entropy value of a split

    """
    # check length of actual and predicted values
    if len(y_predict) != len(y_real):
        print("Unequal length of actual value and predicted value")
        return None
    n = len(y_real)
    # calculate entropy of left and right sides of a node
    i_true, n_true = entropy_of_one_subset(y_real[y_predict])  #left
    i_false, n_false = entropy_of_one_subset(y_real[~y_predict]) #right
    # total entropy
    i = n_true*1.0/n * i_true + n_false*1.0/n * i_false 
    return s







