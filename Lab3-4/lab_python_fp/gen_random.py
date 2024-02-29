from random import randint

def gen_random(count, begin, end):
    return (f', зарплата {randint(begin, end)} руб.' for i in range(count))

def main():
    nums = gen_random(5, 1, 3)
    for i in nums:
        print(i, end=' ')
