import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iris_data.csv")
pairs = [("SepalLengthCm", "SepalWidthCm"),("SepalLengthCm", "PetalLengthCm"),("SepalLengthCm", "PetalWidthCm"),("SepalWidthCm", "PetalLengthCm"),("SepalWidthCm", "PetalWidthCm"),("PetalLengthCm", "PetalWidthCm")]
plt.figure(figsize=(16, 9))
for number in range(6):
    x_name, y_name = pairs[number]
    x = list(data[x_name])
    y = list(data[y_name])
    x_sum = 0
    y_sum = 0
    for i in range(len(x)):
        x_sum += x[i]
        y_sum += y[i]
    x_mean = x_sum / len(x)
    y_mean = y_sum / len(y)
    numerator = 0
    denominator = 0
    for i in range(len(x)):
        numerator += (x[i] - x_mean) * (y[i] - y_mean)
        denominator += (x[i] - x_mean) ** 2
    k = numerator / denominator
    b = y_mean - k * x_mean
    x_min = x[0]
    x_max = x[0]
    for i in range(1, len(x)):
        if x[i] < x_min:
            x_min = x[i]
        if x[i] > x_max:
            x_max = x[i]
    y_min = k * x_min + b
    y_max = k * x_max + b
    plt.subplot(2, 3, number + 1)
    plt.scatter(x, y)
    plt.plot([x_min, x_max], [y_min, y_max], color="red")
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title(y_name + " от " + x_name)
    plt.grid()
plt.tight_layout()
plt.show()
