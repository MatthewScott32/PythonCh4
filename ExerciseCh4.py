import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

numbers_1_to_10 = list(range(1,11))
print(numbers_1_to_10)

for number in numbers_1_to_10:
    the_numbers_match = False
    if number in my_randoms:
        the_numbers_match = True
    
    if the_numbers_match:
        print(f'{number} is in the random list')
    else: print(f'{number} is not on the list')
    
