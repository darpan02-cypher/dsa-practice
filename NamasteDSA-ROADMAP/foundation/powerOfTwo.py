def powerOfTwo(n:int) -> bool:

    #base case
    if n<=0:
        return False    
    if n==1:
        return True

    #check if the number is odd, if it is odd then it cannot be a power of two
    if  n%2==1:
        return False

    #recursive step: divide the number by 2 and check if the result is a power of two
    return powerOfTwo(n//2)

#time complexity: O(log n) - The function divides the input number by 2 in each recursive call, which reduces the problem size logarithmically. Therefore, the time complexity is O(log n).
#space complexity: O(log n) - The space complexity is O(log n) due to the recursive call stack. Each recursive call adds a new frame to the call stack, and the maximum depth of the recursion is proportional to log n, where n is the input number.

#example usage with all types oftest cases
test_cases = [-7,0,1, 2, 3, 4, 5, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
for n in test_cases:
    result = powerOfTwo(n)
    print(f"{n} is a power of two: {result}")       