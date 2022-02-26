#imported libraries
import os
import re
import datetime
import hashlib
import itertools
import sys
import time
import bcrypt
import cv2
import math
from tkinter import *
from art import *
import numpy as np
global path_image
from passlib.hash import argon2
from passlib.hash import scrypt
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import filedialog, Tk, Button, Label


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#name banner
def name_banner():
    print(color.BOLD + color.BLUE),tprint("\nHASH "),print(color.BOLD + color.YELLOW),tprint("AND "),print(color.BOLD + color.RED),tprint("CRACK\n")
    print(color.END)
    print(color.BOLD + color.GREEN + color.UNDERLINE)
    print("BY: ABHISHEK RAJ CHAUHAN, ABHISHEK GUPTA, E.SHANMUKA SAINATH, KANUGO KRISHNA GANESH ,RANJANA TARINI R , YENIGANDLA VENISLAUS ASHISH ")
    print(color.END)
    return 0

def hash():
    print("\nENTER THE TYPE OF ALGORITHM YOU WANT TO USE")
    print("1.argon2\n2.bcrypt\n3.scrypt\n4.pbkdf2\n5.RIPEMD\n6.Hybrid Hash")
    op = int(input(":::-> "))
    password=input("Enter the Password:  ")
    s=os.urandom(32)
    salt1=str(s)
    p=password + salt1
    
    if(op==1):
        print("\nSALT ADDED = ",s)
        h=argon2.using(rounds=17).hash(p)
        print("\nFINAL HASH VALUE = ",h)
    elif (op==2):
        salt=bcrypt.gensalt()
        pas=password.encode()
        print("\nSALT ADDED = \n",salt)
        h= bcrypt.hashpw(pas,salt)
        print("\nFINAL HASH VALUE = ",h)
    elif (op==3):
        print("\nSALT ADDED = ",s)
        h=scrypt.using(rounds=16).hash(p)
        print("\nFINAL HASH VALUE = ",h)
    elif(op==4):
        print("1.sha256\n2.sha512\n")
        p=int(input())
        if(p==1):
            g=password.encode()
            print("\nSALT ADDED = ",s)
            h=hashlib.pbkdf2_hmac('sha256',g,s,10000)
            print("\nFINAL HASH VALUE = ",h)
        elif(p==2):
            g=password.encode()
            print("\nSALT ADDED = ",s)
            h=hashlib.pbkdf2_hmac('sha512',g,s,10000)
            print("\nFINAL HASH VALUE = ",h)
    elif(op==5):
        f=str(p)
        en=f.encode()
        print("\nSALT ADDED = ",s)
        x = hashlib.new('ripemd160',en).hexdigest()
        print("\nFINAL HASH VALUE = ",x)
    elif(op==6):
        salt=bcrypt.gensalt()
        hhh=password.encode()
        kkk=hashlib.sha256(hhh)
        kkk=kkk.hexdigest()
        lll=kkk.encode()
        print("\nSALT ADDED = ",salt)
        fh=bcrypt.hashpw(lll,salt)
        print("\nFINAL HASH VALUE = ",fh)
    else:
        print("\nENTER THE VALID OPTION")
 
def int_selection():
    print('Which encryption do you want to crack:\n')
    print('1.MD5\n2.blake2b\n3.blake2s\n4.SHA-1\n5.SHA-224\n6.SHA-256\n7.SHA-384\n8.SHA-512\n9.SHA3-384\n10.SHA3-512\n11.exit')
    option=input('Select your option:')
    if int(option) not in range(1,12):
        print('\nInvalid option\n')
        exit()
    hash=input('Enter the Hash: ')
    wrd_list=input('Enter the location of the wordlist: ')
    while not os.path.exists(wrd_list):
            print('Error: The file/(file path) does not exist:')
            wrd_list=input('Enter the location of the wordlist: ')
    if option=='1':
        md5(hash,wrd_list)
    elif option=='2':
        blk2b(hash,wrd_list)
    elif option=='3':
        blk2s(hash,wrd_list)
    elif option=='4':
        sha1(hash,wrd_list)
    elif option=='5':
        sha224(hash,wrd_list)
    elif option=='6':
        sha256(hash,wrd_list)
    elif option=='7':
        sha384(hash,wrd_list)
    elif option=='8':
        sha512(hash,wrd_list)
    elif option=='9':
        sha3384(hash,wrd_list)
    elif option=='10':
        sha3512(hash,wrd_list)
    elif option=='11':
        sys.exit(0)
    else:
        print('\nCouldn\'t crack the password :(')


#md5
def md5(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i = i.replace('\n','')
        wrd_hash=hashlib.md5(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            time.sleep(1)
            pass_lst.close()
            exit(0)


#sha256
def sha256(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i = i.replace('\n','')
        wrd_hash=hashlib.sha256(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)            
#sha512
def sha512(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i = i.replace('\n','')
        wrd_hash=hashlib.sha512(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)                                                                            
#sha1
def sha1(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i = i.replace('\n','')
        wrd_hash=hashlib.sha1(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)
#sha224
def sha224(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i = i.replace('\n','')
        wrd_hash=hashlib.sha224(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)
#sha384
def sha384(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i = i.replace('\n','')
        wrd_hash=hashlib.sha384(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)            
#BLAKE2b
def blk2b(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i = i.replace('\n','')
        wrd_hash=hashlib.blake2b(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)
#BLAKE2s
def blk2s(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i = i.replace('\n','')
        wrd_hash=hashlib.blake2s(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)
#SHA3-384
def sha3384(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i = i.replace('\n','')
        wrd_hash=hashlib.sha3_384(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)
#SHA3-512
def sha3512(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i = i.replace('\n','')
        wrd_hash=hashlib.sha3_512(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)            
#SHA3-256
def sha3256(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i = i.replace('\n','')
        wrd_hash=hashlib.sha3_256(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)

def image_encry():
    image_display_size = 300, 300
    def on_click():
        global path_image
        path_image = filedialog.askopenfilename()
        load_image = Image.open(path_image)
        load_image.thumbnail(image_display_size, Image.ANTIALIAS)
        np_load_image = np.asarray(load_image)
        np_load_image = Image.fromarray(np.uint8(np_load_image))
        render = ImageTk.PhotoImage(np_load_image)
        img = Label(app, image=render)
        img.image = render
        img.place(x=20, y=50)
    def encrypt_data_into_image():
        data = txt.get(1.0, "end-1c")
        img = cv2.imread(path_image)
        data = [format(ord(i), '08b') for i in data]
        _, width, _ = img.shape
        PixReq = len(data) * 3
        RowReq = PixReq/width
        RowReq = math.ceil(RowReq)
        count = 0
        charCount = 0
        for i in range(RowReq + 1):  
            while(count < width and charCount < len(data)):
               char = data[charCount]
               charCount += 1
               for index_k, k in enumerate(char):
                    if((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                        img[i][count][index_k % 3] -= 1
                    if(index_k % 3 == 2):
                        count += 1
                    if(index_k == 7):
                        if(charCount*3 < PixReq and img[i][count][2] % 2 == 1):
                            img[i][count][2] -= 1
                        if(charCount*3 >= PixReq and img[i][count][2] % 2 == 0):
                            img[i][count][2] -= 1
                        count += 1
            count = 0
        cv2.imwrite("encrypted_image.png", img)
        success_label = Label(app, text="Encryption Successful!",bg='lavender', font=("Times New Roman", 20))
        success_label.place(x=160, y=300)
    app = Tk()
    app.configure(background='lavender')
    app.title("Encrypt")
    app.geometry('600x600')
    on_click_button = Button(app, text="Choose Image", bg='white', fg='black', command=on_click)
    on_click_button.place(x=250, y=10)
    txt = Text(app, wrap=WORD, width=30)
    txt.place(x=340, y=55, height=165)
    encrypt_button = Button(app, text="Encode", bg='white', fg='black', command=encrypt_data_into_image)
    encrypt_button.place(x=435, y=230)
    app.mainloop()



def decrypt():
    image_display_siz = 300, 300
    def on_click():
        global path_image
        path_image = filedialog.askopenfilename()
        load_image = Image.open(path_image)
        load_image.thumbnail(image_display_siz, Image.ANTIALIAS)
        np_load_image = np.asarray(load_image)
        np_load_image = Image.fromarray(np.uint8(np_load_image))
        render = ImageTk.PhotoImage(np_load_image)
        img = Label(app, image=render)
        img.image = render
        img.place(x=20, y=50)
        
    def decrypt_data_into_image():
        img = cv2.imread(path_image)
        data = []
        stop = False
        for index_i, i in enumerate(img):
            i.tolist()
            for index_j, j in enumerate(i):
                if((index_j) % 3 == 2):
                    data.append(bin(j[0])[-1])
                    data.append(bin(j[1])[-1])
                    if(bin(j[2])[-1] == '1'):
                        stop = True
                        break
                else:
                    data.append(bin(j[0])[-1])
                    data.append(bin(j[1])[-1])
                    data.append(bin(j[2])[-1])
            if(stop):
                break
        message = []
        for i in range(int((len(data)+1)/8)):
            message.append(data[i*8:(i*8+8)])
        message = [chr(int(''.join(i), 2)) for i in message]
        message = ''.join(message)
        message_label = Label(app, text=message, bg='lavender', font=("Times New Roman", 20))
        message_label.place(x=160, y=300)
    app = Tk()
    app.configure(background='lavender')
    app.title("Decrypt")
    app.geometry('600x600')
    on_click_button = Button(app, text="Choose Image", bg='white', fg='black', command=on_click)
    on_click_button.place(x=250, y=10)
    txt = Text(app, wrap=WORD, width=30)
    txt.place(x=340, y=55, height=165)
    decrypt_button = Button(app, text="Decode", bg='white', fg='black', command=decrypt_data_into_image)
    decrypt_button.place(x=435, y=230)
    app.mainloop()


def stegno_sel():
    qw = int(input("\nSelect your choice:\n1.Encode Image\n2.Decode image: "))
    if(qw==1):
        image_encry()
    elif(qw==2):
        decrypt()   
def sel(x):
    if(x==1):
        int_selection()
    if(x==2):
        hash()
    if(x==3):
        stegno_sel()
    return 0 
   
def main():
    name_banner()
    while 1:
        x = int(input("\nSelect Mode:-\n1.HASH CRACKING \n2.HASHING WITH NEW ALGORITHMS \n3.ENCODING THE HASH VALUE INTO AN IMAGE \n4.EXIT : "))
        if(x==4):
            break
        else:
          sel(x)
main()