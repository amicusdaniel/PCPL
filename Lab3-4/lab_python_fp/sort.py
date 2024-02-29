data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

def mysort(mass):
    return sorted(mass)

def main():
    result = sorted(data, key=abs, reverse=True)
    print(result)
    lambda_r = sorted(data, key=lambda i:abs(i), reverse=True)
    print(lambda_r)


