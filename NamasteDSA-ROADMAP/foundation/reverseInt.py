def revereseInt(x: int) -> int:
    is_negative = x < 0  # 1. Save the original sign first
    num = abs(x)         # Use a separate variable to keep track
    rev = 0

    # 2. Proper indentation inside the function
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10

    # 3. Check the stored sign instead of x or num
    return -rev if is_negative else rev

#example usage:check for all test cases
x=789876
result= revereseInt(x)
print(f"Reverse of {x} is: {result}")

x=-789876
result= revereseInt(x)
print(f"Reverse of {x} is: {result}")

