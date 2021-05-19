# 1. 문자형 관련 연산자
# 2. 문자열 생성, 길이
# 3. 이스케이프 문자
# 4. 문자열 연산
# 5. 문자열 형 변환
# 6. 문자열 함수
# 7. 문자열 슬라이상(중요)

str1= "I am Boy."
str2= 'Niceman'
str3= ' '
str4= str('as')

# 1, 2
print(len(str1), len(str2), len(str3), len(str4))

# 3
escape_str1 = "Do you have a \"big collection\""
print(escape_str1)

escape_str2 = "Tab \t Tat \t"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'

print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# Multi Line
multi = \
    """ 
    문자열
    멀티라인
    테스트
    """
print(multi)


# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print('a' in str_o4)
print('T' in str_o4)
print('z' not in str_o4)

tt = 'z' not in str_o4

print(tt, "TTTT")

# 문자열 함수
a = "niceman"
b = "Orange"

# print("---------------------")
# print(a.islower())
# print(b.endswith('e')) # 마지막문자가 e가 있는지 확인
# print(a.capitalize()) # 첫문자를 대문자로
# print(a.replace('nice', 'good'))
# print(list(reversed(b)))


a = "niceman"
b = "orange"

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:4])
print(b[:4:2])
print(b[1:-2])
print(b[::-1])






