import matplotlib.pyplot as plt
%matplotlib inline

plt.figure(figsize=(4,4))
plt.plot([0,3,4,5], [0,6,12,24],label="graph")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("title")
plt.legend()
plt.show()


import numpy as np

x=np.linspace(0, 10, 20)
print(x)
y=x**2
z=(x-1)**3
plt.plot(x, y, label="y=x^2")
plt.plot(x, z, label="z=(x-1)^3")
plt.legend()

### グラフを3つに分ける
### subplot(１行、３列、何番目)

plt.figure(figsize=(12, 4)) #全体

plt.subplot(1, 3, 1)
plt.plot(x, y, label="y=x^2")
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(x, z, label="z=(x-1)^3")
plt.legend()


# データのインポート
import pandas as pd
tips = pd.read_csv("パス.csv") # CSV形式のデータを読み込む
