import itertools

def all_perms(elements):
    for val in elements:
        if val == ' ':
            print("does this work")

def next( current):
    space = current.index(' ')
    cost = 1
    new = []
    for i in range(1, 4):
        new = current[:]
        print(current)
        if ((space - i) > -1):
            new[space - i], new[space] = new[space], new[space - i]

        elif ((space + i )< 7):
            new[space + i], new[space] = new[space], new[space + i]
        print(new)


if __name__ == '__main__':
    next(['w', 'w', 'w', 'b', 'b', 'b' ,' '])
   ## next([ ' ','w', 'w', 'w', 'b', 'b', 'b'])