# I AM BORED ...
# Here, this is "bored" code. blegh

# balance = 0
# payment = 0
#
# while balance <= 0:
#     balance = float(input("Amount to be saved: "))
#
# while payment <= 0:
#     payment = float(input("Amount per payment: "))
#
# for i in range(3):
#     print(i)
#
# remaining_payments = balance/payment
#
# print("{} payments left".format(remaining_payments))

# for i in range(5, 1, -1):
#     print(i)
#
# i = 5
# while i > 1:
#     print(i)
#     i = i-1
#
# for i in range(10):
#     for j in range(10):
#         print(i, '*', j, '=', i*j)

numpeople = int(input("How many people are there?"))

for i in range(1, numpeople+1):
    for j in range(i+1, numpeople+1):
        print(i, j)
