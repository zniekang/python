from time import sleep
import random

students = [] # 여기에 학생들 이름을 리스트로 입력
used = []

def roulette():
    global students
    global used
    num = random.randint(0, len(students)+7)
    if len(students) <= num <= (len(students)+7):
        for i in range(5):
            print(5-i)
            sleep(1)
        return "★☆★☆ 한 번 더 ! ★☆★☆"
    elif students[num] not in used:
        for i in range(5):
            print(5-i)
            sleep(1)
        used.append(students[num])
        return "★☆★☆ "+students[num]+"님 축하합니다! ★☆★☆"

while len(used) != len(students):
    response = input("아무 키나 눌러주세요!")
    p = None
    while p == None:
        p = roulette()
    print(p)
