dic={"boy":"소년","school":"학교","book":"책"}
# print(dic["boy"])
# print(dic.get('boy'))
# print(dic.get('girl'))
# print(dic.get('girl','사전에 없는 단어입니다.'))
# print(dic.keys())
# print(dic.values())
# print(dic.items())

# keylist= dic.keys()
# for key in keylist:
#     print(key, dic[key])

# li= list(dic.keys())
# print(li)
# li=list(dic)
# print(li)

dic2={'student':"학생","teacher":"선생님","book":"서적"}
dic.update(dic2)
print(dic)

li=[['boy','소년'],['school','학교'],['teacher','선생님']]

dic=dict(li)

print(dic)