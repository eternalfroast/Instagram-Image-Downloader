from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as bs
import re
import os


filename = ""
# url = ""

root = Tk()
root.geometry("600x300")
root.configure(background='#f6f6f6')

frame = Frame(root, background="#0168ff", width=20,
              height=200, padx=20, pady=20)


label = Label(root, text="Image Downloader", pady=20,
              background="#f6f6f6", fg="#0168ff", font=("Open Sans", 16, 'bold'))
entry = Entry(root, width=50)

def imageScrape(url):

    with urllib.request.urlopen(url) as response:
        html = response.read()

    soup = bs(html, "lxml")  

    filename = url[-12:-1] + '.jpg'

    links = []

    for link in soup.findAll('meta', attrs={'content': re.compile("^https://")}):
            links.append(link.get('content'))

    img = links[0]
    
    urlretrieve(img, filename)
    

def getText():
    url = entry.get()
    print(url)
    print(url[-12:-1])
    imageScrape(url)
    messagePop()
    entry.delete(0, 'end')


def messagePop():
   messagebox.showinfo("Download report", "The picture has been downloaded sucessfully")

button = ttk.Button(root, text="Download the image", width=25)
button.config(command=getText)
Label(frame, text="This is a instagram image downloader. Please select the link of the image that you want to download and copy it. Paste the copied URL to the URL box and the press the download box to download the image.",
      fg="white", background="#0168ff", wraplength=500, justify=CENTER).pack()
label.pack()
entry.pack(fill=NONE)


frameSpace = Frame(root, height=20)
frameSpace1 = Frame(root, height=30)
frameSpace1.pack()
button.pack()

frameSpace.pack()

frame.pack(fill=BOTH)
root.title('Instagram Image Downloader')
root.mainloop()


