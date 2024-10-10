#https://codeforces.com/problemset/problem/1990/E1

from sys import stdout
import sys
sys.setrecursionlimit(5001)

class Node():
    
    def __init__(self, number) -> None:
        self.number = number
        self.parent = None
        self.children = []
        self.descendants_count = 0
        self.probabilities = 0
    
    def add_parent(self, new_parent):
        self.parent = new_parent
        new_parent.children.append(self)
        
    def print_all_childern(self):
        for i in self.children:
            print(i.number, end=" ")
        print()
              
def print_the_tree(curr_node):
    print("number:", curr_node.number, "parent:", curr_node.parent.number, "descendants_count:", curr_node.descendants_count, "probabilities:", curr_node.probabilities, "children count:", len(curr_node.children), end=" ")
    curr_node.print_all_childern()
    for i in curr_node.children:
        print_the_tree(i)

def count_all_descendants(curr_node):
    """the current node itself is also taken into account"""
    global count_of_nodes
    if not curr_node.children:
        curr_node.descendants_count = 1
        return 1
    ans = 0
    for i in curr_node.children:
        ans += count_all_descendants(i)
    curr_node.descendants_count = ans + 1
    return ans + 1

def count_all_descendants_and_delete_leaves(curr_node):
    global count_of_nodes
    global list_of_nodes
    global root
    if curr_node.number == root.number and len(curr_node.children) == 0:
        curr_node.descendants_count = 1
        return 1
    if not curr_node.children:
        curr_node.descendants_count = 0
        return 0
    ans = 0
    i = 0
    while i < len(curr_node.children):
        another_child_descendants = count_all_descendants_and_delete_leaves(curr_node.children[i])
        if another_child_descendants == 0:
            del curr_node.children[i]
            continue
        ans += another_child_descendants
        i += 1
    curr_node.descendants_count = ans + 1
    return ans + 1
          
def count_probabilities(curr_node):
    global best_probabilities
    global best_node
    curr_node.probabilities = curr_node.descendants_count / count_of_nodes
    if abs(curr_node.probabilities - 1/2) < abs(best_probabilities - 1/2):
        best_probabilities = curr_node.probabilities
        best_node = curr_node
    for i in curr_node.children:
        count_probabilities(i)
        
def delete_this_child(curr_node):
    parent = curr_node.parent
    for i in range(len(parent.children)):
        if parent.children[i].number == curr_node.number:
            del parent.children[i]
            break
        
def find_your_children(curr_node):
    global list_of_edges
    global list_of_nodes
    while list_of_edges[curr_node.number]:
        child = list_of_edges[curr_node.number].pop()
        if child == curr_node.parent.number:
            continue
        list_of_nodes[child].add_parent(curr_node)
        find_your_children(list_of_nodes[child])
        
def count_biggest_depth(curr_node, curr_depth):
    global biggest_depth
    global deepest_node
    curr_depth += 1
    if not curr_node.children:
        if curr_depth > biggest_depth:
            biggest_depth = curr_depth
            deepest_node = curr_node
            return 0
    for i in curr_node.children:
        count_biggest_depth(i, curr_depth)
    
count_inputs = int(input())
list_of_edges = []
biggest_depth = 0
deepest_node = None
for k in range(count_inputs):
    stdout.flush()
    root = None

    count_of_nodes = int(input())
    list_of_nodes = [Node(0)]
    list_of_edges = [[]]
    best_probabilities = -1
    best_node = None

    for i in range(1, count_of_nodes + 1):
        list_of_nodes.append(Node(i))
        list_of_edges.append([])
    list_of_nodes[1].add_parent(list_of_nodes[0])

    root = list_of_nodes[1]
    for i in range(count_of_nodes-1):
        x = input().split(" ")
        node1 = int(x[0])
        node2 = int(x[1])
        list_of_edges[node1].append(node2)
        list_of_edges[node2].append(node1)
    find_your_children(root)
    
    answer = 0
    count_trys = 0
    count_biggest_depth(root, 0)
    if biggest_depth <= 301:
        print("?", deepest_node.number)
        in_ans = int(input())
        if in_ans == 1:
            print("!", deepest_node.number)
            continue
        for i in range(299):
            print("?", deepest_node.number)
            in_ans = int(input())
        print ("!", 1)
        continue
    count_all_descendants(root)
    while count_trys < 300:
        count_of_nodes = root.descendants_count
        best_probabilities = -1
        best_node = None
        #print("count_of_nodes:", count_of_nodes)
        #print("root:", root.number)
        count_probabilities(root)
        #print_the_tree(root)
        print("?", best_node.number)
        in_ans = int(input())
        count_trys += 1
        if in_ans == 0:
            if root.number == 1:
                delete_this_child(best_node)
                count_all_descendants_and_delete_leaves(root)
                continue
            if count_trys < 300:
                print("?", root.number)
                in_ans = int(input())
                count_trys += 1
                if in_ans == 0:
                    answer = root.parent.parent.number
                    if answer == 0:
                        answer = 1
                    break
            delete_this_child(best_node)
            count_all_descendants_and_delete_leaves(root)
        else:
            root = best_node
    if answer == 0:
        print("!", root.number)
    else:
        print("!", answer)
   