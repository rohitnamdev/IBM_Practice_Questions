import math 
def sol(arr):
    total_cost = 0
    while len(arr) !=1 :
        min_,max_ = min(arr), max(arr)
        cost = math.ceil((min_+max_)/(max_-min_+1))
        arr.remove(min_), arr.remove(max_), arr.append(min_+max_)
        total_cost += cost
    return total_cost
arr = [8,8,8,8]
print("total cost is : ", sol(arr))