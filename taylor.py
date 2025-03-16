# 2017
# WilC
# wilz04@gmail.com

def fac(x, b):
	if x > 1:
		return b*(x-1)*x
	else:
		return 1

def sin(x, n):
	f = 0
	y = .0
	for i in range(0, n):
		f = fac(2*i + 1, f)
		y += (-1)**i * (x**(2*i + 1))/f
		
		print("+ (-1)**%d * (%d**(2*%d + 1))/%d", i, x, i, f)
	
	return y

print sin(45, 45)
