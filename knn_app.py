import tkinter as tk
#from tkinter import filedialog
import numpy as np
from math import sqrt

datas = []
dataset = []
credit = []
# test_data = [0, 45, 100000]
test_data = []

window = tk.Tk()
window.title("KnnApp")
window.geometry('500x200')

#get data from file
# def UploadAction(event=None):
#     filename = filedialog.askopenfilename()
#     print('Selected:', filename)

f = open('dataset.csv', 'r')
while True:
    data = f.readline()
    if data == '':
        break
    else:
        pre_data = data.strip('\n').split(',')
        credit.append(int(str(pre_data[3])))
        datas.append(pre_data)
f.close()

for i in range(len(datas)):
    d_list = []
    for j in range(len(datas[i])):
        if j == 3:
            continue
        else:
            d_list.append(int(datas[i][j]))

        if len(d_list) == 3:
            dataset.append(d_list)

#knn calculate
def manhattan_distance(row1, row2):
	distance = 0
	for i in range(len(row1)-1):
		distance += np.absolute(row1[i] - row2[i])
	return distance

def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

def knn(train, test, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test, train_row)
        distances.append((train_row, dist))

    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])

    map_credit = []
    for j in range(len(neighbors)):
        for k in range(len(dataset)):
            if neighbors[j] == dataset[k]:
                map_credit.append(credit[k])

    one = 0
    zero = 0
    for f in map_credit:
        if f == 0:
            zero += 1
        elif f == 1:
            one += 1

    result = ""
    if one > zero:
        result = "Good Credit"
    elif zero > one:
        result = "Not good Credit"

    return result

#GUI
K = tk.StringVar()
G = tk.StringVar()
A = tk.StringVar()
S = tk.StringVar()

def calculate():
    k = int(K.get())
    g = G.get()
    a = int(A.get())
    s = int(S.get())

    if g == 'F' or g == 'f':
        test_data.append(0)
    elif g == 'M' or g == 'm':
        test_data.append(1)
    
    test_data.append(a)
    test_data.append(s)

    result = knn(dataset, test_data, k)
    R_label = tk.Label(window, text=result)
    R_label.place(x=180, y=80)

    test_data.clear()

K_label = tk.Label(window, text="K:")
K_label.place(x=20, y=20)

k = tk.Entry(window, width=7, textvariable=K)
k.place(x=45, y=20)

G_label = tk.Label(window, text="Gender:")
G_label.place(x=100, y=20)

gender = tk.Entry(window, width=7, textvariable=G)
gender.place(x=150, y=20)

A_label = tk.Label(window, text="Age:")
A_label.place(x=205, y=20)

age = tk.Entry(window, width=7, textvariable=A)
age.place(x=240, y=20)

S_label = tk.Label(window, text="Salary:")
S_label.place(x=290, y=20)

salary = tk.Entry(window, width=7, textvariable=S)
salary.place(x=340, y=20)

button = tk.Button(text="Calculate", command= lambda: calculate())
button.place(x=180, y=50)

window.mainloop()