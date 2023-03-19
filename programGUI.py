from tkinter import *
import KNN

root = Tk()
root.title('KNN Amontep , Arun & Sontaya')
root.resizable(width=False, height=False)
frame = Frame(root)
frame.pack()

canvas = Canvas(frame, 
                bg="white", 
                width=300, 
                height=380)

canvas.pack()
def getKNN():
    K = k.get()
    TEMPERATURE = temperature.get()
    MOISTURE = moisture.get()
    WIND_SPEED = wind_speed.get()
    AIR_QUALITY = air_quality.get()
    result  =KNN.knn (K,TEMPERATURE, MOISTURE,  WIND_SPEED, AIR_QUALITY)

    txt.set(result)
    return result

txt = StringVar()
txt_label = Label(root,text="result =").place(x=15,y=320)
txt_disp =Entry(root,textvariable=txt,state=DISABLED).place(x=150, y=320)


name = Label(root,text="WEATHER").place(x=115,y=30)

k = IntVar()
k_label = Label(root,text="K = ").place(x=15,y=70)
k_input = Entry(root, textvariable=k).place(x=150, y=70)
k.set('')

temperature = IntVar()
temperature_label = Label(root,text="TEMPERATURE = ").place(x=15,y=120)
temperature_input = Entry(root, textvariable=temperature).place(x=150, y=120)
temperature.set('')

moisture = IntVar()
moisture_label = Label(root,text="MOISTURE= ").place(x=15,y=170)
moisture_input = Entry(root, textvariable=moisture).place(x=150, y=170)
moisture.set('')

wind_speed = IntVar()
wind_speed_label = Label(root,text="WIND_SPEED= ").place(x=15,y=220)
wind_speed_input = Entry(root, textvariable=wind_speed).place(x=150, y=220)
wind_speed.set('')

air_quality = IntVar()
air_quality_label = Label(root,text=" AIR_QUALITY = ").place(x=15,y=270)
air_quality_input = Entry(root, textvariable=air_quality).place(x=150, y=270)
air_quality.set('')

btn = Button(root, text = 'CHECK', bd = '10', command = getKNN)
btn.pack(side = 'bottom') 

root.mainloop()

