#과제 1 . 4개의 과목 합계(개인합계 / 전체합계) / 평균(개인 평균 / 전체 평균)
# 홍길동1 '국어: 95', '영어:'90, '수학:'80, 과학:50
# 홍길동2 '국어: 100', '영어:'50, '수학:'90, 과학:90
# 홍길동3 '국어: 99', '영어:'60, '수학:'100, 과학:40
# 홍길동4 '국어: 55', '영어:'80, '수학:'80, 과학:60

#for / while / if / elif
#7가지 방법으로 코드를 작성 : 결과는 모두 같아야함


홍길동1 = {'국어':95, '영어':90, '수학':80, '과학':50}
홍길동2 = {'국어':100, '영어':50, '수학':90, '과학':90}
홍길동3 = {'국어':99, '영어':60, '수학':100, '과학':40}
홍길동4 = {'국어':55, '영어':80, '수학':80, '과학':60}

#list = [Score1,Score2,Score3,Score4]

total1=0
total2=0
total3=0
total4=0

for AvgData in 홍길동1: 
    name1 = '홍길동1'
    total1 = total1 + 홍길동1[AvgData]
    value1 = total1 / len(홍길동1)
print('이 름', name1)
print('총 점:', total1)
print('평 균:', value1)

print()

for AvgData in 홍길동2: 
    name2 = '홍길동2'
    total2 = total2 + 홍길동2[AvgData]
    value2 = total2 / len(홍길동2)
print('이 름', name2)
print('총 점:', total2)
print('평 균:', value2)

print()

for AvgData in 홍길동3: 
    name3 = '홍길동3'
    total3 = total3 + 홍길동3[AvgData]
    value3 = total3 / len(홍길동3)
print('이 름', name3)
print('총 점:', total3)
print('평 균:', value3)

print()

for AvgData in 홍길동4: 
    name4 = '홍길동4'
    total4 = total4 + 홍길동4[AvgData]
    value4 = total4 / len(홍길동4)
print('이 름', name4)
print('총 점:', total4)
print('평 균:', value4)

#for AvgData in (Score1, Score2,Score3,Score4):

#print('총 점:', total3)
#print('평 균:', value3)
