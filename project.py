# 프로젝트명 : 삐삐는 아이디
# 기능
# 1. 랜덤 아이디 생성하기 (입력 -> 생성 -> 의미확인)
# 2. 삐삐 숫자 암호 의미 분석 (분석 후 직접 아이디 생성)
# 3. 나만의 숫자 삐삐 암호 만들기
# 4. 숫자 암호 관련 정보 확인하기

import random
from ast import While
from csv import excel
from operator import index, indexOf
# 랜덤 아이디 생성하기
from random import Random

import pandas as pd
#웹프레임워크
from flask import Flask
# 엑셀 파일 읽기
from pandas import read_excel

app = Flask(__name__)

# 엑셀 파일 읽기
data = pd.read_excel('F:\파이썬프로젝트_Id\db.xlsx')
li = []
passli = []

data2 = pd.read_excel('F:\파이썬프로젝트_Id\idname.xlsx')
li2 = []
passli2 = []

# 0을 입력받을 때까지 반복하는 while문
def WhileCodeProg():
    choi = 1
    while choi != 0:
        print("🐣"*20)
        print()
        print("0번. 프로그램 종료")
        print("1번. 삐삐는 아이디 생성")
        print("2번. 아이디 의미 목록")
        print("3번. 나만의 숫자 암호 만들기")
        print("4번. 숫자 암호 연결 게임")
        print()
        print("🐣"*20)
        print()

        choi = int(input("숫자를 선택해주세요 (ex. 1 / 2 ...): "))

        if choi == 1:
            # 엑셀 파일의 숫자 암호 리스트li에 담기
            for i in range(len(data['암호'])):
                li.append(data['암호'][i])

            # 엑셀 파일의 인스타 아이디 리스트li2에 담기
            for i in range(len(data2['아이디'])):
                li2.append(data2['아이디'][i])

            # 엑셀 파일의 암호 의미 리스트 passli에 담기
            for i in range(len(data['의미'])):
                passli.append(data['의미'][i])

            # 엑셀 파일의 암호 의미 리스트 passli2에 담기
            for i in range(len(data2['의미'])):
                passli2.append(data2['의미'][i])

            # 리스트 li안에 있는 숫자 암호 랜덤으로 하나 makeId에 주기
            makeId = random.sample(li, 1)
            ind = li.index(makeId)

            # 리스트 li2안에 있는 숫자 암호 랜덤으로 하나 makeId2에 주기
            makeId2 = random.sample(li2, 1)
            ansId = ' '.join(map(str, makeId2))
            ind2 = li2.index(ansId)

            # [] 빠져나오기
            makeId = str(makeId).strip('[]')
            id_mean = str(passli[ind]).strip('[]')

            # [] 빠져나오기
            id_mean2 = str(passli2[ind2]).strip('[]')

            print("생성할 아이디의 종류를 선택해주세요.😁 ")
            print("1. 일반적인 암호 생성하기 (ex. 이름_삐삐숫자암호)")
            print("2. 인스타 아이디 생성하기 (ex. 영어단어_숫자암호)")
            print("3. 프로그램 나가기")

            cho = int(input("선택을 해 주세요: "))
            # 1,2,3 이외의 숫자가 나오면 계속 다시 선택
            while cho != 1 and cho != 2 and cho != 3:
                print("올바른 번호가 아닙니다. 확인해주세요")
                cho = int(input("다시 선택 해 주세요 : "))
            print()
            if cho == 1:
                ID = input("\n이름을 입력해주세요 : ")
                # 생성된 아이디 출력
                print("\n생성된 아이디 : ", ID, "_", makeId, "\n")
                # 의미 보여주기
                print("아이디 의미 : ", ID, "_", id_mean)

            if cho == 2:
                print("인스타 아이디 생성")
                # 생성된 아이디 출력
                print("\n생성된 인스타아이디 : ", ansId, "_", makeId, "\n")
                # 의미 보여주기
                print("영어 단어 아이디 의미 : ", ansId, " : ", id_mean2)
                print("숫자 암호 의미 : ", makeId, " : ", id_mean)
            elif cho == 3:
                print("프로그램을 종료하겠습니다.")
                break

        if choi == 2:
            print(data)
            print(data2)
        if choi == 3:
            print("나만의 의미있는 암호 만들기")
            print("1. 인스타 아이디 의미 만들기 (ex. idylic 그림같은")
            print("2. 삐삐 숫자 아이디 만들기 ex(6515 보고싶어)")
            print("3. 프로그램 종료")

            makeId = int(input("선택해주세요 > "))
            while makeId != 1 and makeId != 2 and makeId != 3:
                print("잘못된 선택 번호 입니다. ")
                makeId = int(input("다시 선택해주세요 : "))
            if makeId == 1:
                password = input("인스타 아이디를 입력해주세요. : ")
                psmean = input("의미를 입력해주세요. : ")
                
            elif makeId == 2:
                password = int(input("숫자 암호를 입력해주세요. : "))
                psmean = input("의미를 입력해주세요 : ")
            elif makeId == 3:
                print("프로그램을 종료하겠습니다.")
                break

        if choi == 4:
            print("숫자 암호 연결 게임")
        if choi == 0:
            print("프로그램 종료")
            break

WhileCodeProg()
