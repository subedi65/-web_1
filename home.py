# #bit operators
# a=10
# b=1
# print(bin(a&b)) #this is and  gate
# print(bin(a^b)) #this is xor gate
# print(bin(a|b)) #this is or gate
# print(bin(~a)) #this is not gare for a
# print(bin(~b)) # this is not gate for b



# #slice operators
# a=[0,1,2,4,5,6,7,8]
# print("a[:2]->", a[:2])
# print("a[4:-1]->", a[4:-1])
# print("a[::-1]->", a[::-1])
# print("a[2::2]->", a[2::2])
# print("a[7:1:-2]->", a[7:1:-2])

# #condition loop 
# a=99
# if a<100:
#     print("it is smaller than 100")
# else :
#     print("error")


# absence=int(input("enter the number of days :"))
# if absence >3:
#     print("dangerous")
# else :
#     print("normal")

# number = int(input("enter the number"))
# if (number %0):
#     print("enter the odd number")
# else :
#     print("you have entered the correct number")


# for i in range(1,100,2):
#     print(i)
# a=0
# for i in range(1,11):
#     if i%2!=0:
#         a+=i
# print(a)


# total_numbers = int(input("How many numbers do you want to enter? "))
# sum_total = 0

# for i in range(total_numbers):
#     number = int(input(f"Enter number {i+1}: "))
#     sum_total += number

# print("The total sum is:", sum_total)


for a in range(1,10):
 for i in range(11):
    print(a,"*",i,"=", i*a)
    print("_"*30)