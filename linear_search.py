import random
from time import time
import matplotlib.pyplot as plt

def linear_search(a):
    for i in range(1,len(a)):
        if (a[i] == a[-1]):
          return i
          break



def main():
	time_req,x_cord= [],[]
	b=1
	for i in range(1,5):
		b =b * 10
		a = random.sample(range(b),b)
		start = time()
		linear_search(a)
		end = time()
		elapsed = end - start
		time_req.append(elapsed)
		x_cord.append(b)

	plt.plot(time_req,x_cord)
	plt.show()
main()