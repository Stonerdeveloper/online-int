from random import choice
from statistics import mode

color_worn = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE',
              'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED',
              'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN',
              'HARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLUE', 'PINK', 'PINK', 'ORANGE',
              'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE',
              'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE',
              'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE',
              'BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW',
              'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN',
              'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE',
              'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE'
]

no_of_colors = len(color_worn)
print(len(color_worn))

def color_count(co):
    counts = dict()


    for word in color_worn:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

total_color = color_count(color_worn)
print(total_color)


len_color = len(color_count(color_worn))
print(len_color)


# 1: Mean color
mean = no_of_colors/len_color
print('1: The Mean is : ',mean)


# 2: Mode
print('2: The Most worn Color throughout the week is: ', mode(color_worn))


# Median
median = no_of_colors / 2
print('3: Median: ', median)

# 8: Random
list = []
sep = [0, 1]
for _ in range(4):
    selection = choice(sep)
    #print('Randomly selected numbers: ', selection)
    list.append(selection)
print(list)
s = ''.join(map(str, list))
print('8: Randomly selected number converted to base 10: ', int(s, base=2))


# 9: fibonacci sequence
x, y = 0, 1

while y < 50:
    print(y)
    x, y = y, x + y
sum = x + y
print('9: sum of first 50 fibonacci sequence is: ', sum)


