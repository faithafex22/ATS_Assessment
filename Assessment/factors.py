#Write a program that can return factors of a number

def factors(num):
    factors_list = []
    for i in range (1, num+1):
        if num % i == 0:
            factors_list.append(i)
    return f'The factors of {num} number are collated in this list -> {factors_list}'

print(factors(100))