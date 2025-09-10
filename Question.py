#PRINT SQAURE OF A NUMBER
num=int(input("Enter the number: "))
print(f"Square of {num} is {num**2}")



#PRINT SUM OF TWO NUMBERS
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
print(f"Sum 0f {num1} and {num2} is {num1+num2}")



#SWAP TWO VARIABLES
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num1,num2=num2,num1
# temp=num1
# num1=num2
# num2=temp
print(f"Now the 1st number is {num1} and the second number is {num2}")



#NUMER GUESSING GAME
a=7
guess=int(input("Guess the number...."))
if(guess==a):
    print("You are right")
else:
    print("You guessed wrong")
    



#CHECK IF NUMBER IS EVEN OR ODD
num=int(input("Enter the number: "))
if(num%2==0):
    print(f"{num } is even")
else:
    print(f"{num} is odd")



#CONVERT CELSIUS TO FARENHEIT
cel=int(input("Enter the temp in celsius"))
print(f"{cel} degree celsius is equal to {(cel*(9/5))+32} degree farenheit")


#PRINT TYPE OF VARIABLE
a=9
b=8.6
c="hello"
d=True
print(f"Type of: \n  {a} is {type(a)} \n  {b} is {type(b)} \n  {c} is {type(c)} \n  {d} is {type(d)}")



#CALCULATE SIMPLE INTEREST
p=int(input("Enter the principle: "))
r=int(input("Enter the rate: "))
t=int(input("Enter the time in months: "))
print(f"Simple Interest on {p} at the rate of {r}% for {t} months is {(p*r*t)/100}")



#REVERSE THE STRING
s = input("Enter the string: ")
s = list(s)
for i in range(len(s) // 2):
    s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

s = "".join(s)
print("Reversed string:", s)
