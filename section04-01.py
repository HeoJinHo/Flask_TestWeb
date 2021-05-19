# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25,
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}


print(type(v_set))
print(type(v_tuple))
print(type(v_bool))
print(type(v_str2))

a = 5.
b = 4
c = 10

result = a + b

print(result)
print(int(result))
print(float(result))
print(float(c))
print(int(True))
print(int('3'), type(int('3')))
print(complex(False))

y = 100
y += 100

print(y)

# 수치 연산 Function
print(abs(-7))
n,m = divmod(100, 8)
print(float(n),m)

import math

print(math.ceil(5.1))
print(math.floor(3.874))













