#Operation on Tuples\

tup1=()
tup2=(2,5,8,12,6)
print("Tuple with integers ",tup2)

tup3=("Codingal",37.5,10)
print("Tuple with mixed datatypes ",tup3)

print("Temprature outside is ",tup3[1])

tup4=("Hello",[1,2,3],(3,4,5))
print("Nested tuple is  ",tup4)

print(tup4[1][1])
print(tup4[0][3])
print(tup4[2][1])

print(tup4[1:3])

tup5=('W','O','R','L','D')
for letter in tup5:
    print("Hello",letter)
    