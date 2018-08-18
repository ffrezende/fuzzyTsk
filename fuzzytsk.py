#Fuzzy TSK para a aproximacao X e Y:
import numpy as np
import matplotlib.pyplot as plt
x=[]
y=[]
w1=[]
w2=[]
z1=[]
z2=[]
betas=[[0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]]

betasX=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

arq = open('entry.txt', 'r')
text = arq.readlines()
for line in text :
    x.append(float(line.split(' ')[0]))
    y.append(float(line.split(' ')[1].split('\n')[0]))
arq.close()

for i in x :
    w1.append(i*(1))
    w2.append(-1*abs(i)+1)

i=0
for i in range(12):
    betas[0][i] = (w1[i]/(w1[i] + w2[i]))
    betas[1][i] = ((w2[i]/w1[i] + w2[i]))
i=0
for i in range(12):
    betasX[i][0] = betas[0][i]
    betasX[i][1] = betas[1][i]
    betasX[i][2] = betas[0][i]*w1[i]
    betasX[i][3] = betas[1][i]*w2[i]

betasXPseInv = np.linalg.pinv(betasX)
P = np.dot(betasXPseInv,y)
i=0 
for i in range(12):
    z1.append(P[0]*x[i] + P[2])
    z2.append(P[1]*x[i] + P[3])

print z1
print z2

plt.plot(z1)
plt.plot(z2)
plt.show()