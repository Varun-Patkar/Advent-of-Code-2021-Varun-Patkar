f = open('input_1.txt', 'r')
l=[int(i.rstrip('\n')) for i in f.readlines()]
ans=0
for i in range(len(l)-1):
	if l[i+1]>l[i]:
		ans+=1
print(ans)
f.close()
