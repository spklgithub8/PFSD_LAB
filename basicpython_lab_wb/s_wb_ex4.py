

#Ex-4-1

import random
import string

def generate_random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

def generate_random_alphabetical_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for _ in range(length))

def generate_random_between(start, end):
    random_num = random.randint(start, end)
    return random_num

def generate_random_multiple_of_seven():
    multiple_of_seven = random.randint(0, 10) * 7
    return multiple_of_seven

random_color = generate_random_color()
random_string = generate_random_alphabetical_string(8)
random_between = generate_random_between(50, 100)
random_multiple_of_seven = generate_random_multiple_of_seven()


print("Random Color Hex:", random_color)
print("Random Alphabetical String:", random_string)
print("Random Value between 50 and 100:", random_between)
print("Random Multiple of 7 between 0 and 70:", random_multiple_of_seven)


#Ex-4-2

import random
from datetime import datetime, timedelta

def generate_random_excluding_six():
    random_num = random.randint(0, 5)
    return random_num

def generate_random_between_five_and_ten():
    random_num = random.randint(5, 9)
    return random_num

def generate_random_step_of_three():
    random_num = random.randrange(0, 10, 3)
    return random_num

def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

random_num_excluding_six = generate_random_excluding_six()
random_num_between_five_and_ten = generate_random_between_five_and_ten()
random_num_step_of_three = generate_random_step_of_three()

start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)
random_date = generate_random_date(start_date, end_date)

print("Random integer between 0 and 6 (excluding 6):", random_num_excluding_six)
print("Random integer between 5 and 10 (excluding 10):", random_num_between_five_and_ten)
print("Random integer between 0 and 10 with a step of 3:", random_num_step_of_three)
print("Random date between 2022-01-01 and 2023-12-31:", random_date.strftime("%Y-%m-%d"))


# Ex-4-3, in lab sir example.
import pandas as pd
my_dict={
    "Name":["Ravi","Ram","Raja"],
    "Marks":[50,55,53]
}
df=pd.DataFrame(data=my_dict)
df.plot.line(title="Marks")
pic=df.plot.line()
pic=pic.get_figure()
pic.savefig('a.jpg')

#ex 4-3, in lab sir example 2

import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
mylabels=["DBMS","Python","OS","MP"]
plt.pie(y,labels=mylabels,startangle=90)
plt.show()

#Ex 4-4, in lab sir example.
import numpy as np
# Creating a NumPy array
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Basic operations on arrays
sum_arr1 = np.sum(arr1)
mean_arr2 = np.mean(arr2)

print("Sum of 1D Array:", sum_arr1)
print("Mean of 2D Array:", mean_arr2)

# Element-wise operations
squared_arr1 = np.square(arr1)
sqrt_arr2 = np.sqrt(arr2)

print("Squared elements of arr1:", squared_arr1)
print("Square root of arr2:", sqrt_arr2)


#Ex 4-5, in lab sir example.
import matplotlib.pyplot as plt
import numpy as np
regnum = ['101', '102', '103']
categories = ["DBMS", "Python", "OS", "MP"]
values = np.array([
    [35, 25, 25, 15],  # Values for category "DBMS"
    [20, 30, 15, 35],  # Values for category "Python"
    [10, 40, 20, 30],  # Values for category "OS"
])
colors = ['blue', 'green', 'orange', 'red']
# Plot area for each registration number and category
for i, reg in enumerate(regnum):
    plt.fill_between(categories, 0, values[i], label=f'Registration {reg}', color=colors[i], alpha=0.7)
# Add labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Area Plot with Different Colors")
plt.legend()
plt.show()


#3 generate graph using pandas & matplotlib
import pandas as pd
import matplotlib.pyplot as plt
def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df
def generate_graph(data_frame):
    x_values = data_frame['REGNUM']
    y_columns = data_frame.columns[1:]
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i,column in enumerate(y_columns):
        y_values = data_frame[column]
        plt.plot(x_values, y_values, marker='o', linestyle='-', label=column, color = colors[i])
    # plt.plot(x_values, y_values, marker='o', linestyle='-', color=colors)
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('CSV Data Plot')
    plt.grid(True)
    plt.legend()
    plt.savefig("a1.png")
    plt.show()

if __name__ == "__main__":
    file_path = "csf.csv"
    data_frame = read_csv_file(file_path)
    generate_graph(data_frame)
