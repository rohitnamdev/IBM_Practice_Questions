def findFloorSequence(dir, currentFloor, req_Floor):
    if dir not in ["UP", "DN"] or not(0 <= currentFloor <= 15):
        return "Invalid"
    x = sorted(i for i in req_Floor if i >= currentFloor)
    y = sorted(i for i in req_Floor if i < currentFloor)[::-1]
    
    if dir  == "DN":
        y,x = x,y
    s = x+y
    for i in s:
        print(i)