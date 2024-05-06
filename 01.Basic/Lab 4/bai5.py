# === Bài 5 ===
print("Number with sum of digits = 9")
d = 10
s = 1000
while d:
    if sum([int(i) for i in str(s)]) == 9:
        print(s,end=' ')
        d-=1
    s+=1
print()