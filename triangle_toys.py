def triangle_type(sides):
    a,b,c = sorted(sides)
    if a+b > c:
        return "Equilateral" if a == b == c else "Isosceles" if a ==b or b == c else "None of these" 
    else:
        return "None of these"
def sol(toys):
    result = []
    for toy in toys:
        result.append(triangle_type(toy))
    return result


t = [[2, 2, 1], [3, 3, 3], [3, 4, 5], [1, 1, 3]]
print(sol(t))
