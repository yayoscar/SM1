import matplotlib.pyplot as plt
from Dado import Dado

plt.style.use('seaborn-v0_8')
dado1=Dado()
dado2=Dado()
dado3=Dado()

Resultados=[]
Frecuencia=[]

for i in range(1000):Resultados.append(dado1.lanzar() + dado2.lanzar() + dado3.lanzar())

maximo_resultado = dado1.caras + dado2.caras + dado3.caras

for Valor in range(2,maximo_resultado+1):Frecuencia.append(Resultados.count(Valor))

#Visualizar resultado

Valores_x=list(range(2,maximo_resultado+1))
Valores_y = Frecuencia


fig,ax =plt.subplots()
ax.scatter(Valores_x,Valores_y,c='Green',s=35)
ax.plot(Valores_x,Valores_y)

ax.set_title("Cuadrados", fontsize=24, color='Red')
ax.set_xlabel("Valor", fontsize=14, color='Red')
ax.set_ylabel("Cuadrado de valor", fontsize=14,color='Red')

ax.tick_params(axis="both", labelsize=14)

plt.show()

