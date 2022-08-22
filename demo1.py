#install pillow to work with images
from tkinter import *
import psutil
import speedtest
import math
from PIL import Image,ImageTk

def usage():
    cpu_count = psutil.cpu_count()
    cpu_count_label.config(text=cpu_count,image=tk_image,compound='center')

    cpu_usage = psutil.cpu_percent(1)
    cpu_usage_label.config(text=cpu_usage,image=tk_image,compound='center')
    cpu_usage_label.after(100, usage)

    ram_count = math.floor(psutil.virtual_memory()[0]/1000000000)
    ram_count_text = str(ram_count) + "GB"
    ram_count_label.config(text=ram_count_text,image=tk_image,compound='center')

    #ram usage
    ram_usage = psutil.virtual_memory()[2]
    ram_usage_text = str(ram_usage) + "%"
    ram_usage_label.config(text=ram_usage_text,image=tk_image,compound='center')

    #available ram
    avail_ram = math.floor(psutil.virtual_memory()[1]/1000000000)
    avail_ram_text = str(avail_ram) + "GB"
    ram_avail_label.config(text=avail_ram_text,image=tk_image,compound='center')

def internet_speed():
    st = speedtest.Speedtest()
    download_speed = str(math.floor(st.download() / 1000000)) + "Mb/s"
    upload_Speed = str(math.floor(st.upload() / 1000000)) + "Mb/s"
    ping = st.results.ping
    ping = str(st.results.ping) + "MS"
    upload_label.config(text=upload_Speed)
    download_label.config(text=download_speed)
    ping_label.config(text=ping)


root = Tk()
root.config(bg='white')

image = Image.open('speedometer.png')
resized_im = image.resize((round(image.size[0]*0.35), round(image.size[1]*0.35)))
tk_image = ImageTk.PhotoImage(resized_im)

root.geometry("1920x1080")
root.title("CPU STATUS")

#code for cpu count
cpu_count_label = Label(root,font=("Orbitron",40,'bold'), text="0",bd=-2)
cpu_count_label.grid(row=0, column=0)
l1 = Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03', text="CPU's")
l1.grid(row=1, column=0)

#cpu usage
cpu_usage_label = Label(root, font=("Orbitron",40,'bold'), text="0",bd=-2)
cpu_usage_label.grid(row=0,column=1)
l2 = Label(root, font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="CPU Usage In %")
l2.grid(row=1, column=1)

#total ram
ram_count_label = Label(root,font=("Orbitron",40,'bold'), text="0",bd=-2)
ram_count_label.grid(row=0, column=2)
l3 = Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03', text="Total Ram")
l3.grid(row=1, column=2)

#ram % usage
ram_usage_label = Label(root, font=("Orbitron",30,'bold'),text="0",bd=-2)
ram_usage_label.grid(row=0, column=3)
l4 = Label(root, font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Ram used")
l4.grid(row=1, column=3)

#available ram
ram_avail_label = Label(root, font=("Orbitron",40,'bold'),text="0",bd=-2)
ram_avail_label.grid(row=0, column=4)
l5 = Label(root, font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Available Ram")
l5.grid(row=1, column=4)


# add speed button
speed_button = Button(root, text="Test Internet Speed",command=internet_speed,width=15,height=3,font=("Orbitron",20,'bold'))
speed_button.grid(row=3, column=0)

download_label = Label(root,font=("Orbitron",20,'bold'),text="0 Mb/s",image=tk_image,compound='center',bd=-2)
download_label.grid(row=3,column=1)
l6 = Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Download Speed")
l6.grid(row=4,column=1)

upload_label = Label(root,font=("Orbitron",20,'bold'),text="0 Mb/s",image=tk_image,compound='center',bd=-2)
upload_label.grid(row=3,column=2)
l7 = Label(root, font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Upload Speed")
l7.grid(row=4, column=2)

ping_label = Label(root, font=("Orbitron",20,'bold'),text="0 Mb/s",image=tk_image,compound='center',bd=-2)
ping_label.grid(row=3,column=3)
l8 = Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Ping")
l8.grid(row=4,column=3)
usage()
root.mainloop()


