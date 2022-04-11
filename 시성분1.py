import random
numbers = [ i + 1 for i in range(45)]
lottonumbers = random.sample(numbers, 6)
lottonumbers.sort()
print(lottonumbers)
