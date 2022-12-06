import sys
import time
from tabulate import tabulate
from random import choice

for i in range(0, 10):
    while i:
        name_card = ['Jobin', 'Waru', 'Krentil', 'Hati']
        number_card = [2, 4, 5, 8, 10, 'J', 'K', 'Q', 'A']
        datanam = choice(name_card)
        numnam = choice(number_card)
        data = datanam, numnam
        print(data)

        break


x = 46
y = 23
body = [[x, y, x+y, x-y, x*y]]
print(tabulate(body, headers=['variabel_x', 'variabel_y',
      'sum', 'minus', 'multiplication'], tablefmt='grid'))

# tm = 2
# # here is the animation


# def animate():
#     while tm < 2:
#         sys.stdout.write('\rloading |')
#         time.sleep(0.1)
#         sys.stdout.write('\rloading /')
#         time.sleep(0.1)
#         sys.stdout.write('\rloading -')
#         time.sleep(0.1)
#         sys.stdout.write('\rloading \\')
#         time.sleep(0.1)
#     sys.stdout.write('\rDone!     ')


# animate()
# # long process here
# done = 'false'
