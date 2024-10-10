#https://codeforces.com/problemset/problem/2002/F1?locale=en

primes = [1]
def sieve_of_eratosthenes(n):
    global primes
    a = [True] * (n + 1)

    i = 2
    while i * i <= n:
        if a[i] == True:
            primes.append(i)
            for j in range(i, n+1, i):
                a[j] = False
        i += 1
        
    while i <= n:
        if (a[i] == True):
            primes.append(i)
        i += 1

def find_the_nearest_prime_index(n):
    global primes
    l = 0
    r = len(primes) - 1
    while True:
        if (primes[r] == n):
            return r
        if (primes[l] == n):
            return l
        if r - l == 1:
            return l
        mid = (r + l) // 2
        if (primes[mid] < n):
            l = mid
        else:
            r = mid
            
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
   
def depth_search(a, b, n, l, f):
    ###a < b <= n
    ans = a * l + b * f
    
    if a + 1 < b and gcd(a + 1, b) == 1:
        ans = max(ans, depth_search(a+1, b, n, l, f))
    if b + 1 <= n and gcd(a, b + 1) == 1:
        ans = max(ans, depth_search(a, b + 1, n, l, f))
        
    return ans

def dp(n, l, f):
    p_n = find_the_nearest_prime_index(n)
    big_prime = primes[p_n]
    less_prime = primes[p_n - 1]
    arr = []
    ans = 0
    ##j < i <= n
    for i in range(n - big_prime + 1):
        arr.append([])
        for j in range(n - less_prime + 1):
            arr[i].append(False)
    
    for i in range(0, n - big_prime + 1):
        arr[i][0] = True
        if (less_prime) * l + (i + big_prime) * f > ans:
            ans = (less_prime) * l + (i + big_prime) * f

    for j in range(0, n - less_prime + 1):
        if j + less_prime < big_prime:
            arr[0][j] = True
            if (j + less_prime) * l + (big_prime) * f > ans:
                ans = (j + less_prime) * l + (big_prime) * f

    for i in range(1, n - big_prime + 1):
        for j in range(1, n - less_prime + 1):
            if j + less_prime >= big_prime + i:
                break
            if arr[i-1][j] == True or arr[i][j - 1] == True:
                if gcd(i + big_prime, j + less_prime) == 1:
                    arr[i][j] = True
                    if (j + less_prime) * l + (i + big_prime) * f > ans:
                        ans = (j + less_prime) * l + (i + big_prime) * f

    return ans

sieve_of_eratosthenes(20000000)

t = int(input())

for k in range(t):
    x = input().split(" ")
    n,m,l,f = int(x[0]), int(x[1]), int(x[2]), int(x[3])
    l, f = min(l, f), max(l, f)
    
    if n > 10:
        ans = dp(n, l, f)
    else:
        ans = depth_search(1, 1, n, l, f)

    # if n <= 10:
    #     ans = depth_search(1, 1, n, l, f)
    # else:
    #    p_n = find_the_nearest_prime_index(n)
    #    ans = depth_search(primes[p_n - 1], primes[p_n], n, l, f)
                   
    print(ans)