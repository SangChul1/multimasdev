# 과제 1 . 딕셔너리를 이용해서 평균 점수 구하기
#  dic = {'국어: 95', '영어:'90, '수학:'80, 과학:50}

# 과제 2. set을 이용해서 1~100까지 숫자중에 공배수를 구함
#         공배수 = 3과 5의 공배수/ 합집합 구함. 
#         (hint.표현식을 이용하면 쉽다.)

# 과제 4. 리스트데이터 list = [7,5,3,1,-1,-3,-5,-7]
#         range 활용

# 과제 5. 과제4.의 결과를 튜플로 변경(형변환)

# 개인 github 에 업로드.
#폴더 생성후 업로드
#폴더명 : MSA20220119
#파일명 : 이름_Coll.py
-----------------------------------------------------------------
# 과제1.
Score = {'국어': 95, '영어':90, '수학':80, '과학':50}
total=0
for AvgData in Score:
    total = total + Score[AvgData]
value = total / len(Score)

print('총 점:', total)
print('평 균:', value)

temp = 0

# 과제2.
setData1 = {i for i in range(101)}
setData2 = {i for i in range(101) if i % 3 == 0}
setData3 = {i for i in range(101) if i % 5 == 0}

resultData1 = setData2 & setData3 # 3과 5의 공배수
resultData2 = setData2 | setData3 # 3과 5의 합집합

print('3과 5의 공배수:', resultData1)
print('3과 5의 합집합:', resultData2)

temp = 0

# 과제3.

listData1 = list(range(-7, 8, 2))
print('List Data:', listData1)

temp=0

# 과제4.
TupleData = tuple(listData1)
print('리스트->튜플_형변환:', TupleData)

temp=0
---------------------------------------------------------------

