"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

GOOGLE would have it's logo with the letters .

Input Format

A single line of input containing the string .

aabbbccde

Sample Output 0

b 3
a 2
c 2

"""
if __name__ == '__main__':
    s = input()

    d = {}
    for chtr in s:
        if chtr not in d.keys():
            d[chtr] = 1
        else:
            d[chtr] += 1

    ordered_values = sorted(d.items(), key=lambda elem: (-elem[1], elem[0]))

    for key, value in ordered_values[:3]:
        print(f"{key} {value}")
