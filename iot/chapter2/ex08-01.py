s= 'python'
print(s[2]) #t
print(s[-2]) #o

for c in s:
    print( c, end=",")

s= "python programming"

print(len(s)) #18
print(s.find('o')) #4
print(s.rfind('o')) #9
print(s.index('r')) #8
print(s.count('n')) #2

name="허효영"

if name.startswith("허"):
    print("성이 허입니당")

if name.startswith("김"):
    print("성이 김입니당")

file= "pr.jpg"

if file.endswith(".jpg"):
    print("jpg 그림 파일입니다")