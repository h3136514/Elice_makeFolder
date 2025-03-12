from openpyxl import load_workbook
import datetime
import os

searchSheet = input("검색할 시트 이름을 입력해주세요: ")
search = input("관리목을 입력해주세요: ")
plus = input("관리목 코드를 입력해주세요: ")
plus += '-'

# 현재 경로 가지고오기
current_path = os.getcwd()
# 저장할 폴더 생성
try:
    if not os.path.exists("result"):
        os.mkdir("result")
except FileExistsError:
    print("error: 기존에 result라는 폴더가 있으면 삭제 부탁드립니다.")

# data_only=True로 해줘야 수식이 아닌 값으로 받아온다. 
load_wb = load_workbook(current_path +"/sample.xlsx", data_only=True)
# 시트 이름으로 불러오기 
load_ws = load_wb[searchSheet]

# 모든 행과 열 출력
for row in load_ws.rows:
    check = False
    if(row[6].value == search) :
        date = row[3].value  # D열
        Number = str(row[7].value) # H열열
        # datetime 객체를 문자열로 변환
        date_string = date.strftime("%Y.%m.%d.")
        try:
            # 폴더 생성
            os.mkdir(current_path + "/result/" + plus + date_string +"-"+ str(row[7].value))  # 현재 경로 + 폴더명 입력
        except FileExistsError:
            print("error: 파일이 이미 있으므로 만들 수 없습니다. 기존에 똑같은 이름의 폴더가 있으면 삭제 부탁드립니다.")

