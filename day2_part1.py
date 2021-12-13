f = open('input_2.txt', 'r')
l = [i.rstrip('\n') for i in f.readlines()]
h,d=0,0
for st in l:
	if st[:7]=="forward":
		h+=int(st[8:])
	elif st[:2]=="up":
		d-=int(st[3:])
	elif st[:4]=="down":
		d+=int(st[5:])
	else:
		print("Input is bad!!😔😭")
print("Height:",h,"\nDepth:",d)
print("Ans:",h*d)
f.close()
