# Task
#
#  is a shoe shop owner. His shop has  number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.
#
# Your task is to compute how much money  earned.
#
# Input Format
#
# The first line contains , the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains , the number of customers.
# The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

input = "10\n2 3 4 5 6 8 7 6 5 18\n6\n6 55\n6 45\n6 55\n4 40\n18 60\n10 50"
output = "200"


def main():
    from collections import Counter
    n = int(input())
    shoes = Counter(map(int, input().split()))
    customers = int(input())
    income = 0
    for _ in range(customers):
        size, price = map(int, input().split())
        if shoes[size]:
            income += price
            shoes[size] -= 1
    print(income)


