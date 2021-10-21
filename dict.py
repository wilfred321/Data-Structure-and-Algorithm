# d = {}
# d[1] = 'one'
# d[2] = 'two'
# d[3] = 'three'

# print(d.keys())
# print(d.values())
# print(d.items())

# class my_class():
#     def __init__(self):
#         self.data = 'Hello'

# instance = my_class()

# d['object'] = instance

# print(d['object'].data)

# print(d.items())

class_names = ['Wilfred','Bob','Teju','Jerry','Dim','Dami','Charles','Funke','Ope','Joseph']

def create_dataset():
    import random
    num_entries = 5000000
    f = open('data.txt',"w")
    for i in range(num_entries):
        current = random.choice(class_names)
        f.write(current + "\n")
    f.close()

def read_dataset_list():
    class_counts = []
    for c in class_names:
        class_counts.append(0)

    with open('data.txt',"r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                class_counts[class_names.index(line)] += 1
    print (class_counts)



def read_dataset_dict():
    class_counts = {}
    for c in class_names:
        class_counts[c] = 0
    with open("data.txt") as f:
        for line in f:
            line = line.strip()
            if line != "":
                class_counts[line] += 1
    print (class_counts)


import time

import time
t0 = time.time()
create_dataset()
t1 = time.time()
print (f"Dataset creation took {round(t1-t0,2)} seconds")

t0 = time.time()
read_dataset_list()
t1 = time.time()
print (f"List took {round(t1-t0,2)} seconds")


t0 = time.time()
read_dataset_dict()
t1 = time.time()
print (f"Dict took {round(t1-t0,2)} seconds")