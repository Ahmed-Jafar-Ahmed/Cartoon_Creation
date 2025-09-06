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

# upload image function to upload image from the filebox
def upload_image():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath);
    #print(ImagePath)
def cartoonify(ImagePath):
    originalImage = cv2 .imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.RGB2BGR)
    #print(originalImage)
    if originalImage is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()
    Resized1 = cv2.resize(originalImage, (960, 540))
    #plt.imshow(Resized1)
    #plt.show()
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
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
    