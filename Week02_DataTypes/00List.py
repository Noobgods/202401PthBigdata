a = []                      # 비어있는 리스트 선언
b = [1, 2, 3]               # 숫자 저장
c = ['a', 'b', 'c', 'Life'] # 문자 저장
d = [1, 2, 'a', 'b']        # 자료형 섞어서 저장
e = [1, 2, [1, 2, 3]]       # 리스트 안에 리스트 저장
f = list([1, 2, 3])         # 리스트 클래스 생성

# 인덱싱과 슬라이싱
## 인덱싱 
d[2]    #'a'
d[-1]   #'b'
e[2]

e[2][1]

## 슬라이싱
e[0:2]
e[2][0:-2]

# 리스트의 수정과 삭제
e[1] = 4    # 수정

del e[0]    # 삭제
del e[1][1:]     # 삭제 (슬라이싱과 2차원 리스트)

list = [1,2, 'A', 'a', ["Life", "Is"], '  Too', 'Short  '] # 여러가지 자료형을 담은 리스트 선언
list.insert(3, 'B')     # list[3] 위치에 'B' 삽입  
# list = [1, 2, 'A', 'B', 'a', ['Life', 'Is'], '  Too', 'Short  ']
