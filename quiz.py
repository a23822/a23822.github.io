"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")

sum = 0
cnt = 0
for value in iu_score.values():
    sum = sum + value
    cnt = cnt + 1
avr = sum / cnt
print(avr)


# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")

#1. 반복문 작성
tmp = []
for val in score.values():
    tmp.append(val)
print(tmp)
sum2 = 0
cnt2 = 0
tot = len(tmp)
for i in range(len(tmp)):
    for val in tmp[i].values():
        sum2 = sum2 + val
        cnt2 = cnt2 + 1
avr2 = sum2 / cnt2
print(avr2)

# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")
tmperList = []
for value in city.values():
    tmperList.append(value)
print(tmperList)


sumlist = []
print(len(tmperList))
for i in range(len(tmperList)):
    sum3 = 0
    temp = tmperList[i]
    for j in range(len(temp)):
        sum3 = sum3 + temp[j]
    sumlist.append(sum3)
print("서울은 {:.2f} 입니다.".format(sumlist[0]/3))
print("대전은 {:.2f} 입니다.".format(sumlist[1]/3))
7+print("광주는 {:.2f} 입니다.".format(sumlist[2]/3))
print("부산은 {:.2f} 입니다.".format(sumlist[3]/3))


# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")
x = dict()
x['서울'] = sumlist[0]/3
x['대전'] = sumlist[1]/3
x['광주'] = sumlist[2]/3
x['부산'] = sumlist[3]/3
print(x)
#tp_min = min(x.v
#tp_max = max(x.values())
#print("가장 추웠던 곳은 {} 이며 온도는 {} 입니다.".format(x[tp_min], tp_min))
#print("가장 더운 곳은 {} 이며 온도는 {} 입니다.".format(x[tp_max], tp_max))


# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")
cnt3 = 0
for i in range(len(tmperList[0])):
    temp2 = tmperList[0]
    if temp2[i] == 2:
        cnt3 = cnt3 + 1

if cnt3 > 0:
    print("영상 2도였던 적이 있습니다")
else:
    print("없습니다.")