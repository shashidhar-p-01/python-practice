import random
import date
import calculator
from greetings import welcome
import math as m 
from utility import even_or_odd, largest



# 16. Create Your First Module
print(calculator.add(5, 3))        # Output: 8
print(calculator.subtract(5, 3))   # Output: 2
print(calculator.multiply(5, 3))   # Output: 15


# 17 Import and Use Your Module
print(welcome("appu"))   #Output : welcome appu!

# 18. Use Alias
print(m.sqrt(16))   # Output: 4.0

# 19. Create Utility Module
print(even_or_odd(5))   # Output: Odd
print(largest(5, 10, 3))   # Output: 10

# 21. Random Module Practice
li = random.randint(1,100)
print(li)
print(random.choice(['apple', 'banana', 'cherry']))


