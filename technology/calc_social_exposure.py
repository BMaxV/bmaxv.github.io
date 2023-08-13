import matplotlib.pyplot as plt

def main():
	
	
	xs=[0,10]
	ys=[-3,1]
	red=[0,0]
	plt.plot(xs,red,color="red")
	plt.xlabel("quality")
	plt.ylabel("exposure value")
	plt.plot(xs,ys)
	plt.grid()
	plt.savefig("exposure.svg")
	
if __name__ =="__main__":
	main()
