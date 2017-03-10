import psycopg2 as pg2
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

conn = pg2. connect(database = 'dvdrental', user = 'postgres',
                    password = 'rishabhj')

cur = conn.cursor()

cur.execute('SELECT rental_rate, COUNT(rental_rate) FROM film GROUP BY rental_rate')

rental_rates = cur.fetchall()

count = []
rental_value = []
for rental in rental_rates:
    rental_value.append(str(rental[0]))
    count.append(rental[1])
ax = plt.subplot(111)

position = np.arange(3)
width = 0.35    
ax.bar(width + position, count, width, color = 'yellow')
ax.set_xticks(position + width + width/2)
ax.set_xticklabels(rental_value)
plt.grid(False)
plt.xlabel('Rental Value')
plt.ylabel('Count')
plt.title('Total Rental Value Count', fontsize = 20)
plt.show()