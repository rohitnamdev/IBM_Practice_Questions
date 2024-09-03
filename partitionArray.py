def partitionArray(k, numbers):
    from collections import Counter
    freq = Counter(numbers)
    n = len(numbers)
    if n% k !=0:
        return "No"
    num_subsequence= n//k
    for count in freq.values():
        if count > num_subsequence:
            return "No"
    return "Yes"

print(partitionArray(2,[1,2,3,4]))


def partitionArray(k, numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % k != 0:
        return "No"
    
    num_subsequence = n // k
    freq = {}
    
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for count in freq.values():
        if count > num_subsequence:
            return "No"
    
    return "Yes"

print(partitionArray(2, [1, 2, 3, 4]))
