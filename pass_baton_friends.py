def batonPass(friends, time):
    current_passer = 1  # Start with Friend 1
    direction = 1  # 1 for forward, -1 for backward
    
    for _ in range(time):
        # Pass the baton
        current_passer += direction
        
        # Reverse direction when reaching the end or the beginning
        if current_passer == friends + 1:
            direction = -1
            current_passer = friends - 1
        elif current_passer == 0:
            direction = 1
            current_passer = 2
    
    final_passer = current_passer
    final_receiver = current_passer + direction
    
    return [final_passer, final_receiver]

# Test the function
friends = 4
time = 5
output = batonPass(friends, time)
print(output)  # Expected Output: [3, 2]
