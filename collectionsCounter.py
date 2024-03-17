
num = input('Enter the number:')
def main():
    from collections import Counter
    n = int(num)
    shoes = Counter(map(int, num.split()))
    customers = int(num)
    income = 0
    for _ in range(customers):
        size, price = map(int, num.split())
        if shoes[size]:
            income += price
            shoes[size] -= 1
    print(income)


