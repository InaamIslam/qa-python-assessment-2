def two(number):
    if number > 1:
        for integer in range(2, number):
            if number % integer == 0:
                return False
            else:
                return True 
    
    # if number / number == 1:
    #     return True
    # elif number in range(2, number) % number == 0:
    #     return True
    # else:
    #     return False


testing = two(7)
print(testing)
