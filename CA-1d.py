import random

# The idea is to have a vector CA that represents the sequence of sites in 1d
# The following functions are used to initialize, update and print the CA

# This is a function to print the state at a particular moment of the CA

def print_ca(ca):
    printing_v = ''
    for i in range(0,len(ca)):
        if ca[i]==0:
            printing_v += '-'
        else:
            printing_v += '*'
    print(printing_v)

# These are the initialization function

def random_initialization(N):
    ca = []
    for i in range(0,N):
        ca.append(random.randint(0,1))
    return ca

def central_initialization(N):
    ca = []
    for i in range(0,N):
        if i!=N/2:
            ca.append(0)
        else:
            ca.append(1)
    return ca

# Here we can give an easy example of a propagation rule: they move to the right

def trivial_propagate(ca):
    new_ca = random_initialization(len(ca))
    for i in range(0, len(ca)-1):
        if ca[i]==1:
            new_ca[i+1] = 1
        else:
            new_ca[i + 1] = 0
    if ca[len(ca)-1] == 1:
        new_ca[0] = 1
    else:
        new_ca[0] = 0
    for i in range(0, len(ca)):
        ca[i] = new_ca[i]

# Here starts the real work. Each CA is characterized by an update rule. We consider only nearest neighbours update
# so r=1. Thus we have 8 possible states of a triplet. Each state of the triplet can be updated in 0 or 1, thus
# we have 256 possible rules. These possible rules are encoded by a correspondency between the 8 possible states of
# the triplet and the correponding bit of the rule. To see it practically, try to see some rules with the rule function

# To make the rule function we need to use binary representation. This is not convenient in python, so we arranged
# specific functions

def from_int_to_bin_3(n):
    washed_bin_n = bin(n)[2:len(bin(n))] # the output of bin() is in form 0b###, thus we pop the 0b
    while len(washed_bin_n) < 3: # here we need to arrange to have triplets, since bin(2) would be 10, while we need 010
        washed_bin_n = '0' + washed_bin_n
    return washed_bin_n

def from_int_to_bin_8(n):
    washed_bin_n = bin(n)[2:len(bin(n))]
    while len(washed_bin_n) < 8: # since we need to update 8 triplets, we need 8 bits, that is the corresponding rule
        washed_bin_n = '0' + washed_bin_n
    return washed_bin_n

def rule(n):
    dicti = {} # we build a dictionary s.t. dict[triplet] = correponding bit from the rule n
    for i in range(0, 8):
        dicti[from_int_to_bin_3(i)] = from_int_to_bin_8(n)[-1-i]
    return dicti

print(rule(18))

# Now we can write a function that updates the CA

def evolution_1d(n, ca):
    dicti = rule(n) # we define the rule
    new_ca = [] # we define the copy of the ca that will be updated
    ca.append(ca[0]) # for the boundary conditions we add to the ca the corresponding boundaries
    ca.insert(0, ca[-1])
    # print(ca)
    for i in range(0, len(ca)):
        new_ca.append(ca[i])
    str_ca = '' #we need to manipulate string to access the corresponding key of the dict rule
    for i in range(0,len(ca)):
        str_ca = str_ca + str(new_ca[i])

    for i in range(1, len(new_ca) - 1): # the loop excludes the boundary bits, that will be removed
        new_ca[i] = int(dicti[str_ca[i-1:i+2]]) # we update the state in the copy of the ca

    # we remove the boundary bits
    ca.pop(0)
    ca.pop(-1)
    new_ca.pop(0)
    new_ca.pop(-1)
    for i in range(0, len(ca)): # we copy the updated ca in the new ca
        ca[i] = new_ca[i]

# From here on we modify features to see the different rules
# The numbers of steps and sites is arbitrary, as the initialization.
# The rule's number rule_n is between 0 and 255

steps = 20 # number of steps
N = 200 #number of sites
CA = random_initialization(N) #initialization
rule_n = 18 # rule number between 0 and 255

for i in range(0,steps):
    print_ca(CA)
    trivial_propagate(CA)
    #evolution_1d(rule_n, CA)
