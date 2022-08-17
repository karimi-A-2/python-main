n = int(input())
orgs = []
for i in range(n):
    org = input()
    orgs.append(org)
    
q = int(input())
out = 0
tmp_set = set()
for i in range(q):
    org = input()
    tmp_set.add(org)
    if len(tmp_set) == len(orgs):
        out += 1
        tmp_set.clear()
        tmp_set.add(org)

print(out)

