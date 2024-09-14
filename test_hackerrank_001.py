"""
Example


There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'. 
The first substring is all 'A' characters, so . The second substring has 
all distinct characters, so . The third substring has  different characters, 
so . Note that a subsequence maintains the original order of characters 
encountered. The order of characters in each subsequence shown is important.

Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

string s: the string to analyze
int k: the size of substrings to analyze

Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
"""
def merge_the_tools(string, k):
    # your code goes here
    l_string = len(string)
    part_size = l_string // k

    for i in range(part_size):
        start = i * k
        end = start + k
        c = set(string[start:end])
        print("".join(c))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
