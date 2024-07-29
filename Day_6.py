# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(1, t+1):
    s = input()
    n = len(s)
    e_s = ''
    o_s = ''
    for i in range(0, n):
        if i == 0:
            e_s += s[i]
        elif i % 2 == 0:
            e_s += s[i]
        elif i % 2 == 1:
            o_s += s[i]
    print(e_s, o_s)
