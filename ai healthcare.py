import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Define a list of diseases and conditions
diseases = ['Healthy', 'Hypertension', 'Diabetes', 'Obesity', 'Hyperthyroidism', 'Hypothyroidism']

# Define a function to get the diagnosis
def get_diagnosis():
    # Get input data from user
    try:
        age = float(age_entry.get())
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        systolic_bp = float(systolic_bp_entry.get())
        diastolic_bp = float(diastolic_bp_entry.get())
        cholesterol = float(cholesterol_entry.get())
        glucose = float(glucose_entry.get())

        # Use the model to make a prediction on the user's data
        X_new = np.array([age, height, weight, systolic_bp, diastolic_bp, cholesterol, glucose]).reshape(1, -1)
        y_pred = model.predict(X_new)

        # Print the predicted diagnosis or disease
        if y_pred == 0:
            diagnosis_label.config(text="You are healthy.")
        else:
            diagnosis_label.config(text="You may have " + diseases[int(y_pred)] + " and should seek medical attention.")
    except ValueError:
        messagebox.showwarning("Invalid input", "Please enter valid numeric values.")

# Define a function to clear all the input fields and diagnosis label
def clear_fields():
    age_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    systolic_bp_entry.delete(0, tk.END)
    diastolic_bp_entry.delete(0, tk.END)
    cholesterol_entry.delete(0, tk.END)
    glucose_entry.delete(0, tk.END)
    diagnosis_label.config(text="")

# Prepare the data
data = np.array([[40, 1.6, 70, 110, 70, 80, 1.0, 0], 
                 [50, 1.8, 90, 120, 80, 85, 1.2, 1],
                 [35, 1.7, 65, 100, 60, 75, 0.8, 0],
                 [55, 1.65, 75, 130, 90, 90, 1.3, 2],
                 [45, 1.75, 80, 120, 80, 85, 1.2, 1],
                 [30, 1.5, 50, 90, 60, 70, 0.9, 2]])

df = pd.DataFrame(data, columns=['age', 'height', 'weight', 'systolic_bp', 'diastolic_bp', 'cholesterol', 'glucose', 'diagnosis'])

# Prepare the data for training
X = df.drop('diagnosis', axis=1)
y = df['diagnosis']


#Train a Random Forest Classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

#Create the GUI window
root = tk.Tk()
root.geometry("400x400")
root.title("Health Diagnosis System")

#Create the input labels and fields
age_label = ttk.Label(root, text="Age:")
age_label.pack()
age_entry = ttk.Entry(root)
age_entry.pack()

height_label = ttk.Label(root, text="Height (m):")
height_label.pack()
height_entry = ttk.Entry(root)
height_entry.pack()

weight_label = ttk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = ttk.Entry(root)
weight_entry.pack()

systolic_bp_label = ttk.Label(root, text="Systolic blood pressure (mmHg):")
systolic_bp_label.pack()
systolic_bp_entry = ttk.Entry(root)
systolic_bp_entry.pack()

diastolic_bp_label = ttk.Label(root, text="Diastolic blood pressure (mmHg):")
diastolic_bp_label.pack()
diastolic_bp_entry = ttk.Entry(root)
diastolic_bp_entry.pack()

cholesterol_label = ttk.Label(root, text="Cholesterol level (mg/dL):")
cholesterol_label.pack()
cholesterol_entry = ttk.Entry(root)
cholesterol_entry.pack()

glucose_label = ttk.Label(root, text="Glucose level (mg/dL):")
glucose_label.pack()
glucose_entry = ttk.Entry(root)
glucose_entry.pack()

#Create the buttons
diagnose_button = ttk.Button(root, text="Diagnose", command=get_diagnosis)
diagnose_button.pack()

clear_button = ttk.Button(root, text="Clear", command=clear_fields)
clear_button.pack()

#Create the diagnosis label
diagnosis_label = ttk.Label(root, text="")
diagnosis_label.pack()
#Start the GUI
root.mainloop()