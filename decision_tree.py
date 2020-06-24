import math 
import numpy as np
import pandas as pd

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



# Decison tree 

class DecisionTreeClassifier:

    """
    implementing decision tree classifier with 
    max depth
    min_sample_leaf

    """

    def __init__(self,max_depth):
        self.depth = 0
        self.max_depth = max_depth

    # defining how split is done

    # find best split for one column
    def find_best_split(self,col,y):
        """
        args: column to split on, target variable
        return: minimum entropy and its cuttoff point
        """
        min_entropy =  10
        n = len(y)
        # iterate through each value in the column
        for value in set(col):
            # separate y into two groups
            y_predict = col < value 
            # get entropy of the split
            the_entropy = get_entropy(y_predict,y)
            # check if this is the best value
            if the_entropy <= min_entropy:
                min_entropy = the_entropy
                #  select value as cutoff point
                cuttoff = value
        return min_entropy, cutoff
    
    # find best split for multiple columns 
    def find_best_split_of_all(self,x,y):
        """
        args: features, target variable
        returns: col to split on, cutoff, minimum entropy
        """
        col = None
        min_entropy = 1
        cutoff = None 
        # Transpose features and iterate through each feature
        for i, c in enumerate (x.T):
            # find best split on column
            entropy, current_cutoff = self.find_best_split(c,y)
            # find the first perfect split and returns the cutoff
            if entropy == 0:
                return i, current_cutoff, entropy
            # check if it's the best so far and update values
            elif entropy <= min_entropy:
                min_entropy = entropy
                col = i
                cutoff = current_cutoff
        return col, cutoff, min_entropy

    # fit function
    # we recursively split into nodes from top to bottom 
    def fit(self,x,y,this_node={},depth=0):
        """
        args: features, target variable, node generated for this x and y
        returns: None

        """
        #  find our base cases 
        # case 1: tree stops at root
        if this_node is None:
            return None 
        #  case 2: no data in this group 
        elif len(y) == 0:
            return None 
        #  case 3: all values of y are the same this node
        elif self.values_identical(y):
            return {'val':y[0]}
        # case 4: we reached max depth 
        elif depth >= self.max_depth:
            return None
        else:
            # recursively generate trees
            # find split given information gain 
            col, cuttoff, entropy = self.find_best_split_of_all(x, y)
            # left of data
            y_left = y[x[:, col] < cutoff] 
            # right of data 
            y_right = y[x[:, col] >= cutoff] 
            # set node with the information
            this_node = {'col': iris.feature_names[col], 'index_col': col,
                        'cutoff': cuttoff,
                        'value': np.round(np.mean(y))
                        }
            # generate tree for left handside data
            this_node['left'] = self.fit(x[x[:, col] < cutoff], y_left, {}, depth+1)
            # generate tree for right handside data 
            this_node['right'] = self.fit(x[x[:, col] >= cutoff], y_right, {}, depth+1)   
            # increase depth of tree
            self.depth += 1 
            self.trees = this_node
            return this_node
    
    # function to check group with same values 
    def values_identical(self,items):
        """
        args: iterable variable list
        returns: True if all values are identical
        """
        return all(x == items[0] for x in items)



        








        


            



