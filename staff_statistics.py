import psycopg2 as pg2
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

conn = pg2. connect(database = 'dvdrental', user = 'postgres',
                    password = 'rishabhj')

cur = conn.cursor()

cur.execute('SELECT staff_id, SUM(amount) FROM payment GROUP BY staff_id ORDER BY staff_id')

amount_by_staff_id = cur.fetchall()

cur.execute('SELECT staff_id, COUNT(staff_id) FROM payment GROUP BY staff_id ORDER BY staff_id')

transactions_by_staff_id = cur.fetchall()

x = []
y = []
x1 = [] 
y1 = []
for row in amount_by_staff_id:
    x.append(str(row[0]))
    y.append(row[1])

for row in transactions_by_staff_id:
    x1.append(str(row[0]))
    y1.append(row[1])    

position = np.arange(2)
width = 1.4
fig = plt.figure()

fig.subplots_adjust(wspace = 0.5)
ax1 = fig.add_subplot(121)
ax1.set_xticks(position + width )
ax1.set_xticklabels(x)
ax1.set_ylabel('Amount')
ax1.set_xlabel('Staff ID')

ax2 = fig.add_subplot(122)
ax2.set_xticks(position + width)
ax2.set_xticklabels(x)
ax2.set_xlabel('Staff ID')
ax2.set_ylabel('Transactions')

ax1.bar(x,y, color = 'green')
ax2.bar(x1,y1, color = 'blue')
plt.suptitle('Staff Statistics', fontsize = 20)
plt.show()
    