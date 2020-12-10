##########################################################################
#
#    randSelect.py
#    randomized selection
#    
#    selects element of kth rank in unsorted array of numbers
#    note: uses 1-based indexing
#
##########################################################################
import random

# ray is a list of ints
# index is an int
def randSelect(ray, index):
    print("Looking for value with rank " + str(index) + " in the array:\n" + str(ray))
    i = random.randint(0, len(ray) - 1) #pick a pivot index by random
    pivot = str(ray[i]) #store pivot before partition
    pos = partition(ray, i)
    if pos == index:
        success(pivot, str(pos))
        return ray[pos]
    elif pos > index:
        tooBig(pivot, str(pos))
        return randSelect(ray[0:pos], index)
    else:
        tooSmall(pivot, str(pos))
        return randSelect(ray[pos+1:len(ray)], index - pos - 1)
    
def partition(ray, i):
    pivot = ray[i] #store pivot
    ray[0], ray[i] = ray[i], ray[0] # put pivot in first slot
    s = l = 0 #starter num smalls and larges
    while s+l+1 < len(ray): #i.e. stop when the 'first unknown' is out of bounds
        if pivot < ray[s + l + 1]: #last unknown larger than pivot?
            l += 1 #add large
        else: #smaller?
            ray[s + l + 1], ray[s + 1] = ray[s + 1], ray[s + l + 1] #swap unknown w first large
            s += 1 #add small
    ray[0], ray[s] = ray[s], ray[0] #swap pivot with last small to place at middle
    return s #final index of pivot


###################
#     messages    #
###################
def success(pivot, rank):
    print(
        "Selected " +
        pivot +
        " as the pivot; its rank is " +
        rank +
        "; Thus, we recurse on nothing. We are done."
    )

def tooBig(pivot, rank):
    print(
        "Selected " +
        pivot +
        " as the pivot; its rank is " +
        rank +
        "; Thus, we recurse on left."
    )
    
def tooSmall(pivot, rank):
    print(
        "Selected " +
        pivot +
        " as the pivot; its rank is " +
        rank +
        "; Thus, we recurse on right."
    )
                          
