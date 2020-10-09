from functools import reduce

if __name__ == "__main__":
    for i in range(1, int(input())+1): # More than 2 lines will result in 0 score. Do not leave a blank line also
        print(reduce(lambda x, y: x*10 + y, list(range(1, i)) + list(range(i, 0, -1))))




