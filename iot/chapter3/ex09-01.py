# lol=[[1,2,3,],[4,5],[6,7,8,9]]

# print(lol[0])
# print(lol[2][1])

# for a in lol:
#     for b in a:
#         print(b, end=" ")
#     print()

# for a in lol:
#     print(a, end=" ")
#     print()

# for sub in lol:
#     for item in sub:
#         print(item, end=" ")
#     print()

# score = [
#  [88, 76, 92, 98],
#  [65, 70, 58, 82],
#  [82, 80, 78, 88]
# ]

# total = 0
# totalsub =0

# for student in score:
#     subject_total = 0
#     for subject in student:
#         subject_total += subject
#
#     subjects = len(student)
#     # print(len(student))
#     print("총점 %d, 평균 %.2f" % (subject_total, subject_total/subjects))
#     total += subject_total
#     totalsub += subjects

# print(score[0])
# print("전체평균 %.2f" % (total/totalsub))
#
# nums = [ n*2 for n in range(1, 11)]
#
# print(nums)
#
# perf=nums.index(16)
# print("점수는 %d 입니다."%perf)

# score = [88, 95, 70, 100, 99]
# score.sort()
# print(score)
# score.reverse()
# print(score)
# score.sort(reverse=True)
# print(score)

# country = ["Korea", "japan", "CHINA", "america"]
# country.sort()
# print(country)
# country.sort(key= str.upper)
# print(country)

# names="이", "김", "강"
# lee, kim, kang= names
# print(lee)
# print(kim)
# print(kang)

# import time
#
# def gettime():
#     now = time.localtime()
#     return now.tm_hour, now.tm_min
#
# result = gettime()
# print("지금 %d시 %d분 입니다."%(result[0],result[1]))
#
# hour,minute = gettime()
#
# print("지금 %d시 %d분 입니다."%(hour,minute))

# d,m=divmod(7,3)
#
# print("몫",d)
# print("나머지",m)
#
# score=[88,95,70,100,99]
# tu=tuple(score)
# print(tu)
# li=list(tu)
# li.pop(1)
# li[0]=100,100
# print(li)
