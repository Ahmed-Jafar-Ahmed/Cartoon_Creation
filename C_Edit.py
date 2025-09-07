import cv2 #for image processing
import easygui #to open the filebox
import numpy as np #to store image
import imageio #to read image stored at particular path
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

cartoonImage = None
# upload image function to upload image from the filebox
def upload_image():
    global cartoonImage
    ImagePath = easygui.fileopenbox()
    cartoonImage = cartoonify(ImagePath);
    #print(ImagePath)
def cartoonify(ImagePath):
    originalImage = cv2 .imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    #print(originalImage)
    if originalImage is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()
    Resized1 = cv2.resize(originalImage, (960, 540))
    #plt.imshow(Resized1)
    #plt.show()
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_RGB2GRAY)
    Resized2 = cv2.resize(grayImage, (960, 540))
    #plt.imshow(Resized2, cmap='gray')
    #plt.show()
    smoothed_image = cv2.medianBlur(grayImage, 5)
    Resized3 = cv2.resize(smoothed_image, (960, 540))
    #plt.imshow(Resized3, cmap='gray')
    #plt.show()
    edgeImage = cv2.adaptiveThreshold(smoothed_image, 255,
                                      cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 9, 9)
    Resized4 = cv2.resize(edgeImage, (960, 540))
    #plt.imshow(Resized4, cmap='gray')
    #plt.show()
    colorImage = cv2.bilateralFilter(originalImage, 9, 300, 300)
    Resized5 = cv2.resize(colorImage, (960, 540))
    #plt.imshow(Resized5)
    #plt.show()
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=edgeImage)
    Resized6 = cv2.resize(cartoonImage, (960, 540))
    #plt.imshow(Resized6)
    #plt.show()
    # Plotting the whole transition
    images = [Resized1, Resized2, Resized3, Resized4, Resized5, Resized6]
    fig, axes = plt.subplots(3, 2, figsize=(8, 8), subplot_kw={'xticks': [], 'yticks': []})
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
    plt.tight_layout()
    plt.show()
    return cartoonImage
def save():
        cartoonImagePath = easygui.filesavebox(
        msg="Save cartoon image as...",
            title="Save File",
            default="cartoonified_image.jpg",
            filetypes=["*.jpg", "*.png"]
        )
        if cartoonImagePath:
            cv2.imwrite(cartoonImagePath, cv2.cvtColor(cartoonImage, cv2.COLOR_RGB2BGR))
            easygui.msgbox("Image saved as " + cartoonImagePath)
        else:
            easygui.msgbox("Save cancelled.")
# Tkinter GUI
top = tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='black')
label = Label(top, background="#050505", font=('calibri', 20, 'bold'))
upload = Button(top, text="Cartoonify an Image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='black', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)
save1 = Button(top, text="Save cartoon image", command=save, padx=10, pady=5)
save1.configure(background='#364156', foreground='black', font=('calibri', 10, 'bold'))
save1.pack(side=TOP, pady=50)
label.pack(side=TOP, pady=20)
top.mainloop()
    

