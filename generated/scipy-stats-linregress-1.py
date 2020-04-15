import matplotlib.pyplot as plt
from scipy import stats

# Generate some data:

np.random.seed(12345678)
x = np.random.random(10)
y = 1.6*x + np.random.random(10)

# Perform the linear regression:

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("slope: %f    intercept: %f" % (slope, intercept))
# slope: 1.944864    intercept: 0.268578

# To get coefficient of determination (R-squared):

print("R-squared: %f" % r_value**2)
# R-squared: 0.735498

# Plot the data along with the fitted line:

plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.legend()
plt.show()

# Example for the case where only x is provided as a 2x2 array:

x = np.array([[0, 1], [0, 2]])
r = stats.linregress(x)
r.slope, r.intercept
# (2.0, 0.0)
