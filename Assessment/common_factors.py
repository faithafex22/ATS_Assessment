#Write a program that can return common factors of two or more numbers
def common_factors(num1 , num2):
    factors1 = []
    factors2 = []
    common_fact = []
    for i in range (1, num1+1):
        if num1%i == 0:
            factors1.append(i)
    for i in range (1, num2+1):
        if num2%i == 0:
            factors2.append(i)
        if i in factors1 and i in factors2:
            common_fact.append(i)
    return f'The common factors of {num1} and {num2} are -> {common_fact}'
print(common_factors(50, 100))

