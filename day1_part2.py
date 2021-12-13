f = open('input_1.txt', 'r')
l=[int(i.rstrip('\n')) for i in f.readlines()]
ans=0
prev=l[0]+l[1]+l[2]
for i in range(1,len(l)-2):
	if (l[i]+l[i+1]+l[i+2])>prev:
		ans+=1
	prev=l[i]+l[i+1]+l[i+2]
print(ans)
f.close()