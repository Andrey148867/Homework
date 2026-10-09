import random                      
import matplotlib.pyplot as plt    
part = 1000  # 1 часть - создание списка с положением частиц
step = 1000      
positions = [0] * part
steps = []
sigma = []


for i in range(step):
    for j in range(part):
        rand = random.randint(0, 1)
        if rand == 0:
            positions[j] = positions[j] - 1
        else:
            positions[j] = positions[j] + 1
    sumsquers = 0
    for j in range(part):
        sumsquers = (sumsquers + positions[j] ** 2)
    sigma0 = (sumsquers/part)**0.5
    steps.append(i + 1)
    sigma.append(sigma0)
t_sigma = []
for i in range(1, step + 1):
    t_sigma.append(i ** 0.5)


#гистограмма
plt.hist(positions,bins=31,edgecolor="black") # 2 часть построение двух графиков
plt.xlabel("Положение частицы x")
plt.ylabel("Количество частиц")
plt.title("Положения 1000 частиц после 1000 шагов")
plt.grid()
plt.show()

#зависимость итогового отклонения от теоретического
plt.plot(steps,sigma,label="Результат моделирования")
plt.plot(steps,t_sigma,label="Теория: СКО = N ** 0.5")
plt.xlabel("Количество шагов N")
plt.ylabel("Среднеквадратичное отклонение")
plt.title("Зависимость СКО от количества шагов")
plt.legend()
plt.grid()
plt.show()

