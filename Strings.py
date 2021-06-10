s = "SampleString"
print(s[6:8])
print(s[1:])
print(s[:])
#[startindex:endindex:steps]
print(s[0:14:2])
numb = "1,345;456:789,908"
print(numb[1::4])

backwards = s[0:15:1]
print(backwards)

#string concatanation
print("Hello" "world" "Green" "Earth")
print("World" * 4)

#substring
print("Hell".upper() in "Hello".upper()) # same case
print("HELL" in "Hello") # upper case

#string formatting
age =12
Height = 5.3
print("My age is" +str(age) +"and height is  "+ str(Height))
print("My age is {0} and height is {1}".format(age,Height))
print(f"My Age is {age} and height {Height}")
print("Days in Months Jan {0} : Feb {1} : Mar {2} : Apr {0} : May {2} : June {0} : July {2} : Aug {0}".format(31,28,30))

# < Left centered
# > right centered
# ^ center aligned

#for var in range(1,10):
    #print(f"The square of {var:<2} is {var**2:>3} and cube is\t {var**3:^4}")
print(f"The floating point number is {22/7:12}")
print(f"The floating point number is {22/7:<12f}")
print(f"The floating point number is {22/7:^0.55f}")

if age >=45:
    print("45+ for vaccination")
elif age>=18<45:
    print("18+ for vaccination")
elif age>=12<18:
    print("12+ for vaccination")
else:
    print("Not valid for any vaccination")

dt = 25
aj=5
daytype = False

if 3 >= dt <= 15 or not daytype:
    print("No idea what i am doing")
else:
    print("I am crazy bugger")

