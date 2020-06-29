import tanima as kaynak
import cv2
import pickle
import struct
import kivy.core.camera as kcamera
import socket
import io
import time
from threading import Thread
from PIL import Image
import matplotlib.pyplot as pl
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


UDP_IP = "192.168.1.107"
UDP_PORT = 6001



anaDuzen = BoxLayout(orientation = "vertical") # Elemanların hepsini tutan ana pencere düzenimiz
ikinci_Duzen = BoxLayout(orientation = "vertical")

ilkSatir = BoxLayout()
ikinciSatir = BoxLayout()
ucuncuSatir = BoxLayout()
dorduncuSatir = BoxLayout()
besinciSatir = BoxLayout()
altinciSatir = BoxLayout()



ip_txt=TextInput()
textdeneme=TextInput()
take_port_number=TextInput()
label_for_ip=Label(text='IP Adresi:')
label_for_port=Label(text='Port Numarası:')
doldurLabel2=Label()
doldurLabel=Label()

ileri_Button=Button(text = "İleri")
geri_Button=Button(text = "Geri")
sag_button=Button(text = "Sag")
sol_button=Button(text = "Sol")
kamera_button = Button(text = "Kamera")
goruntu_isleme_button = Button(text = "GoruntuIsleme")



def threadFunc(arg):

    server_socket = socket.socket()
    server_socket.bind(('', 8001))  # ADD IP HERE
    server_socket.listen(0)

    # Accept a single connection and make a file-like object out of it
    connection = server_socket.accept()[0].makefile('rb')
    try:
        img = None
        while True:
            # Read the length of the image as a 32-bit unsigned int. If the
            # length is zero, quit the loop
            image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
            if not image_len:
                break
            # Construct a stream to hold the image data and read the image
            # data from the connection
            image_stream = io.BytesIO()
            image_stream.write(connection.read(image_len))
            # Rewind the stream, open it as an image with PIL and do some
            # processing on it
            image_stream.seek(0)
            image = Image.open(image_stream)

            if img is None:
                img = pl.imshow(image)
            else:
                img.set_data(image)

            pl.pause(0.01)
            pl.draw()

            print('Image is %dx%d' % image.size)
            image.verify()
            print('Image is verified')
    finally:
        connection.close()
        server_socket.close()


def ileriGit(instance):
    MESSAGE = "Ileri"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(str.encode(MESSAGE),(UDP_IP,UDP_PORT))
    except:
        pass

def geriGit(instance):
    #print("Hello")
    MESSAGE = "Geri"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(str.encode(MESSAGE),(UDP_IP,UDP_PORT))
    except:
        pass

def sagaGit(instance):
    MESSAGE="Sag"

    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(str.encode(MESSAGE),(UDP_IP,UDP_PORT))
    except:
        pass

def solaGit(instance):
    MESSAGE="Sola"

    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(str.encode(MESSAGE),(UDP_IP,UDP_PORT))
    except:
        pass

thread_func = Thread(target = threadFunc, args = (10, ))

def kameraTextGonder():
    MESSAGE="KameraAc"
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(str.encode(MESSAGE),(UDP_IP,UDP_PORT))
    except:
        pass

def kameraFunc(instance):
    kameraTextGonder()
    thread_func.start()

def goruntuIsle(instance):
    kaynak.main()

ileri_Button.bind(on_press = ileriGit)
geri_Button.bind(on_press = geriGit)
sag_button.bind(on_press = sagaGit)
sol_button.bind(on_press = solaGit)
kamera_button.bind(on_press = kameraFunc)
goruntu_isleme_button.bind(on_press = goruntuIsle)

# Ens on denenen kod burada
#geri_Button.bind(on_press=onur)
class Program(App):

    def build(self):

        #İLK SATIR
        ilkSatir.add_widget(label_for_ip)
        ilkSatir.add_widget(ip_txt)
        #deneme
        #İKİNCİ SATIR
        ikinciSatir.add_widget(label_for_port)
        ikinciSatir.add_widget(take_port_number)

        ucuncuSatir.add_widget(doldurLabel)
        ucuncuSatir.add_widget(ileri_Button)
        ucuncuSatir.add_widget(doldurLabel2)
        dorduncuSatir.add_widget(sol_button)
        dorduncuSatir.add_widget(geri_Button)
        dorduncuSatir.add_widget(sag_button)
        besinciSatir.add_widget(kamera_button)
        altinciSatir.add_widget(goruntu_isleme_button)
        
        
        anaDuzen.add_widget(ilkSatir)
        anaDuzen.add_widget(ikinciSatir)
        anaDuzen.add_widget(ucuncuSatir)
        anaDuzen.add_widget(dorduncuSatir)
        anaDuzen.add_widget(besinciSatir)
        anaDuzen.add_widget(altinciSatir)
        return anaDuzen


obj=Program()
obj.run()
