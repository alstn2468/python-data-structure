# Deque.py

# collections 모듈 선언
import collections

# 덱 모듈 클래스 선언
deque = collections.deque()

# 덱 데이터 삽입
deque.append(10), deque.appendleft(20)
deque.append(30), deque.appendleft(40)
deque.append(50), deque.appendleft(60)

# 덱 데이터 출력
print('Add Data')
print(deque)
'''
Add Data
deque([60, 40, 20, 10, 30, 50])
'''

# 덱 데이터 삭제
print('Pop : %d' % deque.pop())
print('Pop Left : %d' % deque.popleft())
'''
Pop : 50
Pop Left : 60
'''

# 데이터 삭제 후 덱 데이터 출력
print('After Pop')
print(deque)
'''
After Pop
deque([40, 20, 10, 30])
'''

# 덱 역순 변경
deque.reverse()
print('After Reverse')
print(deque)
'''
After Reverse
deque([30, 10, 20, 40])
'''
