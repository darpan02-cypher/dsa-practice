def countNeg(x: list[int])-> int:
    count =0
    for num in x:
        if num<0:
            count=count +1
    return count


#example usage:check for all test cases
x=[-1,2,-3,4,-5]    
print(countNeg(x))
