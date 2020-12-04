# a=range (10)
# unpack: *
# print(*a)
# b=range(1,18)
# print(b)
# print(*b)
# c=range(20,10,-3)
# print(*c)
# for i in range(20,10,-1):
#     print(i)
# for _ in range(10):
#     print("Ha", end="----")
    # print("Ha",sep="**")
# d=range(101)
# print(*d)
# e=range(100,-1,-1)
# print(*e)
# f=range(0,101,2)
# print(*f)
# g=range(1,101,2)
# print(*g)
# print("a","b","c","d",sep="**")
# a=int(input("n="))
# b=range(a)
# print(*b)
# i = 1
# while i<=10:
#     print(i)
#     i = i + 1
i = 0
while i <= 10:
    i = i +1
    if i % 2!= 0:
        continue
    print (i)

