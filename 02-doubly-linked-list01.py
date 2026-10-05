# head node method
class Node:
    def __init__(self, data=None):
        self.data = data
        self.llink = None  # 이전(선행) 노드를 가리키는 포인터
        self.rlink = None  # 다음(후행) 노드를 가리키는 포인터


class DoublyLinkedList:
    def __init__(self):
        # 경계 조건 처리를 위해 더미(Dummy) head와 tail 노드를 생성합니다.
        self.head = Node()
        self.tail = Node()
        
        # head와 tail을 서로 연결합니다.
        self.head.rlink = self.tail
        self.tail.llink = self.head

    def insert(self, before, data):
        """before 노드 바로 뒤에 새 노드를 삽입합니다."""
        newnode = Node(data)

        newnode.llink = before
        newnode.rlink = before.rlink
        before.rlink.llink = newnode
        before.rlink = newnode

        return newnode

    def search(self, data):
        """data 값을 가진 첫 번째 노드를 탐색하여 반환합니다. (없으면 None)"""
        p = self.head.rlink
        while p != self.tail:
            if p.data == data:
                return p
            p = p.rlink
        return None

    def delete(self, target):
        """지정된 노드(target)를 리스트에서 삭제합니다."""
        # 삭제 대상이 없거나, 더미 노드인 경우 동작하지 않음
        if target is None or target == self.head or target == self.tail:
            return

        target.llink.rlink = target.rlink
        target.rlink.llink = target.llink

    def print_list(self):
        """리스트의 모든 노드를 순서대로 출력합니다."""
        p = self.head.rlink
        elements = []
        while p != self.tail:
            elements.append(str(p.data))
            p = p.rlink
        print(" <-> ".join(elements))


# --------------------------------
# Test
# --------------------------------
if __name__ == "__main__":
    L = DoublyLinkedList()

    print("1. 노드 삽입 테스트")
    n1 = L.insert(L.head, 10)  # head 뒤에 10 삽입
    n2 = L.insert(n1, 20)      # n1(10) 뒤에 20 삽입
    n3 = L.insert(n2, 30)      # n2(20) 뒤에 30 삽입
    L.print_list()             # 출력: 10 <-> 20 <-> 30

    print("\n2. 탐색 테스트 (20 검색)")
    found = L.search(20)
    print(f"찾은 노드 데이터: {found.data if found else '없음'}")

    print("\n3. 노드 삭제 테스트 (20 삭제)")
    L.delete(n2)
    L.print_list()             # 출력: 10 <-> 30