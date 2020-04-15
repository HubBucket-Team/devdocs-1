import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull, convex_hull_plot_2d

# The convex hull of a random set of points:

points = np.random.rand(30, 2)
hull = ConvexHull(points)

# Plot it:

_ = convex_hull_plot_2d(hull)
plt.show()
