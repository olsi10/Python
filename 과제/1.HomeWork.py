from re import M


student_grade = 2
student_class = 3
student_number = 11
student_name = "최윤영"
student_height = 160.3

print(type(student_grade))
print(type(student_class))
print(type(student_number))
print(type(student_name))
print(type(student_height))

our_team = ["김비야", "김유진", "박선주", "백선미", "안소영",
            "양혜원", "이혜령", "임재연", "최윤영", "최혜민", "하도연", "하진"]


# 10번째 학생이름을 출력해보자
print(our_team[9])

# 6번째부터 9번째까지 출력해보자 // 시험문제 예상
print(our_team[5:9])

# 친구들 동아리 알아보기 과제 / 다음 주 목요일까지
club = {"김비야": "영화감상부", "김유진": "코딩클리닉",
        "박선주": "도서부", "백선미": "심리학연구반",
        "안소영": "금융경제반", "양혜원": "피구반",
        "이혜령": "교지편집부", "임재연": "또래상담반",
        "최윤영": "사진부", "최혜민": "코딩클리닉",
        "하도연": "배드민턴부", "하진": "영화감상부"}


print(club["안소영"])

print(club[our_team[0]])

#####################################################################

# 65p
a = 331
b = 17
c = '{0} / {1} = {2}'.format(a, b, a/b)
print(c)  # 19.~~

#############################

x = 37

print(pow(x, 2))

#############################

y = 10e10
print(y)

############################

d = 123 + 456j
print(d.conjugate)  # 켤레복소수

###########################

fun = "funny day"

###########################

e = fun.replace("day", "life")
print(e)

###########################

print(e.find("if"))

###########################

mon = [31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]

############################

h = 3
m = 15
h = m
m, h = h, m
# 양쪽 수 바꾸기, 교체

############################
############################
############################
############################


# 87p
