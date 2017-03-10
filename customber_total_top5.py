import psycopg2 as pg2
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

conn = pg2. connect(database = 'dvdrental', user = 'postgres',
                    password = 'rishabhj')

cur = conn.cursor()

cur.execute('SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id ORDER BY customer_id')
payments = cur.fetchall()
amts = []
cus_ids = []
for payment in payments:
    cus_id = payment[0]
    amt = payment[1]
    amts.append(amt)
    cus_ids.append(cus_id)    

cur.execute('SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id ORDER BY SUM(amount) DESC LIMIT(5)')
top_5_customers = cur.fetchall()
amts1 = []
cus_ids1 = []
for cus in top_5_customers:
    cus_ids1.append(str(cus[0]))
    amts1.append(cus[1])    
    
plt.figure(1)
plt.bar(cus_ids,amts, color = 'orange', alpha = 0.7) 
plt.ylabel('Amount Spent')
plt.xlabel('Customer ID')
plt.title('Total Amount spent for all Customers', fontsize = 18)
plt.xlim(0,600)
plt.ylim(0,250)
plt.grid(False)
ax = plt.gca()
ax.set_axis_bgcolor('black')

position = np.arange(5)
w = 0.4

plt.figure(2)
ax = plt.gca() 
plt.bar(position, amts1, color = 'red', alpha = 0.7)
ax.set_xticks(position + w)
ax.set_xticklabels(cus_ids1)
ax.set_axis_bgcolor('white')
plt.title('Top 5 Customers', fontsize = 20)
plt.xlabel('Customer ID')
plt.ylabel('Amount Spent')
plt.ylim(0,250)

plt.show()


  