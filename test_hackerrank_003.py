"""
You are given a function f(X)= X*2. You are also given K lists. 
The i*th list consists of Nsubi elements.

You have to pick one element from each list so that the value 
from the equation below is maximized:
S=(f(X1) + f(X1) + ... + f(Xsubk)) % M

Xsubi denotes the element picked from the i*th list . Find the 
maximized value Smax obtained.

% denotes the modulo operator.

Note that you need to take exactly one element from each list, 
not necessarily the largest element. You add the squares of the 
chosen elements and perform the modulo operation. The maximum 
value that you can obtain, will be the answer to the problem.

Input Format

The first line contains 2 space separated integers K and M.
The next K lines each contains an integer Nsubi, denoting the 
number of elements in the i*th list, followed by Nsubi space 
separated integers denoting the elements in the list.

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output

206
"""

from itertools import product, repeat

if __name__ == '__main__':

    k, m = map(int, input().split())

    k_lists = [list(map(int, input().split()))[1:] for _ in range(k)]

    max_result = 0
    for vals in product(*k_lists):
        result = sum(map(pow, vals, repeat(2))) % m
        max_result = max(max_result, result)

    print(max_result)
