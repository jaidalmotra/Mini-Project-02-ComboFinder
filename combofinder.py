#To generate randome interger for the random size of the combo
import random

#The following is a dictionary that will contain the product and their respective costs for eg:- we have 14 products here with their respective costs 
ProductList = {'p1': 10, 'p2': 15, 'p3': 20, 'p4': 25, 'p5': 30, 'p6': 35, 'p7': 50,
               'p8': 40, 'p9': 55, 'p10': 60, 'p11': 65, 'p12': 75, 'p13': 70, 'p14': 45}

#LB is the lower bound or the lower limit total cost of your combo where UB is the upper limit cost of your combo .your combo price will be within this range (LB,UB)
LB = 290
UB = 310
ResultList = set()

# this will be the number of iteration for which the random list will be generated
iterations=1000

for _ in range(iterations):
    combo_size = random.randint(2, len(ProductList) - 1)
    combo_list = random.sample(list(ProductList.keys()), combo_size)  # Convert dict keys to a list
    combo_sum = sum(ProductList[i] for i in combo_list)
    if LB <= combo_sum <= UB:
        ResultList.add(tuple(combo_list))

for result in ResultList:
    print(result)

print("\nTotal Sets:", len(ResultList), "\n")