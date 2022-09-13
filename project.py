# 프로젝트명 : 삐삐는 아이디
# 기능
# 1. 랜덤 아이디 생성하기 (입력 -> 생성 -> 의미확인)
# 2. 삐삐 숫자 암호 의미 분석 (분석 후 직접 아이디 생성)
# 3. 나만의 숫자 삐삐 암호 만들기
# 4. 숫자 암호 관련 정보 확인하기

# 랜덤 아이디 생성하기
# 엑셀 파일 가져오기 
from csv import excel
from operator import index, indexOf
# 랜덤 
from random import random
import pandas as pd
#엑셀 파일 읽기 
from pandas import read_excel
import random

#엑셀 파일 읽기 
data = pd.read_excel('F:\python\실습\삐삐는아이디\db.xlsx')
li = []
passli = []

while True:
    print("🖤🤍"*15)
    print()
    print("1번. 삐삐는 아이디 생성")
    print("2번. 삐삐 숫자 암호 의미")
    print("3번. 나만의 숫자 암호 만들기")
    print("4번. 재미있는 정보")
    print()
    print("🖤🤍"*15)
    print()

    choi = int(input("숫자를 선택해주세요 (ex. 1 / 2 ...): "))

    if choi == 1:
        ID = input("\n이름을 입력해주세요 : ")

        #엑셀 파일의 숫자 암호 리스트li에 담기
        for i in range(len(data['암호'])):
            li.append(data['암호'][i])

        #엑셀 파일의 암호 의미 리스트 passli에 담기
        for i in range(len(data['의미'])):
            passli.append(data['의미'][i])

        #리스트 li안에 있는 숫자 암호 랜덤으로 하나 makeId에 주기
        makeId = random.sample(li, 1)
        ind = li.index(makeId)

        #[] 빠져나오기 
        makeId = str(makeId).strip('[]')

        #생성된 아이디 출력
        print("\n생성된 아이디 : ",ID,"_",makeId, "\n")
        #의미 보여주기 
        id_mean = str(passli[ind]).strip('[]')
        print("아이디 의미 : " , ID ,"_", id_mean)

        print()
        print("-"*30)
        print("나가기 == 0 ")
        print("선택하기 == 1")
        print("-"*30)

        res = int(input("선택해주세요 : "))
        if res == 0:
            exit()
        elif res == 1:
            print("다시 선택")
        else :
            print("다시 입력하세요")
            res = int(input("선택해주세요 : "))
        break
    if choi == 2:
        print(data)
        break
    if choi == 3:
        print("나만의 숫자 암호 만들기")
        break
    if choi == 4:
        print("재미있는 정보")
        break
