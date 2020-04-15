from scipy import stats
import matplotlib.pyplot as plt
np.random.seed(1234)  # make this example reproducible

# Generate some data and determine optimal ``lmbda``

x = stats.loggamma.rvs(5, size=30) + 5
lmax = stats.yeojohnson_normmax(x)

fig = plt.figure()
ax = fig.add_subplot(111)
prob = stats.yeojohnson_normplot(x, -10, 10, plot=ax)
ax.axvline(lmax, color='r')

plt.show()
