import random
import speech_recognition as sr
import numpy as np
import pyttsx3
import tkinter as tk
from PIL import ImageGrab
from tkinter import ROUND, TRUE
from flask import Flask, send_file
from threading import Thread


app = Flask(__name__)

def run_flask():
    app.run(host='0.0.0.0', port=8002)

@app.route('/GUI')
def get_gui_script():
    return send_file('handwritten.py')



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
# text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def predict(Theta1, Theta2, X):
	m = X.shape[0]
	one_matrix = np.ones((m, 1))
	X = np.append(one_matrix, X, axis=1) # Adding bias unit to first layer
	z2 = np.dot(X, Theta1.transpose())
	a2 = 1 / (1 + np.exp(-z2)) # Activation for second layer
	one_matrix = np.ones((m, 1))
	a2 = np.append(one_matrix, a2, axis=1) # Adding bias unit to hidden layer
	z3 = np.dot(a2, Theta2.transpose())
	a3 = 1 / (1 + np.exp(-z3)) # Activation for third layer
	p = (np.argmax(a3, axis=1)) # Predicting the class on the basis of max value of hypothesis
	return p
# Define the functions globally
def check():
    global l1
    widget = cv
    # Setting co-ordinates of canvas
    x = window.winfo_rootx() + widget.winfo_x()
    y = window.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()

    # Image is captured from canvas and is resized to (28 X 28) px
    img = ImageGrab.grab().crop((x, y, x1, y1)).resize((28, 28))

    # Converting rgb to grayscale image
    img = img.convert('L')
    # Extracting pixel matrix of image and converting it to a vector of (1, 784)
    x = np.asarray(img)
    vec = np.zeros((1, 784))
    k = 0
    for i in range(28):
        for j in range(28):
            vec[0][k] = x[i][j]
            k += 1
    
    # Loading Thetas
    Theta1 = np.loadtxt('training/Theta1.txt')
    Theta2 = np.loadtxt('training/Theta2.txt')	
    # Calling function for prediction
    pred = predict(Theta1, Theta2, vec / 255)
    

    # Displaying the result
    if(rand==pred[0]):	
        l1 = tk.Label(window, text="✔️",fg="green", font=('Comic Sans MS', 34),bg="#fbf29b")
        l1.place(x=260, y=437)
        speak("That's good its a  "+str(rand))
    else:
        l1 = tk.Label(window, text="❌",fg="red", font=('Comic Sans MS', 34),bg="#fbf29b")
        l1.place(x=260, y=437)
        speak("Try again")
# To draw on canvas
def draw_lines(event):
	global lastx, lasty
	x, y = event.x, event.y
	cv.create_line((lastx, lasty, x, y), width=30, fill='white', capstyle=ROUND, smooth=TRUE, splinesteps=12)
	lastx, lasty = x, y
# Activate canvas
def event_activation(event):
	global lastx, lasty
	cv.bind('<B1-Motion>', draw_lines)
	lastx, lasty = event.x, event.y
def tryagain():
    global cv, l1, rand
    cv.delete("all")
    l1.destroy()
    rand=random.randint(0,9)
    text = "Try " + str(rand)
    # Label
    L1 = tk.Label(window, text=text, font=('Comic Sans MS', 25), fg="#252a2a",bg="#fbf29b")
    L1.place(x=250, y=10)

def clear():
    global cv
    cv.delete("all")


global l1, cv, rand, window
window = tk.Tk()
window.title("let's learn numbers")
window.geometry("600x500")
window.configure(bg="#fbf29b")  # Set background color

l1 = tk.Label()

rand=random.randint(0,9)
text = "Try " + str(rand)
# Label
L1 = tk.Label(window, text=text, font=('Comic Sans MS', 25), fg="#252a2a",bg="#fbf29b")
L1.place(x=250, y=10)

# Button to clear canvas
b1 = tk.Button(window, text="Try again", font=('Comic Sans MS', 20), bg="#aed8e6", fg="#252a2a", command=tryagain)
b1.place(x=95, y=370)

# Button to predict digit drawn on canvas
b2 = tk.Button(window, text="Check", font=('Comic Sans MS', 20), bg="white", fg="#252a2a", command=check)
b2.place(x=275, y=370)
# Button to predict digit drawn on canvas
b3 = tk.Button(window, text="clear", font=('Comic Sans MS', 20), bg="#252a2a", fg="#fbf29b", command=clear)
b3.place(x=415, y=370)
# Setting properties of canvas
cv = tk.Canvas(window, width=350, height=290, bg='black')
cv.place(x=120, y=70)

cv.bind('<Button-1>', event_activation)

window.mainloop()


if __name__ == "__main__":
    t = Thread(target=run_flask)
    t.start()

    