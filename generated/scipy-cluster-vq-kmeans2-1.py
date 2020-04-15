from scipy.cluster.vq import kmeans2
import matplotlib.pyplot as plt

# Create z, an array with shape (100, 2) containing a mixture of samples
# from three multivariate normal distributions.

np.random.seed(12345678)
a = np.random.multivariate_normal([0, 6], [[2, 1], [1, 1.5]], size=45)
b = np.random.multivariate_normal([2, 0], [[1, -1], [-1, 3]], size=30)
c = np.random.multivariate_normal([6, 4], [[5, 0], [0, 1.2]], size=25)
z = np.concatenate((a, b, c))
np.random.shuffle(z)

# Compute three clusters.

centroid, label = kmeans2(z, 3, minit='points')
centroid
# array([[-0.35770296,  5.31342524],
# [ 2.32210289, -0.50551972],
# [ 6.17653859,  4.16719247]])

# How many points are in each cluster?

counts = np.bincount(label)
counts
# array([52, 27, 21])

# Plot the clusters.

w0 = z[label == 0]
w1 = z[label == 1]
w2 = z[label == 2]
plt.plot(w0[:, 0], w0[:, 1], 'o', alpha=0.5, label='cluster 0')
plt.plot(w1[:, 0], w1[:, 1], 'd', alpha=0.5, label='cluster 1')
plt.plot(w2[:, 0], w2[:, 1], 's', alpha=0.5, label='cluster 2')
plt.plot(centroid[:, 0], centroid[:, 1], 'k*', label='centroids')
plt.axis('equal')
plt.legend(shadow=True)
plt.show()
