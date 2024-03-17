import numpy as np 
import matplotlib.pyplot as plt
pi=3.141592
def a_ind(n):
    x=np.linspace(-pi,pi,1000)
    y=((
np.sin(x)+2*np.sin(2*x)+3*np.sin(3*x)+4*np.sin(4*x)+5*np.sin(5*x)+np.cos(x)+2*np.cos(2*x)+3*np.cos(3*x)+4*np.cos(4*x)+5*np.cos(5*x))*np.cos(n*x))
    if n==0 : return (np.cos(pi)-np.cos(-1*pi))/(2*pi)
    else : return (1/pi)*np.trapz(y,x)
def b_ind(n):
    x=np.linspace(-pi,pi,1000)
    y=((
np.sin(x)+2*np.sin(2*x)+3*np.sin(3*x)+4*np.sin(4*x)+5*np.sin(5*x)+np.cos(x)+2*np.cos(2*x)+3*np.cos(3*x)+4*np.cos(4*x)+5*np.cos(5*x))*np.sin(n*x))
    if n==0 : return 0
    else : return (1/pi)*np.trapz(y,x)
def funcs(z):
    func=0
    for i in range(10):
        func+=a_ind(i)*np.cos(i*z)+b_ind(i)*np.sin(i*z)
    return func    
z=np.linspace(-5,5,1000)
funk=[funcs(i) for i in z]
plt.plot(z,funk,c='k')
plt.grid(True)
x=np.linspace(-5,5,1000)
y=[(
np.sin(i)+2*np.sin(2*i)+3*np.sin(3*i)+4*np.sin(4*i)+5*np.sin(5*i)+np.cos(i)+2*np.cos(2*i)+3*np.cos(3*i)+4*np.cos(4*i)+5*np.cos(5*i)) for i in x]
plt.plot(x,y,c='red')
plt.show()