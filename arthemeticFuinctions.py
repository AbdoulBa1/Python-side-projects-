def plus_one(number):
    return number + 1
def add(number1, number2):
    total_sum = number1 
    for i in range(number2):
        total_sum = plus_one(total_sum)
    return total_sum
def multiply(number1, number2):
    total_product = 0
    for i in range(number2):
         total_product = add(number1, total_product)
    return total_product 
# only works for positive numbers; when adding positive number or multiplying by positive number. 