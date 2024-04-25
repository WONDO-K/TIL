import sys
input = sys.stdin.readline

def preorder(root):
    if root != '.':
        # 부모
        print(root,end='')
        # 왼쪽
        preorder(arr[root][0])
        # 오른쪽
        preorder(arr[root][1])

def inorder(root):
    if root != '.':
        # 왼쪽
        inorder(arr[root][0])
        # 부모
        print(root, end='')
        # 오른쪽
        inorder(arr[root][1])
def postorder(root):
    if root != '.':
        # 왼쪽
        postorder(arr[root][0])
        # 오른쪽
        postorder(arr[root][1])
        # 부모
        print(root, end='')

n = int(input())
arr = {}

for i in range(n):
    p,left,right = map(str,input().split())
    arr[p] = [left,right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
