def parent(total_nodes, current):
    subtree_nodes = total_nodes
    offset = 0
    while(subtree_nodes != 0):
        subtree_nodes //= 2 # remaining nodes/2
        left = offset + subtree_nodes 
        right = left + subtree_nodes
        if left == current or right == current:
            return right + 1
        # if checked node is greater than the left leaf,
        # we know to visit the right subtree
        if current > left:
            offset = left
    return -1

# root is equal to the total nodes
# every left subtree of the root has (n-1)/2 nodes which also equals the total nodes in its subtree
# every right node is the parent node - 1 forall subtrees
def solution(h,q):
    if (h not in range(1,31)) or (len(q) not in range(0,10000)):
        return -1
    p=[]
    total_nodes = pow(2,h) - 1
    for i in q:
        if i in range(1,total_nodes):
            p.append(parent(total_nodes,i))
        else:
            p.append(-1)
    return p

print(solution(5,[19,14,28]))
print(solution(3,[7,3,5,1]))
