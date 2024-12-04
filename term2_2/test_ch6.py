from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

# โหลดข้อมูล
data = pd.read_csv('it_data\\data.csv')

# ทำ PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(data)
principalDataframe = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2'])

# ใช้ KMeans เพื่อแบ่งกลุ่มข้อมูล
kmeans = KMeans(n_clusters=2)  # กำหนดจำนวนกลุ่มที่ต้องการ
kmeans.fit(principalDataframe)

# ทำนายกลุ่มของข้อมูล
labels = kmeans.predict(principalDataframe)

# Plot Data และเส้นแบ่งการ Clustering
plt.figure(figsize=(10, 7))

# แสดงข้อมูลที่ถูกจัดกลุ่ม
plt.scatter(principalDataframe['PC1'], principalDataframe['PC2'], c=labels, cmap='viridis', marker='o', label='PCA Transformed Data')

# สร้าง decision boundary
x_min, x_max = principalDataframe['PC1'].min() - 1, principalDataframe['PC1'].max() + 1
y_min, y_max = principalDataframe['PC2'].min() - 1, principalDataframe['PC2'].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# วาด decision boundary
plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')

# แสดงผล
plt.title('K-Means Clustering with PCA')
plt.xlabel('Principal Component 1 (PC1)')
plt.ylabel('Principal Component 2 (PC2)')
plt.legend()
plt.grid(alpha=0.5)
plt.show()
