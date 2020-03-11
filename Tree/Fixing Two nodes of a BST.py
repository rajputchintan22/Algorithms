# User function Template for python3
def myMapper(root, hash, ans):
    if root.left:
        myMapper(root.left, hash, ans)
    hash[root.data] = root
    ans.append(root.data)
    if root.right:
        myMapper(root.right, hash, ans)


def correctBST(root):
    hash = {}
    ans = []
    ans2 = []
    myMapper(root, hash, ans)
    counter = 2
    temp = 0
    if len(ans) > 1:
        if ans[-1] < ans[-2]:
            ans2.append(ans[-1])
            counter -= 1
            temp = ans[-1]
        if ans[0] > ans[1]:
            ans2.append(ans[0])
            temp = ans[0]
            counter -= 1
    if counter == 2:
        for i in range(1, len(ans) - 1):
            if ans[i - 1] < ans[i + 1] < ans[i] or ans[i] < ans[i - 1] < ans[i + 1]:
                temp = ans[i]
                ans2.append(ans[i])
                counter -= 1
                break
    if counter == 1:
        for i in range(1, len(ans) - 1):
            if ans[i - 1] < temp < ans[i + 1] and (
                    ans[i - 1] < ans[i + 1] < ans[i] or ans[i] < ans[i - 1] < ans[i + 1]):
                counter -= 1
                ans2.append(ans[i])
                break

    if counter == 0:
        r1 = hash[ans2[0]]
        r2 = hash[ans2[1]]
        r1.data, r2.data = r2.data, r1.data
    return root


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict  # default dict used as a map, to store node-value mapping.


# Contributed by : Nagendra Jha

# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)

    def Insert(self, parent, child, dir):
        if self.root is None:
            root_node = Node(parent)
            child_node = Node(child)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node

            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node

            return

        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        self.map_nodes[child] = child_node

        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node

        return


# driver checker list
check = []


def Inorder(root):
    if root is None:
        return
    Inorder(root.left)  # left subtree
    check.append(root.data)
    Inorder(root.right)  # right subtree
    return


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list

        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.
        root = correctBST(tree.root)
        Inorder(root)  # list shld be sorted
        check_sorted = check[:]
        check_sorted.sort()

        if check_sorted == check:
            print(1)
        else:
            print(0)
        check = []
# } Driver Code Ends