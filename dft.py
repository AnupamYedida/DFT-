import scipy
import numpy as np 
import matplotlib.pyplot as plt 
import random 

def rand_data_creation():
	T = 0
	rand_nums = []
	while(T<1000):
		rand_nums.append(100+50*np.sin(T*((np.pi)/20))+random.randint(-25,25))
		T = T+1
	return rand_nums

def periodic_function():
	T = 0
	periodic_function_form = []
	while(T<1000):
		periodic_function_form.append(np.sin(T*((np.pi)/20))+(np.sin(T*((np.pi)/50))))
		T = T+1
	return periodic_function_form 

def dft():
	input = raw_input ("Please Press 1 for a perfect sinusoidal wave: \nPlease Press 2 for a sinusoidal wave with noise: ")
	
	if input == '1':
		data = periodic_function()
	elif input == '2':
		data = rand_data_creation()
	else :
		print "Wrong Input !"
		exit()
	data_length = len(data)
	x_im = []
	x_re = []

	n = 0
	k = 0
	container = 0
	container_2 = 0

	while (n<data_length):
		while(k<data_length):
			container= container + data[k]*np.cos(2*np.pi*k*n/1000)
			k=k+1
		x_re.append(container)
		container = 0
		k = 0
		n = n +1
		
	n=0
	k=0
	
	while (n<data_length):
		while (k<data_length):
			container_2 = container_2 - data[k]*np.sin(2*np.pi*k*n/1000)
			k = k+1
		x_im.append(container_2)
		container_2  = 0
		k = 0
		n = n+1
		
	i=0
	container_3 = 0
	amplitudes = []
	while (i<1000):
		container_3 = np.sqrt((x_im[i]*x_im[i] + x_re[i]*x_re[i]))
		amplitudes.append(container_3/1000)
		i = i+1
		container_3 = 0
	
	plt.plot(data)
	plt.plot(amplitudes)
	plt.show()	
		
dft()	
