class TreeNode:

    def __init__(self, data):
        self.data = data  # 1. 데이터 (C의 element data)
        self.left = None  # 2. 왼쪽 포인터 (C의 struct TreeNode* left)
        self.right = None  # 3. 오른쪽 포인터 (C의 struct TreeNode* right)

"""
c 언어

typedef int element;

typedef struct TreeNode{
    element data;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

이 코드와 같다
"""