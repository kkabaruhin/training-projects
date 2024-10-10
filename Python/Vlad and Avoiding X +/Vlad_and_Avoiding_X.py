#https://codeforces.com/contest/1926/problem/F

table = []
neighbours_table = []
for i in range(7):
    table.append([])
    for j in range(7):
        table[i].append("W")
        
def check(rem):
    for i in range (1, 6):
        for j in range(1, 6):
            if (i + j) % 2 == rem:
                if table[i][j] == "B" and table[i-1][j-1] == "B" and table[i-1][j+1] == "B" and table[i+1][j-1] == "B" and table[i+1][j+1] == "B":
                    return False
    return True

def count_neighbours():
    global neighbours_table
    neighbours_table = []
    for i in range(7):
        neighbours_table.append([])
        for j in range(7):
            neighbours_table[i].append(0)
            
    for i in range(1, 6):
        for j in range(1, 6):
            if table[i][j] == "B" and table[i-1][j-1] == "B" and table[i-1][j+1] == "B" and table[i+1][j-1] == "B" and table[i+1][j+1] == "B":
                neighbours_table[i-1][j-1] += 1
                neighbours_table[i-1][j+1] += 1
                neighbours_table[i+1][j-1] += 1
                neighbours_table[i+1][j+1] += 1
                
def del_neighbours(i, j):
    if i >= 6 or i <= 0 or j >= 6 or j <= 0:
        return 1
    if table[i][j] == "B" and table[i-1][j-1] == "B" and table[i-1][j+1] == "B" and table[i+1][j-1] == "B" and table[i+1][j+1] == "B":
        neighbours_table[i-1][j-1] -= 1
        neighbours_table[i-1][j+1] -= 1
        neighbours_table[i+1][j-1] -= 1
        neighbours_table[i+1][j+1] -= 1
        
def set_white(i, j):
    del_neighbours(i-1, j-1)
    del_neighbours(i-1, j+1)
    del_neighbours(i+1, j-1)
    del_neighbours(i+1, j+1)
    if table[i-1][j-1] == "B" and table[i-1][j+1] == "B" and table[i+1][j-1] == "B" and table[i+1][j+1] == "B":
        neighbours_table[i-1][j-1] -= 1
        neighbours_table[i-1][j+1] -= 1
        neighbours_table[i+1][j-1] -= 1
        neighbours_table[i+1][j+1] -= 1
    neighbours_table[i][j] = 0
    table[i][j] = "W"
    
def add_neighbours(i, j):
    if i >= 6 or i <= 0 or j >= 6 or j <= 0:
        return 1
    if table[i][j] == "B" and table[i-1][j-1] == "B" and table[i-1][j+1] == "B" and table[i+1][j-1] == "B" and table[i+1][j+1] == "B":
        neighbours_table[i-1][j-1] += 1
        neighbours_table[i-1][j+1] += 1
        neighbours_table[i+1][j-1] += 1
        neighbours_table[i+1][j+1] += 1
        
def set_back_black(i, j):
    table[i][j] = "B"
    add_neighbours(i-1, j-1)
    add_neighbours(i-1, j+1)
    add_neighbours(i+1, j-1)
    add_neighbours(i+1, j+1)
    if table[i-1][j-1] == "B" and table[i-1][j+1] == "B" and table[i+1][j-1] == "B" and table[i+1][j+1] == "B":
        neighbours_table[i-1][j-1] += 1
        neighbours_table[i-1][j+1] += 1
        neighbours_table[i+1][j-1] += 1
        neighbours_table[i+1][j+1] += 1
    
def whiting_some_cells(count, rem):
    global neighbours_table
    global table
    if (count == 0):
        return check(rem)
    
    for i in range (1, 6):
        for j in range(1, 6):
            if (neighbours_table[i][j] > 0 and (i+j) % 2 == rem):
                set_white(i, j)
                ans = whiting_some_cells(count - 1, rem)
                set_back_black(i, j)
                if ans:
                    return True
                
    return False
            
count_in = int(input())

for k in range(count_in):
    for i in range(7):
        x = input()
        for j in range(7):
            table[i][j] = x[j]
    count_neighbours()
    ans = 0
    for rem in range(0, 2):
        for j in range(0, 5):
            if whiting_some_cells(j, rem):
                ans += j
                break
    print(ans)

            

