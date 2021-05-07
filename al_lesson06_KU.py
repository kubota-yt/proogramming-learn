y=[5,20,6,15,18,2,8,11,9,1,23,12]
z = 0
for i in range(len(y)):
	if y[i] > z:
		z = y[i]
print(z)