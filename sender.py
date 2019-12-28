import socket
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


UDP_IP = ""
UDP_PORT = 6666
MESSAGE = ""



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


def onpresone(instance):
    #MESSAGE=textdeneme.text
    UDP_IP=ip_txt.text
    UDP_PORT=int(take_port_number.text)
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #sock.sendto(bytearray(MESSAGE,'utf-8'), (UDP_IP, UDP_PORT))
        sock.sendto(str.encode(MESSAGE), (UDP_IP, UDP_PORT))
    except: 
        pass
    #textdeneme.text=''
    #ikinci_Duzen.Toplevel()
    if textdeneme.text=="admin":
        anaDuzen.remove_widget(ilkSatir)
        anaDuzen.remove_widget(ikinciSatir)
        anaDuzen.remove_widget(dorduncuSatir)
    


def ileriGit(instance):
    MESSAGE="ileri"
    UDP_IP=ip_txt.text
    UDP_PORT=int(take_port_number.text)
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #sock.sendto(bytearray(MESSAGE,'utf-8'), (UDP_IP, UDP_PORT))
        sock.sendto(str.encode(MESSAGE), (UDP_IP, UDP_PORT))
    except: 
        pass

def geriGit(instance):
    #print("Hello")
    MESSAGE="geri"
    UDP_IP=ip_txt.text
    UDP_PORT=int(take_port_number.text)
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(str.encode(MESSAGE),(UDP_IP,UDP_PORT))
    except:
        pass

def sagaGit(instance):
    #print("Hello")
    MESSAGE="sag"
    UDP_IP=ip_txt.text
    UDP_PORT=int(take_port_number.text)
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(str.encode(MESSAGE),(UDP_IP,UDP_PORT))
    except:
        pass

def solaGit(instance):
    #print("Hello")
    MESSAGE="sol"
    UDP_IP=ip_txt.text
    UDP_PORT=int(take_port_number.text)
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(str.encode(MESSAGE),(UDP_IP,UDP_PORT))
    except:
        pass




ileri_Button.bind(on_press = ileriGit)
geri_Button.bind(on_press = geriGit)
sag_button.bind(on_press = sagaGit)
sol_button.bind(on_press = solaGit)

#geri_Button.bind(on_press=onur)
class Program(App):
    def __del__(self): 
        pass
    def build(self):

        #İLK SATIR
        ilkSatir.add_widget(label_for_ip)
        ilkSatir.add_widget(ip_txt)

        #İKİNCİ SATIR
        ikinciSatir.add_widget(label_for_port)
        ikinciSatir.add_widget(take_port_number)

        dorduncuSatir.add_widget(doldurLabel)
        dorduncuSatir.add_widget(ileri_Button)
        dorduncuSatir.add_widget(doldurLabel2)
        besinciSatir.add_widget(sol_button)
        besinciSatir.add_widget(geri_Button)
        besinciSatir.add_widget(sag_button)
        
        anaDuzen.add_widget(ilkSatir)
        anaDuzen.add_widget(ikinciSatir)
        anaDuzen.add_widget(dorduncuSatir)
        anaDuzen.add_widget(besinciSatir)

        return anaDuzen


obj=Program()
obj.run()