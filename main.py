import imp
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image 
from tkinter import *


@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 


    


st.title('Main project')

menu = ["image","video"]
choice = st.sidebar.selectbox("select image or video for processing...",menu)
if st.button("Process"):
            root = Tk()
            a = Label(root, text ="Hello World")
            a.pack()
            root.mainloop()

# if choice == 'image':
#     st.title("image compression")
#     image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
#     if image_file is not None:
#         file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":(image_file.size)}
#         st.write(file_details)
#         img = load_image(image_file)
#         st.write(type(img))
#         st.image(img,width=500)
#         if st.button("Process"):
#             root = Tk()
#             a = Label(root, text ="Hello World")
#             a.pack()
#             root.mainloop()
            # select_option1 = st.radio('Select one of the compression techniques :', ['DCT','DWT','Hybrid DCT-DWT'])
            # select_option2 = st.radio('Select anyone or nothing :', ['ALCHE','CHE'])

            # if select_option1 == "DCT":
            #     st.write("hahahahha")

            pass
elif choice == 'video':
    st.title("video compression")
    
# 

# if select_option == 'image':
    
# elif select_option == 'video':
#     st.write("video selected")



