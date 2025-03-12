# Elice_makeFolder
해당 프로그램은 (주)엘리스그룹에서 2024년 디지털새싹 사업 정산 관련 업무를 진행하다가 업무의 효율화를 위해 개발한 자동화 프로그램이다.


## <배경>
정산 관련하여 폴더 형식을 “관리목코드-집행일자-집행순번” 순서로 만들어야 됐습니다. 처음에는 수동으로 만들다가 회의비나 강사료와 같이 수백개가 넘는 것을 일일이 액셀에서 옮겨 적을 수 없어 이를 파이썬을 이용해서 자동화를 진행하였다.

## <동작 방식>
콘솔창에서 검색할 시트의 이름과 관리목 이름(G열), 관리목 코드들을 입력받아서 해당 액셀 시트에 있는 관리목을 기준으로 관리목코드 + 집행일자(D열) +관리목No(H열) 순서로 파일을 자동 생성하게 구현했습니다. 
(실행파일’을 압축을 풀고 dist라는 폴더 안에서 'folderName.exe’파일을 실행하면 됩니다.)
![2](https://github.com/user-attachments/assets/d40a220b-14e0-4fb7-ab25-44657397d51a)
 <div align="center">액셀 내용</div><br>
 
![7](https://github.com/user-attachments/assets/92f37a9e-a57d-41d6-8dac-a817145cb007)
 <div align="center">관리목별 폴더들</div><br>

 ## <주의 사항>
실행파일을 압축을 풀고 검색할 액셀 시트를 dist 폴더안에 넣어주고 이름을 “sample.xlsx“로 변경해 줘야 합니다.

![3](https://github.com/user-attachments/assets/b68625c7-83ce-4684-87ea-8825d4c7e64a)

![8](https://github.com/user-attachments/assets/54d9af90-a11d-400e-ae84-6bccbf57de52)
<div align="center">콘솔창 입력</div><br>

그 결과 폴더들이 들어 있는 result 폴더가 생성된걸 확인 할 수 있습니다.

![6](https://github.com/user-attachments/assets/2891019b-4985-478e-ac59-02b73338bd1d)
<div align="center">result 폴더</div><br>

![7](https://github.com/user-attachments/assets/0e22a757-1d2d-4209-a252-c95469d8a859)
<div align="center">해당 관리목 코드에 대응하는 폴더 생성(result 폴더 안)</div><br>
