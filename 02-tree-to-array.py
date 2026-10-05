class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# BFS를 사용하여 이진 트리를 배열로 변환하는 함수
def tree_to_array(root):
    if root is None:
        return []

    array = []
    queue = [(root, 0)]  # (노드 객체, 해당 노드의 배열 인덱스)

    while queue:
        node, index = queue.pop(0)

        # 현재 인덱스가 배열 크기보다 크면 None으로 배열 확장
        if index >= len(array):
            array.extend([None] * (index - len(array) + 1))

        array[index] = node.key

        # 왼쪽 자식 노드 인덱스: 2 * index + 1
        if node.left:
            queue.append((node.left, 2 * index + 1))

        # 오른쪽 자식 노드 인덱스: 2 * index + 2
        if node.right:
            queue.append((node.right, 2 * index + 2))

    return array


# --------------------------------
# 사용 예시 (테스트)
# --------------------------------
if __name__ == "__main__":
    # 트리 생성
    #       1
    #      / \
    #     2   3
    #      \
    #       4
    binary_tree_root = TreeNode(1)
    binary_tree_root.left = TreeNode(2)
    binary_tree_root.right = TreeNode(3)
    binary_tree_root.left.right = TreeNode(4)

    # 트리를 배열로 변환
    array_representation = tree_to_array(binary_tree_root)
    print(array_representation)
    # 출력: [1, 2, 3, None, 4]

"""
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)  # 4의 자식 노드로 넣을 노드

# 관계 연결
root.left = node2
root.right = node3
node2.right = node4
node4.right = node5  # binary_tree_root.left.right.right 대신 node4.right 사용
"""