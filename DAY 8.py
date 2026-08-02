import matplotlib.pyplot as plt

departments = ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
employee_counts = [15, 45, 30, 22, 50]

plt.figure(figsize=(8, 5))
plt.bar(departments, employee_counts, color='skyblue', edgecolor='black')
plt.xlabel('Department Name')
plt.ylabel('Number of Employees')
plt.title('Employee Count by Department')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

import matplotlib.pyplot as plt

departments = ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
employee_counts = [15, 45, 30, 22, 50]

plt.figure(figsize=(8, 5))
plt.bar(departments, employee_counts, color='skyblue', edgecolor='black')
plt.xlabel('Department Name')
plt.ylabel('Number of Employees')
plt.title('Employee Count by Department')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

import matplotlib.pyplot as plt

# Sample Data: Market Share
companies = ['Company A', 'Company B', 'Company C', 'Company D']
market_share = [40, 25, 20, 15]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0, 0)

plt.figure(figsize=(7, 7))
plt.pie(market_share, explode=explode, labels=companies, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  
plt.title('Company Market Share Distribution')
plt.show()