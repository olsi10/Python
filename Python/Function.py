# def times (a, b):
#     return a * b

# print(times)            # 함수의 주소값
# print(times(10 ,5))     # 함수의 리턴값

# myTimes = times # times의 주소를 가리킴

# def myTimes (a, b):
#     return a * b

# print(times)            # 함수의 주소값 / 함수 카피 가능 같은 주소를 가리킴!
# print(times(10 ,5))     # 함수의 리턴값


# 표준 함수와 사용자 정의 함수
# 컴파일러가 미리 제공

# pi = 3.56789
# print(pi, "의 소수점 1자리 반올림은", round(pi))
# print(pi, "의 소수점 1자리 반올림은", round(pi, 0))
# print(pi, "의 소수점 2자리 반올림은", round(pi, 1))
# print(pi, "의 소수점 3자리 반올림은", round(pi, 2))
# print(pi, "의 소수점 4자리 반올림은", round(pi, 3))

# numbers = [1, 5, -2, 0 ,6]
# print(numbers, "중 가장 큰 값은 : ", max(numbers))
# print(numbers, "중 가장 작은 값은 : ", min(numbers))
# print(numbers, "합계는 : ", sum(numbers))
# print("2의 10승은 :  ", pow(2, 10))

# print(10, "의 절댓값 : ", abs(10))
# print(-10, "의 절댓값 : ", abs(-10))

# print(128, "의 2진수 : ", bin(128))
# print(255, "의 2진수 : ", bin(255))
# print(7, "의 8진수 : ", oct(128))
# print(8, "의 8진수 : ", oct(8))
# print(15, "의 16진수 : ", hex(15))
# print(16, "의 16진수 : ", hex(16))

# user_name = input("이름은?")
# user_age = input("나이는?")

# print(user_name + "님! 나이는 " + str(user_age ) + "세군요!")

# say = "{0}님! 나이는 {1}세군요 {1}세라니 놀라워"

# print(say.format(user_name, user_age))

# pi = "3.14159"
# print("문자열 출력 : ", pi)
# print("실수 변환 출력 : ", float(pi))
# print(float(pi) + 100)

# year = "2018"
# print("올해 년도 : ", year)
# print("100년 뒤는 ", int(year) + 100, "년입니다")
# print("숫자는 문자열로 변환하려면 str()을 이용합니다")
# print("올해는 " + str(year) + "년 입니다")

# list = ['d', 'c', 'a', 'b']
# list.reverse()
# # print("리스트 항목 순서 뒤집기 ", list) reverse 와 같음!!! 주석해도 결과는 같음 중간 과정이 요약된 것
# # list.sort()
# print("리스트 항목 정렬하기 ", list)
# list.sort(reverse=True)
# print("리스트 항목 역정렬하기 ", list)
# for index, value in enumerate(list):
#     print("인덱스", index, "위치의 값은 ", value)

# str = "나는 문자열"
# print(str)
# n = 3
# print(str(n))

# 함수보다 변수가 먼저임!!!

# 사용자 정의 함수


# import random

# # n = random.randint(1, 6)
# # print("결과 ", n)
# # n = random.randint(1, 6)
# # print("결과 ", n)
# # n = random.randint(1, 6)
# # print("결과 ", n)

# def rolling_dice():
#     n = random.randint(1, 6)
#     print("육면 주사위 굴린 결과 : ", n)


# rolling_dice()

# rolling_dice()

# rolling_dice()


# rolling_dice()

# rolling_dice()

# rolling_dice()