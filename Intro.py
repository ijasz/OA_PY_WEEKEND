##print(type(43))
##print(type("Arun"))
##print(type(True))
##print(type(0.1))
##print(type(1j))

#variable

##var1 = 34

##print(type(var1))
##print(var1)

##var1 = 545.54

##print(type(var1))
##print(var1)

##var1 = False

##print(type(var1))
##print(var1)

##var1 = "Arun"

##print(type(var1))
##print(var1)

##Two types of error
##syntax error and runtime error

##indentifier

##camelCase
##Python is case-sensitive

##isValidBool = True
##isvalidbool = False

##print(isvalid)
##print(isValid)

##a = 10
##b = 20

##a,b = 10,20

##variable swapping using temp variable
##c = a
##a = b
##b = c

##print(a, b)

##variable swapping without using temp variable

##a,b = b,a

##print(a, b)

##print(id(a), id(b))

##Operator

##Arithmetic operators

##+  Addition
##-  Subtraction
##*  Multiplication
##/  Division
##// Floor division	
##%  Modulus
##** Exponentiation

##a = 5
##b = 2

##print(a + b)
##print(a - b)
##print(a * b)
##print(a / b)
##print(a // b)
##print(a % b)
##print(a ** b)



##Assignment Operators

##=	
##+=		
##-=		
##*=		
##/=		
##%=		
##//=		
##**=		
##&=		
##|=	
##^=	
##>>=	
##<<=

##a = 10

##a = a + 10
##a += 10

##print(a)

##Comparison Operators

##==	Equal	
##!=	Not equal	
##>	Greater than	
##<	Less than	
##>=	Greater than or equal to	
##<=	Less than or equal to

##print(1 == 2)
##print(1 != 2)
##print(1 >= 1)
##print(1 <= 2)

##Python Logical Operators

##and or not

##print(4 > 3 and 0 >= -6)
##print(4 > 3 and 0 >= 6)
##print(4 > 3 or 0 >= 6)
##print(4 > 3 and not(0 >= 6))
##print(not(4 > 3 and 0 >= 6))

##Identity Operators

##a = "a"
##b = "a"

##print(id(a), id(b))

##print(a == b)
##print(a is b)


##Membership Operators

##a = "myself arun"

##print("mys" not in a)

##Operator Precedence PEMDAS

##print(54 - (5 * 2))
##print(54 - 5 * 2)

##Type Casting

##a = "10"
##a = int(a)
##a = float(a)
##a = str(a)
##a = list(a)

##print(a)
##print(type(a))

##String concatenation

##greeting = "hello"
##name = input("enter your name")
##result = greeting + " " + name

##print(result)

##Multiplication of Strings

##a = int(input("how many columns you want"))

##print("* " * a)
##print("* " * a)
##print("* " * a)
##print("* " * a)

##conditional statement

username = input("Enter your name to Login☺: ")
password = input("Enter your passwword to Login: ")

realUsername= "arun"
realPassword = "1234"

if(realUsername == username and password == realPassword):
    print("Hi! buddy you are logged in")
elif(username == realUsername):
    print("you can change your password")
    choice = int(input("Enter 0 to change password"))
    if(choice == 0):
        realPassword = input("change your password: ")

        username = input("Enter your name to Login☺: ")
        password = input("Enter your passwword to Login: ")

        if(realUsername == username and password == realPassword):
            print("you are logged in")
        else:
            print("Sorry invalid credential")


    
else:
    print("Sorry invalid credential")




















