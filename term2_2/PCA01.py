# import pandas as pd
# import numpy as np
# from sklearn.decomposition import PCA
# from sklearn import preprocessing
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler


# x=pd.read_csv('it_data\\dataX.csv')
# y=pd.read_csv('it_data\\dataY.csv')
# data=pd.read_csv('it_data\\data.csv')
# pca = PCA(n_components=2)
# principalComponents = pca.fit_transform(data)
# principalDataframe = pd.DataFrame(data = principalComponents, columns = ['PC1', 'PC2'])

# import pandas as pd
# from sklearn.decomposition import PCA
# from sklearn.preprocessing import StandardScaler
# import numpy as np

# # Load the dataset
# data = pd.read_csv('it_data\\data.csv')
# # Apply PCA
# pca = PCA(n_components=2)

# # Standardize the dataset
# principalComponents = pca.fit_transform(data)

# principalDataframe = pd.DataFrame(data = principalComponents, columns = ['PC1', 'PC2'])

# # Variance of PC1 and PC2
# variance_pc1_pc2 = pca.explained_variance_

# # Eigenvectors and Eigenvalues
# eigenvectors = pca.components_
# eigenvalues = pca.explained_variance_

# # Display results
# print("Variance of PC1 and PC2:", variance_pc1_pc2)
# print("\nCovariance Matrix:\n", cov_matrix)
# print("\nEigenvectors:\n", eigenvectors)
# print("\nEigenvalues:\n", eigenvalues)

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv('it_data\\data.csv')

# Apply PCA
pca = PCA(n_components=2)

# Fit PCA to the dataset
principalComponents = pca.fit_transform(data)

# Create a DataFrame for principal components
principalDataframe = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2'])

kmeans = KMeans(n_clusters=2)  # กำหนดจำนวนกลุ่มที่ต้องการ
kmeans.fit(principalDataframe)

# ทำนายกลุ่มของข้อมูล
labels = kmeans.predict(principalDataframe)

# Variance of PC1 and PC2
variance_pc1_pc2 = pca.explained_variance_

# Eigenvectors and Eigenvalues
eigenvectors = pca.components_
eigenvalues = pca.explained_variance_

# Compute the Covariance Matrix of the original data
cov_matrix = np.cov(data.T)

# Display results
print("Variance of PC1 and PC2:", variance_pc1_pc2)
print("\nCovariance Matrix:\n", cov_matrix)
print("\nEigenvectors:\n", eigenvectors)
print("\nEigenvalues:\n", eigenvalues)

# Plot original and PCA-transformed data
plt.figure(figsize=(10, 7))

# Original Data (using the first two features)
plt.scatter(data.iloc[:, 0], data.iloc[:, 1], c='blue', marker='o', label='Original Data')

# PCA-Transformed Data
plt.scatter(principalDataframe['PC1'], principalDataframe['PC2'], c='green', marker='x', label='PCA Transformed Data')

# Add titles, labels, and legend

plt.title('Original vs PCA Transformed Data')
plt.xlabel('X-axis (Feature 1 / PC1)')
plt.ylabel('Y-axis (Feature 2 / PC2)')
# plt.axhline(0, color='red', linestyle='--', linewidth=0.8)  # Horizontal axis
# plt.axvline(0, color='red', linestyle='--', linewidth=0.8)  # Vertical axis
plt.legend()
plt.grid(alpha=0.5)
# Show plot
plt.show()

plt.figure(figsize=(10, 7))
plt.scatter(principalDataframe['PC1'], principalDataframe['PC2'], c='green', marker='o', label='PCA Transformed Data')
# สร้าง decision boundary
x_min, x_max = principalDataframe['PC1'].min() - 1, principalDataframe['PC1'].max() + 1
y_min, y_max = principalDataframe['PC2'].min() - 1, principalDataframe['PC2'].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# วาด decision boundary
plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')

plt.title('PCA Transformed Data')
plt.xlabel('Principal Component 1 (PC1)')
plt.ylabel('Principal Component 2 (PC2)')
# plt.axhline(0, color='red', linestyle='--', linewidth=0.8)  # Horizontal axis
# plt.axvline(0, color='red', linestyle='--', linewidth=0.8)  # Vertical axis
plt.legend()
plt.grid(alpha=0.5)

# Show plot
plt.show()

