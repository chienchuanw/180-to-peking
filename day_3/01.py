import numpy as np
import matplotlib.pyplot as plt

# 1. 產生線性資料 y = 3x + 2，加上一些隨機噪音
np.random.seed(3)  # 設定隨機種子，讓結果可重現
x = np.linspace(0, 10, 50)  # 建立從 0 到 10 的 50 個等距 x 值
noise = np.random.normal(0, 1, x.shape)  # 加入平均為 0、標準差為 1 的隨機噪音
y = 3 * x + 2 + noise  # 套用 y = 3x + 2 並加入噪音

# 2. 使用 numpy 的 polyfit 計算最佳擬合直線的斜率和截距
slope, intercept = np.polyfit(x, y, deg=1)
print(f"Fitted line: y = {slope:.2f}x + {intercept:.2f}")

# 3. 畫出原始資料點和擬合的直線
plt.scatter(x, y, color="blue", label="Data points")  # 原始資料點
plt.plot(x, slope * x + intercept, color="red", label="Fitted line")  # 擬合直線
plt.xlabel("X value")
plt.ylabel("Y value")
plt.title("Linear Regression Example")
plt.legend()
plt.grid(True)
plt.show()
