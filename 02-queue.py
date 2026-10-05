from collections import deque

queue = deque()

# 1. Enqueue (데이터 넣기): 맨 뒤에 추가
queue.append(10)
queue.append(20)
queue.append(30)  # deque([10, 20, 30])

# 2. Peek (맨 앞 데이터 확인): 0번 인덱스 조회
print(queue[0])  # 10

# 3. Dequeue (데이터 꺼내기): 맨 앞 데이터 $O(1)$로 삭제 및 반환
data = queue.popleft()  # 10
print(queue)  # deque([20, 30])

# 4. Empty 확인 (비어있는지 확인)
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")