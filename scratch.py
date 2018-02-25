import itertools

def all_perms(elements):
    for val in elements:
        if val == ' ':
            print("does this work")


if __name__ == '__main__':
    all_perms(['w', 'w', 'w', 'b', 'b', 'b' ,' '])