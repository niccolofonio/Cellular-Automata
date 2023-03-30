import numpy as np
import random
#import cell
# First we consider a square lattice, and we represent it as a matrix

N = 20
CA = []

for i in range(0, N):
    CA.append([])
    for j in range(0, N):
        CA[i].append(0)

def random_initialization(ca):
    for i in range(0, len(ca)):
        for j in range(0, len(ca[i])):
            ca[i][j] = random.randint(0,1)

def print_ca(ca):
    for i in range(0, len(ca)):
        string = ''
        for j in range(0, len(ca[i])):
            if ca[i][j] == 0 :
                string += ' - '
            else:
                string += ' * '
        print(string)
    print('------------------------------------')

def nn(ca, i, j):
    v = []
    v.append(ca[i][j - 1])
    v.append(ca[i][j + 1])
    v.append(ca[i - 1][j])
    v.append(ca[i + 1][j])
    return(v)

def ca_with_boundaries(ca):
    new_ca = []

    for i in range(0, len(ca)):
        new_ca.append([])
        for j in range(0, len(ca[i])):
            new_ca[i].append(ca[i][j])
    for i in range(0, len(new_ca)):
        new_ca[i].insert(0,new_ca[i][-1])
        new_ca[i].append(new_ca[i][1])

    new_ca.insert(0, new_ca[-1])
    new_ca.append(new_ca[1])

    return new_ca

random_initialization(CA)

# For the update we face a more complex situation than CA1d. We start with a really easy one.
# We consider the 4 nearest neighbours and, if there are 2 or more, the cell survive, if there are less than 2
# the cell dies, if it is empty but it has 3 or more neighbours it becomes full. We call this "islands model", since
# we can see that from random initialization we arrive to islands configuration

def evolution_1(ca):
    new_ca = ca_with_boundaries(ca)
    #print_ca(new_ca)
    for i in range(0, len(ca)):
        for j in range(0, len(ca[i])):
            v = nn(new_ca, i+1, j+1)
            #print(ca[i][j])
            #print(new_ca[i+1][j+1])
            #print(v)
            if ca[i][j]==1:
                if sum(v)>=2:
                    new_ca[i + 1][j + 1] = 1
                else:
                    new_ca[i + 1][j + 1] = 0
            else:
                if sum(v)>=3:
                    new_ca[i + 1][j + 1] = 1
                else:
                    new_ca[i + 1][j + 1] = 0

    new_ca.pop(0)
    new_ca.pop(-1)
    for i in range(0, len(new_ca)):
        new_ca[i].pop(0)
        new_ca[i].pop(-1)

    for i in range(0, len(ca)):
        for j in range(0, len(ca)):
            ca[i][j] = new_ca[i][j]

    #print_ca(new_ca)

steps = 200

print("Initial CA")
print_ca(CA)

for i in range(0, steps):
    evolution_1(CA)

print(f"CA after {steps} steps")

print_ca(CA)


