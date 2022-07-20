import sys
input=sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent[x])
    return x

    #         parent[x] = find_parent(parent[x])
    # return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(a, b):  
    a = find_parent(a) #F F F
    b = find_parent(b) #B V W
    if a!=b:
        parent[b] = a
        number[a]+=number[b]

N = int(input())

for i in range(N):
    F = int(input())
    parent={}
    number={}
    for j in range(F):
        f1,f2 = input().split()
        if f1 not in parent.keys():
            parent[f1]=f1
            number[f1]=1
        if f2 not in parent.keys():
            parent[f2]=f2
            number[f2]=1
        union_parent(f1,f2)
        print(number[find_parent(f1)])
