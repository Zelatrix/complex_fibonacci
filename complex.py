import math
import cmath
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.spines as sp

phi = ((1 + math.sqrt(5))/2)
x = 0
y = 0
z = complex(x, y)
n = 500

# Initialising lists to store the real and complex values
real = []
imag = []

# Calculating and storing the real and imaginary parts of the complex numbers
for i in range(0, n):
    z = ((phi**(i/100))-((-1/phi)**(i/100)))/math.sqrt(5)
    real.append(z.real)
    imag.append(z.imag)

# Turn the data into a format that can be stored inside of a pandas dataframe
data = {'Real': real,
        'Imaginary': imag
       }

# Create a dataframe and store the data inside it
df = pd.DataFrame(data, columns = ['Real', 'Imaginary'])

# Retrieve the values for plotting
x_vals = df['Real']
y_vals = df['Imaginary']

# Change the position of the x-axis to be centred on zero
# and hide the now-redundant spines.
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xlabel("Re(z)")
plt.ylabel("Im(z)")

# Plot and show the graph
plt.plot(x_vals, y_vals)
plt.show()
