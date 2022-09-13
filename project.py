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

ID = input("이름을 입력해주세요 : ")
#엑셀 파일 읽기 
data = pd.read_excel('F:\python\실습\삐삐는아이디\db.xlsx')
li = []
passli = []

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
print("아이디 의미 : " , id_mean)

#삐삐 숫자 암호 의미
# print(data)
# data['암호']

