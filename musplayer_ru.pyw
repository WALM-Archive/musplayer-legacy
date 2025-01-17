from tkinter import *
import pygame
from tkinter import filedialog, messagebox, Entry, ttk
import pystray
import PIL.Image
import sys
import os
import time
import wget
import os.path
import webbrowser
from pytube import YouTube
from moviepy import *

oname_mus = ''

pygame.mixer.init()

upbut = float(1.05)
playlist_move_remove_panel = int(0)
volume = 100
pygame.mixer.music.set_volume(volume)
#image_icon_png = PIL.Image.open('icons/logo.png')
mus_loop = NO
des = Tk()
des.geometry('480x300+420+170')

des.resizable(width=0, height=0)
des.title('musplayer')
#des.iconbitmap('icons/logo.ico')
name_mus = 'нет музыки'

theme = 'sun'

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)
right_speed = float(0.0) 

def equo():
    global theme
    global freq
    global buffer
    global bits
    global int_freq

    freq  = int(44100)
    buffer = int(512)
    bits = (8, 16, 32)

    def pg_apply():
        global int_buffer
        global int_freq
        global right_speed
        global btn_mus_play_pause
        global mus_loop
        global var_btn_mus_play_pause
        pygame.mixer.music.stop()
        pygame.mixer.pre_init(int(int_freq), int(bits_combo.get()), 2, int(int_buffer))

        btn_mus_play_pause.configure(image = mus_play)
        mus_loop = True
        var_btn_mus_play_pause = 0
        right_speed = float(0.0)
        dl_mus.config(text = "время музыки")

    def bits_sel(event):
        select_bits = bits_combo.get()
        lbl_bits['text'] = f'разрядность {select_bits}'

    def sc_buf(buffer):
        global int_buffer
        buffer = float(buffer)
        int_buffer = round(buffer)
        lbl_buffer['text'] = f'буфер {int_buffer}'

    def sc_fr(freq):
        global int_freq
        if freq == 44100:
            freq = float(freq)
            int_freq = round(freq)
            lbl_frequency['text'] = f'частота {int_freq}'
        else:
            freq = float(freq)
            int_freq = round(freq)
            lbl_frequency['text'] = f'частота {int_freq}'

    equodes = Toplevel()
    equodes.geometry('500x150')
    equodes.resizable(width = False, height = False)
    equodes.title('Эквалайзер')

    canequo = Canvas(equodes, width = 500, height = 300)
    canequo.pack()

    lbl_frequency = Label(canequo, text = f'частота {freq} ', font = ('Nunito', 13))
    lbl_frequency.place(x = 20, y = 30)

    lbl_buffer = Label(canequo, text = f'буфер {buffer} ', font = ('Nunito', 13))
    lbl_buffer.place(x = 180, y = 30)

    lbl_bits = Label(canequo, text = f'разрядность {bits[1]} ', font = ('Nunito', 13))
    lbl_bits.place(x = 300, y = 30)

    sc_frequency = ttk.Scale(canequo, orient = HORIZONTAL, from_ = int(22500), to = int(44100), value = freq, command = sc_fr)
    sc_frequency.place(x = 20, y = 60)

    sc_frequency = ttk.Scale(canequo, orient = HORIZONTAL, from_ = int(256), to = int(1024), value = buffer, command = sc_buf)
    sc_frequency.place(x = 180, y = 60)

    bits_combo = ttk.Combobox(canequo, values = bits, state = 'readonly', font = ('Nunito', 10))
    bits_combo.place(x = 300, y = 60)
    bits_combo.bind("<<ComboboxSelected>>", bits_sel)

    btn_apply = Button(canequo, text = 'apply', font = ('Nunito', 10), command = pg_apply)
    btn_apply.place(x = 400, y = 100)

    if theme == 'sun':
        canequo['bg'] = 'white'
        lbl_frequency.config(fg = 'black', bg = 'white')
        lbl_buffer.config(fg = 'black', bg = 'white')
        lbl_bits.config(fg = 'black', bg = 'white')
        bits_combo.config(foreground = 'black', background = 'white')
        btn_apply.config(bg = 'white', fg = 'black')
    elif theme == 'loon':
        canequo['bg'] = 'black'
        lbl_frequency.config(bg = 'black', fg = 'white')
        lbl_buffer.config(bg = 'black', fg = 'white')
        lbl_bits.config(bg = 'black', fg = 'white')
        btn_apply.config(bg = 'black', fg = 'white')
        bits_combo.config(foreground = 'black', background = 'white')

    equodes.mainloop()

def replace_theme():
    global theme
    if theme == 'sun':
        btn_tray.config(bg = 'black')
        btn_mus_load.config(bg = 'black')
        btn_playlist.config(bg = 'black')
        btn_prog_about.config(bg = 'black')
        btn_mus_downloader.config(bg = 'black')
        btn_mus_play_pause.config(bg = 'black')
        btn_mus_clp.config(bg = 'black')
        btn_mus_left.config(bg = 'black')
        btn_mus_right.config(bg = 'black')
        btn_mus_stop.config(bg = 'black')
        btn_mus_equolizer.config(bg = 'black')

        mus_label.config(bg = 'black', fg = 'white')
        lbl_playlist.config(bg = 'black', fg = 'white')
        dl_mus.config(bg = 'black', fg = 'white')

        btn_theme.config(image = sunico)
        theme = 'loon'
        can['bg'] = 'black'
        can.create_line(0, 210, 190, 210, fill = 'white')
        can.create_line(190, 0, 190, 210, fill = 'white')

        can.create_line(190, 210, 600, 210, fill = 'white')
        can.create_line(190, 110, 600, 110, fill = 'white')

        can.create_line(0, 240, 600, 240, fill = 'white')

        can_mus_job = can.create_image(100, 90, image = mus_job_white)
    elif theme == 'loon':
        btn_tray.config(bg = 'white')
        btn_mus_load.config(bg = 'white')
        btn_playlist.config(bg = 'white')
        btn_prog_about.config(bg = 'white')
        btn_mus_downloader.config(bg = 'white')
        btn_mus_play_pause.config(bg = 'white')
        btn_mus_clp.config(bg = 'white')
        btn_mus_left.config(bg = 'white')
        btn_mus_right.config(bg = 'white')
        btn_mus_stop.config(bg = 'white')
        btn_mus_equolizer.config(bg = 'white')

        mus_label.config(fg = 'black', bg = 'white')
        dl_mus.config(fg = 'black', bg = 'white')
        lbl_playlist.config(fg = 'black', bg = 'white')

        btn_theme.config(image = loonico)
        theme = 'sun'
        can['bg'] = 'white'
        can.create_line(0, 210, 190, 210, fill = 'black')
        can.create_line(190, 0, 190, 210, fill = 'black')

        can.create_line(190, 210, 600, 210, fill = 'black')
        can.create_line(190, 110, 600, 110, fill = 'black')

        can.create_line(0, 240, 600, 240, fill = 'black')

        can_mus_job = can.create_image(100, 90, image = mus_job_black)

def lbl_name_playlist():
    global name_musplay_playlist
    if name_musplay_playlist.count("-") > 0 :
       name_musplay_playlist = name_musplay_playlist.split("-")
       mus_label.configure(text = (f'{name_musplay_playlist[0]}\n{name_musplay_playlist[1]}')) 
 
def add_playlist(name_mus):
    index = 0
    listplaylist.insert(index, name_mus)
    playlist.insert(index, mus_name)
    index += 1
    

def move_remove_playlist():
    global var_btn_playlist
    global playlist_move_remove_panel
    if var_btn_playlist == 0:
        des.geometry('670x300')
        var_btn_playlist = 1
        playlist_move_remove_panel = int(1)
    elif var_btn_playlist == 1:
        des.geometry('480x300')
        var_btn_playlist = 0
        playlist_move_remove_panel = int(0)

def fun_mus_downloader():
    global varurl
    global varname
    global theme

    downdes = Toplevel()
    downdes.title('Скачать')
    downdes.geometry('250x300')
    #downdes.iconbitmap('icons/logo.ico')
    downdes.resizable(width=0, height=0)

    def downget():
        global varname
        global varurl
        varurl = urlentry.get()
        varname = nameentry.get()
        if format_combo.get() == '':
            messagebox.showerror('Скачать', 'Ошибка в url \n или в имени')
        else:
            print('Начнём')
        if varurl == '' or varname == '':
            messagebox.showerror('Скачать', 'Ошибка в url \n или в имени')
        else:
            print('Начнём')
        if directentry.get() == '':
            if os.path.isdir(directentry.get()):
                print('OK')
            else:
                messagebox.showerror('Скачать', 'Ошибка в пути')
        else:
            print('Начнём')
        if urlcombo.get() == 'URL':   
            wget.download(varurl, f'{directentry.get()}{varname}')
            messagebox.showinfo('Скачать', 'скачивание \nуспешное')
        elif urlcombo.get() == 'Youtube URL':
            downdes.title('Пожалуйста подождиите')
            downdes.update()
            yt = YouTube(f'{varurl}')
            ytnm = yt.title
            yt.streams.first().download(directentry.get())
            audioclip = AudioFileClip(f"{directentry.get()}{ytnm}.3gpp")
            audioclip.write_audiofile(filename = f"{directentry.get()}{varname}.{format_combo.get()}", fps = 44100, buffersize = 50000, bitrate = '500k')
            messagebox.showinfo('Скачать', 'скачивание \nуспешное')
            downdes.title('Скачать')
            downdes.update()
            os.remove(f"{directentry.get()}{ytnm}.3gpp")
        elif urlcombo.get() == '':
            messagebox.showerror('Скачать', 'Ошибка в выборе\n типа url')

    downcan = Canvas(downdes, width=250, height=300)
    downcan.pack()
    varnameentry = StringVar()
    lblnameentry = Label(downcan, text = 'Название               формат', font = ('Nunito', 13))
    lblnameentry.place(x=42, y=25)
    nameentry = ttk.Entry(downcan, width = 22)
    nameentry.place(x=12, y = 50)
    format_combo = ttk.Combobox(downcan, font = ('Nunito', 9), values = ('mp3', 'wav', 'ogg'), width = 5, state = 'readonly')
    format_combo.place(x = 197, y = 50)
    varurlentry = StringVar()
    lblurlentry = Label(downcan, text = 'Вставьте URL музыки\nYoutube URL', font = ('Nunito', 10))
    lblurlentry.place(x=62, y=75)
    urlentry = ttk.Entry(downcan, width = 28)
    urlentry.place(x=12, y=125)
    downbtn = ttk.Button(downcan, width = 8, text='Скачать', command=downget)
    downbtn.place(x=85,y=270)
    urlcombo = ttk.Combobox(downcan, font = ('Nunito', 10), state = 'readonly', values = ('URL', 'Youtube URL'))
    urlcombo.place(x = 35, y = 175)
    typeurl = Label(downcan, text = 'Тип URL', font = ('Nunito', 10))
    typeurl.place(x = 85, y = 150)
    directlabel = Label(downcan, text = 'путь для сохранения', font = ('Nunito', 10))
    directlabel.place(x = 65, y = 215)
    directentry = ttk.Entry(downcan, width = 28, font = ('Nunito', 10))
    directentry.place(x = 15, y = 240)

    if theme == 'sun':
        downcan['bg'] = 'white'
        lblurlentry['bg'] = 'white'
        lblurlentry['fg'] = 'black'
        lblnameentry['bg'] = 'white'
        lblnameentry['fg'] = 'black'
        typeurl['bg'] = 'white'
        typeurl['fg'] = 'black'
        directlabel['bg'] = 'white'
        directlabel['fg'] = 'black'
    elif theme == 'loon':
        downcan['bg'] = 'black'
        lblnameentry['bg'] = 'black'
        lblnameentry['fg'] = 'white'
        lblurlentry['bg'] = 'black'
        lblurlentry['fg'] = 'white'
        typeurl['fg'] = 'white'
        typeurl['bg'] = 'black'
        directlabel['fg'] = 'white'
        directlabel['bg'] = 'black'

    downdes.mainloop()

#mus_right
def c_mus_right():
    global update_update
    global mus_loop
    global var_btn_mus_play_pause
    global right_speed
    if right_speed < 0:
        right_speed = float(0.0)
        right_speed = float(right_speed + 1.5)
        pygame.mixer.music.play(start = right_speed)
    else:
        right_speed = float(right_speed + 1.5)
        pygame.mixer.music.play(start = right_speed)
    btn_mus_play_pause.configure(image = mus_pause)
    mus_loop = 2
    var_btn_mus_play_pause = 1
    update_update = False
def c_mus_left():
    global update_update
    global mus_loop
    global var_btn_mus_play_pause
    global right_speed
    right_speed = float(right_speed - 1.5)
    pygame.mixer.music.play(start = right_speed)
    btn_mus_play_pause.configure(image = mus_pause)
    mus_loop = 2
    var_btn_mus_play_pause = 1
    update_update = False

#длительность музыки
def song_duration_time():
     global right_speed
     global mus_loop
     global var_btn_mus_play_pause
     global update_update
     global MUSIC_END
     global mus_end
     global mus_name
     try:
        duration =  AudioFileClip(f'{mus_name}').duration
     except:
        messagebox.showerror('Musplayer', 'файл поврежден')
     duration = int(duration)
     mus_end = 0
     raw_time = pygame.mixer.music.get_pos()/1000
     converted_time = time.strftime("%H:%M:%S",time.gmtime(raw_time))

     mn, sc = divmod(duration, 60)
     hr, mn = divmod(mn, 60)

     us_converted_time = f"{hr}:{mn}:{sc}"
     if update_update == False:
        dl_mus.config(text=f'{str(converted_time)} - {us_converted_time}')
     elif update_update == True:
        dl_mus.config(text=f'{str(converted_time)} - повторение')
     for event in pygame.event.get():
      if event.type == MUSIC_END:
        mus_end = 1
        right_speed = float(0.0)
        dl_mus.config(text="it's music time")
        if update_update == True:
            raw_time = 0
            time.sleep(0.1)
            raw_time = pygame.mixer.music.get_pos()/1000
            converted_time = 0
            time.sleep(0.1)
            converted_time = time.strftime("%H:%M:%S",time.gmtime(raw_time))
        elif update_update == False:
            btn_mus_play_pause.configure(image = mus_play)
            mus_loop = True
            var_btn_mus_play_pause = 0
     if mus_end == 1:
        pass
     else:
        dl_mus.after(1000,song_duration_time)

#открыть файл
def load_mus():
    global mus_name
    global name_mus
    global mus_label
    global mus_loop
    global var_btn_mus_play_pause
    global playlist_move_remove_panel
    mus_name = filedialog.askopenfilename(title = "Выберите любимый трек",filetypes = (("mp3 Файлы","*.mp3"),("ogg Файлы","*.ogg"), ("wav Файлы", "*.wav")))
    pygame.mixer.music.stop()
    if mus_name == '':
        mus_label.config(text = 'Нет музыки')
    else:
     vame_mus=os.path.basename(mus_name)
     if vame_mus.count('y2meta.com - '):
        qname_mus = vame_mus.split('y2meta.com - ')
        name_mus = qname_mus[1]
     else:
        name_mus = vame_mus
    if name_mus.count("-") > 0 :
            bame_mus = name_mus.split("-")
            mus_label.configure(text = (f'{bame_mus[0]}\n{bame_mus[1]}')) 
            des.title(f'{bame_mus[0]}\n{bame_mus[1]}')
    else:
        mus_label.config(text = f'{name_mus}')
        des.title(f'{name_mus}')
    add_playlist(name_mus)
    bytes_name_mus = len(name_mus)
    print(bytes_name_mus)
    if bytes_name_mus < 20:
        mus_label.config(font = ('Nunito', 16))
    elif bytes_name_mus < 30:
        mus_label.config(font = ('Nunito', 15))
    elif bytes_name_mus < 40:
        mus_label.config(font = ('Nunito', 14))
    elif bytes_name_mus < 80:
        mus_label.config(font = ('Nunito', 10))
    if playlist_move_remove_panel == int(0):
        pygame.mixer.music.load(mus_name)
    elif playlist_move_remove_panel == int(1):  
        pygame.mixer.music.queue(mus_name)
    btn_mus_play_pause.configure(image = mus_play)
    mus_loop = True
    var_btn_mus_play_pause = 0
#открыть файл кнопкой l
def l_load_mus(event):
    global mus_name
    global name_mus
    global mus_loop
    global var_btn_mus_play_pause
    global playlist_move_remove_panel
    mus_name = filedialog.askopenfilename(title = "Выберите любимый трек",filetypes = (("mp3 Файлы","*.mp3"),("ogg Файлы","*.ogg"), ("wav Файлы", "*.wav")))
    pygame.mixer.music.stop()
    if mus_name == '':
        mus_label.config(text = 'Нет музыки')
    else:
     vame_mus=os.path.basename(mus_name)
     if vame_mus.count('y2meta.com - '):
        qname_mus = vame_mus.split('y2meta.com - ')
        name_mus = qname_mus[1]
     else:
        name_mus = vame_mus
    if name_mus.count("-") > 0 :
            bame_mus = name_mus.split("-")
            mus_label.configure(text = (f'{bame_mus[0]}\n{bame_mus[1]}')) 
            des.title(f'{bame_mus[0]}\n{bame_mus[1]}')
    else:
        mus_label.config(text = f'{name_mus}')
        des.title(f'{name_mus}')
    add_playlist(name_mus)
    bytes_name_mus = len(name_mus)
    print(bytes_name_mus)
    if bytes_name_mus < 20:
        mus_label.config(font = ('Nunito', 16))
    elif bytes_name_mus < 30:
        mus_label.config(font = ('Nunito', 15))
    elif bytes_name_mus < 40:
        mus_label.config(font = ('Nunito', 14))
    elif bytes_name_mus < 60:
        mus_label.config(font = ('Nunito', 10))
    if playlist_move_remove_panel == int(0):
        pygame.mixer.music.load(mus_name)
    elif playlist_move_remove_panel == int(1):  
        pygame.mixer.music.queue(mus_name)
    btn_mus_play_pause.configure(image = mus_play)
    mus_loop = True
    var_btn_mus_play_pause = 0
#повторять музыку
def mus_update():
    global update_update
    global update_mus
    global mus_loop
    if update_update == False:
        pygame.mixer.music.stop()
        c_mus_stop()
        update_update = True
        mus_loop = True
        messagebox.showinfo('повторение','повторение\nвключено')
    elif update_update == True:
        pygame.mixer.music.stop()
        c_mus_stop()
        update_update = False
        mus_loop = True
        messagebox.showinfo('повторение','повторение\nвыключено')
def r_mus_update(event):
    global update_update
    global update_mus
    global mus_loop
    if update_update == False:
        pygame.mixer.music.stop()
        update_update = True
        mus_loop = True
        messagebox.showinfo('повторение','повторение\nвключено')
    elif update_update == True:
        pygame.mixer.music.stop()
        update_update = False
        mus_loop = True
        messagebox.showinfo('повторение','повторение\nвыключено')

def mus_play_pause():
    global name_musplay_playlist
    global playlist
    global musplay_playlist
    global selplaylist
    global var_btn_mus_play_pause
    global mus_loop
    global update_update
    global update_mus
    global right_speed
    global playlist_move_remove_panel
    if var_btn_mus_play_pause == 0:
        if mus_loop == NO:
         var_btn_mus_play_pause = 1
         btn_mus_play_pause.configure(image = mus_pause)
         print(mus_loop, var_btn_mus_play_pause)
         messagebox.showwarning('musplayer', 'нет загруженной музыыки')
         btn_mus_play_pause.configure(image = mus_play)
         mus_loop = NO
         var_btn_mus_play_pause = 0
        if mus_loop == True:
            if update_update == True:
             if playlist_move_remove_panel == int(1):
              var_btn_mus_play_pause = 1
              btn_mus_play_pause.configure(image = mus_pause)
              right_speed = float(0.0)
              selplaylist = listplaylist.curselection()
              selplaylist = int(selplaylist[0])
              musplay_playlist = playlist[selplaylist]
              name_musplay_playlist = os.path.basename(musplay_playlist)
              pygame.mixer.music.stop()
              pygame.mixer.music.load(musplay_playlist)
              try:
                pygame.mixer.music.play(loops=update_mus)
              except:
                messagebox.showerror('Musplayer', 'Ошибка в повторении музыки\nфайл поврежден')
              des.title(name_musplay_playlist)
              lbl_name_playlist()
             elif playlist_move_remove_panel == int(0):
                var_btn_mus_play_pause = 1
                btn_mus_play_pause.configure(image = mus_pause)
                right_speed = float(0.0)
                des.title(name_mus)
                pygame.mixer.music.play(loops = update_mus)
             song_duration_time()
            elif update_update == False:
             if playlist_move_remove_panel == int(1):
              var_btn_mus_play_pause = 1
              btn_mus_play_pause.configure(image = mus_pause)
              right_speed = float(0.0)
              selplaylist = listplaylist.curselection()
              selplaylist = int(selplaylist[0])
              musplay_playlist = playlist[selplaylist]
              name_musplay_playlist = os.path.basename(musplay_playlist)
              pygame.mixer.music.load(musplay_playlist)
              try:
                pygame.mixer.music.play()
              except:
                messagebox.showerror('Musplayer', 'Ошибка в музыки\nфайл поврежден')
              des.title(name_musplay_playlist)
              lbl_name_playlist()
             elif playlist_move_remove_panel == int(0):
              des.title(name_mus)
              var_btn_mus_play_pause = 1
              btn_mus_play_pause.configure(image = mus_pause)
              right_speed = float(0.0)
              try:
                pygame.mixer.music.play() 
              except:
                messagebox.showerror('Musplayer', 'Ошибка в музыки\nфайл поврежден')
             song_duration_time()
        elif mus_loop == 2:
         var_btn_mus_play_pause = 1
         btn_mus_play_pause.configure(image = mus_pause)
         pygame.mixer.music.unpause()
    else:
        if mus_loop == 1:
         var_btn_mus_play_pause = 0
         mus_loop = 2
         btn_mus_play_pause.configure(image = mus_play)
         pygame.mixer.music.pause()
        elif mus_loop == NO:
         var_btn_mus_play_pause = 0
         btn_mus_play_pause.configure(image = mus_play)
         pygame.mixer.music.pause()
         messagebox.showwarning('musplayer', 'no integreted audio')
        elif mus_loop == 2:
         var_btn_mus_play_pause = 0
         btn_mus_play_pause.configure(image = mus_play)
         pygame.mixer.music.pause()

#кнопка плей но для пробела
def space_mus_play_pause(event):
    global name_musplay_playlist
    global playlist
    global musplay_playlist
    global selplaylist
    global var_btn_mus_play_pause
    global mus_loop
    global update_update
    global update_mus
    global right_speed
    global playlist_move_remove_panel
    if var_btn_mus_play_pause == 0:
        if mus_loop == NO:
         var_btn_mus_play_pause = 1
         btn_mus_play_pause.configure(image = mus_pause)
         print(mus_loop, var_btn_mus_play_pause)
         messagebox.showwarning('musplayer', 'нет загруженной музыки')
         btn_mus_play_pause.configure(image = mus_play)
         mus_loop = NO
         var_btn_mus_play_pause = 0
        if mus_loop == True:
            if update_update == True:
             if playlist_move_remove_panel == int(1):
              var_btn_mus_play_pause = 1
              btn_mus_play_pause.configure(image = mus_pause)
              right_speed = float(0.0)
              selplaylist = listplaylist.curselection()
              selplaylist = int(selplaylist[0])
              musplay_playlist = playlist[selplaylist]
              name_musplay_playlist = os.path.basename(musplay_playlist)
              pygame.mixer.music.stop()
              pygame.mixer.music.load(musplay_playlist)
              try:
               pygame.mixer.music.play(loops=update_mus)
              except:
                messagebox.showerror('Musplayer', 'Ошибка в повторении музыки\nфайл поврежден')
              des.title(name_musplay_playlist)
              lbl_name_playlist()
             elif playlist_move_remove_panel == int(0):
                var_btn_mus_play_pause = 1
                btn_mus_play_pause.configure(image = mus_pause)
                right_speed = float(0.0)
                des.title(name_mus)
                try:
                    pygame.mixer.music.play(loops = update_mus)
                except:
                    messagebox.showerror('Musplayer', 'Ошибка в повторении музыки\nфайл поврежден')
             song_duration_time()
            elif update_update == False:
             if playlist_move_remove_panel == int(1):
              var_btn_mus_play_pause = 1
              btn_mus_play_pause.configure(image = mus_pause)
              right_speed = float(0.0)
              selplaylist = listplaylist.curselection()
              selplaylist = int(selplaylist[0])
              musplay_playlist = playlist[selplaylist]
              name_musplay_playlist = os.path.basename(musplay_playlist)
              pygame.mixer.music.load(musplay_playlist)
              try:
                pygame.mixer.music.play()
              except:
                messagebox.showerror('Musplayer', 'Ошибка в музыки\nфайл поврежден')
              des.title(name_musplay_playlist)
              lbl_name_playlist()
             elif playlist_move_remove_panel == int(0):
              des.title(name_mus)
              var_btn_mus_play_pause = 1
              btn_mus_play_pause.configure(image = mus_pause)
              right_speed = float(0.0)
              try:
                pygame.mixer.music.play() 
              except:
                messagebox.showerror('Musplayer', 'Ошибка в музыки\nфайл поврежден')
             song_duration_time()
        elif mus_loop == 2:
         var_btn_mus_play_pause = 1
         btn_mus_play_pause.configure(image = mus_pause)
         pygame.mixer.music.unpause()
    else:
        if mus_loop == 1:
         var_btn_mus_play_pause = 0
         mus_loop = 2
         btn_mus_play_pause.configure(image = mus_play)
         pygame.mixer.music.pause()
        elif mus_loop == NO:
         var_btn_mus_play_pause = 0
         btn_mus_play_pause.configure(image = mus_play)
         pygame.mixer.music.pause()
         messagebox.showwarning('musplayer', 'нет загруженной музыки')
        elif mus_loop == 2:
         var_btn_mus_play_pause = 0
         btn_mus_play_pause.configure(image = mus_play)
         pygame.mixer.music.pause()

def fun_prog_about():
    global upbut
    abdes = Toplevel()
    abdes.title('о musplayer')
    abdes.geometry('494x244+420+170')
    #abdes.iconbitmap('icons/logo.ico')
    abdes.resizable(width=0, height=0)

    def updateapp():
        global nupbut
        global nnup
        global upbut
        global theme
        wget.download('https://gitlab.com/lbhnik12/comine/-/raw/main/musplayer.txt?inline=false')
        nupbut = open('musplayer.txt', 'r')
        nnup = float(nupbut.readline())
        if upbut < nnup:
            webbrowser.open_new_tab('https://disk.yandex.ru/d/OH4HGaTunun94g')
            nupbut.close()
            os.remove('musplayer.txt')
        else:
            messagebox.showinfo('version', 'the present\nversion')
            nupbut.close()
            os.remove('musplayer.txt')
    abcan = Canvas(abdes, width= 494, height=244, bg='white')
    abcan.pack()
    if theme == 'sun':
        absp = PhotoImage(file = 'src/about_splash_white.png')
        ablbl = Label(abcan, text = f'musplayer\nверсия {upbut}\nСделал WebMast', font=('Arial', 20), fg = '#000', bg='#FFF')
        upim = PhotoImage(file = 'src/update_black.png')
        upbutton = Button(abcan, image=upim, highlightthickness=0, bd=0, bg = 'white', command = updateapp)
    elif theme == 'loon':
        absp = PhotoImage(file = 'src/about_splash_black.png')
        upim = PhotoImage(file = 'src/update_white.png')
        ablbl = Label(abcan, text = f'musplayer\nверсия {upbut}\nСделал WebMast', font=('Arial', 20), fg = '#FFF', bg='black')
        upbutton = Button(abcan, image=upim, highlightthickness=0, bd=0, bg = 'black', command = updateapp)
    spcan = abcan.create_image(245,120, image = absp)
    ablbl.place(x=200, y=10)
    upbutton.place(x=265, y=120)
    abdes.mainloop()
def c_mus_stop():
    global right_speed
    global btn_mus_play_pause
    global mus_loop
    global var_btn_mus_play_pause
    pygame.mixer.music.stop()
    btn_mus_play_pause.configure(image = mus_play)
    mus_loop = True
    var_btn_mus_play_pause = 0
    right_speed = float(0.0)
    dl_mus.config(text = "время музыки")

#стоп кнопкой s
def s_mus_stop(event):
    global right_speed
    global btn_mus_play_pause
    global mus_loop
    global var_btn_mus_play_pause
    pygame.mixer.music.stop()
    btn_mus_play_pause.configure(image = mus_play)
    mus_loop = True
    var_btn_mus_play_pause = 0
    right_speed = float(0.0)
    dl_mus.config(text = "время музыки")

def close():
    sys.exit()

def on_closing():
    global mus_loop
    global playning
    global theme
    playning = 'not_play'

    def tray_mus_update():
        global update_update
        global playning
        global mus_loop
        if update_update == False:
            pygame.mixer.music.stop()
            update_update = True
            playning = 'get_play'
            mus_loop = True
            notify_support = icon_tray.HAS_NOTIFICATION
            if notify_support == True:
                icon_tray.notify('повторение включено', 'musplayer')
            elif notify_support == False:
                print('Уведомления не работают в этой ОС')
                print('повторение включено')
        elif update_update == True:
            pygame.mixer.music.stop()
            playning = 'get_play'
            mus_loop = True
            update_update = False
            notify_support = icon_tray.HAS_NOTIFICATION
            if notify_support == True:
                icon_tray.notify('повторение выключено', 'musplayer')
            elif notify_support == False:
                print('Уведомления не работают в этой ОС')
                print('повторение включено')

    def mustray_version():
        global upbut
        icon_tray.notify(f'версия {upbut}', 'musplayer')

    def mustray_play_on_pause():
        global playning
        global mus_loop
        if playning == 'get_play':
            if mus_loop == True:
                if update_update == True:
                 mus_loop = 2
                 try:
                  pygame.mixer.music.play(loops = 10000)
                  notify_support = icon_tray.HAS_NOTIFICATION
                  if notify_support == True:
                     icon_tray.notify('проигрывание с повторением', 'musplayer')
                  elif notify_support == False:
                    print('Уведомления не работают в этой ОС')
                    print('проигрывание с повторением')
                 except:
                  if notify_support == True:
                    icon_tray.notify('файл поврежден', 'musplayer')
                  elif notify_support == False:
                    print('Уведомления не работают в этой ОС')
                    print('файл поврежден')
                elif update_update == False:
                 mus_loop = 2
                 try:
                  pygame.mixer.music.play()
                  notify_support = icon_tray.HAS_NOTIFICATION
                  if notify_support == True:
                     icon_tray.notify('проигрывание ', 'musplayer')
                  elif notify_support == False:
                     print('Уведомления не работают в этой ОС')
                     print('проигрывание')
                 except:
                    if notify_support == True:
                        icon_tray.notify('файл поврежден', 'musplayer')
                    elif notify_support == False:
                        print('Уведомления не работают в этой ОС')
                        print('файл поврежден')
                playning = 'play'
        elif playning == 'play':
            pygame.mixer.music.pause()
            playning = 'pause'
            notify_support = icon_tray.HAS_NOTIFICATION
            if notify_support == True:
                icon_tray.notify('пауза ', 'musplayer')
            elif notify_support == False:
                print('Уведомления не работают в этой ОС')
                print('пауза')
        elif playning == 'pause':
            pygame.mixer.music.unpause()
            playning = 'unpause'
            notify_support = icon_tray.HAS_NOTIFICATION
            if notify_support == True:
                icon_tray.notify('возобновление ', 'musplayer')
            elif notify_support == False:
                print('Уведомления не работают в этой ОС')
                print('возобновление')
        elif playning == 'unpause':
            pygame.mixer.music.pause()
            playning = 'pause'
            notify_support = icon_tray.HAS_NOTIFICATION
            if notify_support == True:
                icon_tray.notify('пауза ', 'musplayer')
            elif notify_support == False:
                print('Уведомления не работают в этой ОС')
                print('пауза')

    def mustray_stop():
        global playning
        global mus_loop
        pygame.mixer.music.stop()
        playning = 'get_play'
        mus_loop = True

    def mustray_load():
       global playning
       global mus_loop
       global name_mus
       global oname_mus
       global mus_name
       mus_name = filedialog.askopenfilename(title = "Выберите любимый трек",filetypes = (("mp3 Файлы","*.mp3"),("ogg Файлы","*.ogg"), ("wav Файлы", "*.wav"))) 
       if mus_name == '':
        pass
       else:
        playning = 'get_play'
       vame_mus=os.path.basename(mus_name)
       if vame_mus.count('y2meta.com - '):
        qname_mus = vame_mus.split('y2meta.com - ')
        name_mus = qname_mus[1]
        oname_mus = name_mus
       else:
        name_mus, oname_mus = vame_mus
       pygame.mixer.music.load(mus_name)
       notify_support = icon_tray.HAS_NOTIFICATION
       if notify_support == True:
        icon_tray.notify(f'загружен\n{name_mus}', 'musplayer')
       elif notify_support == False:
        print('Уведомления не работают в этой ОС')
        print(f'загружен\n{name_mus}')  
       mus_loop = True 
    def musplayer_exit():
        sys.exit()

    def return_label():
        global oname_mus
        global mus_label

        bytes_name_mus = len(name_mus)
        if bytes_name_mus < 20:
            mus_label.config(font = ('Nunito', 16))
        elif bytes_name_mus < 30:
            mus_label.config(font = ('Nunito', 15))
        elif bytes_name_mus < 40:
            mus_label.config(font = ('Nunito', 14))
        elif bytes_name_mus < 60:
            mus_label.config(font = ('Nunito', 10))
        if oname_mus.count("-") > 0 :
            bame_mus = oname_mus.split("-")
            mus_label.configure(text = (f'{bame_mus[0]}\n{bame_mus[1]}')) 
            des.title(f'{bame_mus[0]}\n{bame_mus[1]}')
        else:
            mus_label.config(text = f'{name_mus}')

    def return_des():
        global mus_loop
        global playning
        global var_btn_mus_play_pause
        global name_mus
        global mus_label
        global mus_name
        if playning == 'play':
            des.title(f'{name_mus}')
            #mus_label.config(text = f'{name_mus}')
            btn_mus_play_pause.config(image = mus_pause)
            var_btn_mus_play_pause = 1
        elif playning == 'pause':
            mus_loop = 2 
            des.title(f'{name_mus}')
            #mus_label.config(text = f'{name_mus}')
            btn_mus_play_pause.configure(image = mus_play)
            var_btn_mus_play_pause = 0
        elif playning == 'get_play':
            mus_loop = True
            des.title(f'{name_mus}')
            #mus_label.config(text = f'{name_mus}')
            btn_mus_play_pause.configure(image = mus_play)
            var_btn_mus_play_pause = 0
        if mus_name == '':
            pass
        else:
            song_duration_time()
        des.deiconify()
        return_label()
        icon_tray.stop()


    des.withdraw()
    #трей
    if theme == 'sun':
        image_icon_png = PIL.Image.open('icons/logo_white.png')
    elif theme == 'loon':
        image_icon_png = PIL.Image.open('icons/logo_black.png')
    icon_tray = pystray.Icon('musplayer', image_icon_png, menu = pystray.Menu(
    pystray.MenuItem('play/pause', mustray_play_on_pause),
    pystray.MenuItem('stop', mustray_stop),
    pystray.MenuItem('repeat',tray_mus_update),
    pystray.MenuItem('load', mustray_load),
    pystray.MenuItem('version', mustray_version),
    pystray.MenuItem('exit', musplayer_exit),
    pystray.MenuItem('return program format', pystray.Menu(
        pystray.MenuItem('window format', return_des),
    )),
   ))
    icon_tray.run()

def esc_mus_exit(event):
    sys.exit()

#для рисовки кнопок и разных приколюх
can = Canvas(des, width=810, height=530, bg='white')
can.place(x=0, y=1)
#значок обложки
mus_job_white = PhotoImage(file = 'src/mus_job_white.png')
mus_job_black = PhotoImage(file = 'src/mus_job_black.png')
can_mus_job = can.create_image(100, 90, image = mus_job_black)
#открыть файл фотка и кнопка
mus_load = PhotoImage(file = 'src/mus_load.png')
btn_mus_load = Button(can, image=mus_load, highlightthickness=0, bg='white', bd=0, command=load_mus)
btn_mus_load.place(x=300, y=115)
#кнопка паузы и игры и их фотки а также переменная
mus_play = PhotoImage(file='src/mus_play.png')
mus_pause = PhotoImage(file='src/mus_pause.png')
btn_mus_play_pause = Button(can, image=mus_play, highlightthickness=0, bg = 'white', bd=0, command = mus_play_pause)
btn_mus_play_pause.place(x = 190, y=245)
var_btn_mus_play_pause = 0
#о программе
prog_about = PhotoImage(file = 'src/prog_about.png')
btn_prog_about = Button(can, image=prog_about, highlightthickness=0, bg='white', bd=0, command=fun_prog_about)
btn_prog_about.place(x=250, y=115)
#реакция на кнопку закрыть
des.protocol("WM_DELETE_WINDOW", close)
#название музыки
mus_label = Label(can, text = name_mus, font=('Nunito', 16), bg= 'white', fg = 'black')
mus_label.place(x=195, y=10)
#повтор
update_mus = 10000
update_update = False
mus_clp = PhotoImage(file = 'src/mus_clp.png')
btn_mus_clp = Button(can, image=mus_clp, highlightthickness=0, bg='white', bd=0, command=mus_update)
btn_mus_clp.place(x=240, y=245)
#стоп
mus_stop = PhotoImage(file='src/mus_stop.png')
btn_mus_stop = Button(can, image=mus_stop, highlightthickness=0, bg='white', bd=0, command=c_mus_stop)
btn_mus_stop.place(x = 140, y = 245)
#в трей!
tray = PhotoImage(file='src/tray.png')
btn_tray = Button(can, image=tray, highlightthickness=0, bg='white', bd=0, command=on_closing)
btn_tray.place(x = 200, y = 115)
#разделитель на колонки
can.create_line(0, 210, 190, 210, fill = 'black')
can.create_line(190, 0, 190, 210, fill = 'black')

can.create_line(190, 210, 600, 210, fill = 'black')
can.create_line(190, 110, 600, 110, fill = 'black')

can.create_line(0, 240, 600, 240, fill = 'black')
#время музыки
dl_mus = Label(can, text = "время музыки", bg='white', font = ('Nunito', 14), fg = 'black')
dl_mus.place(x=160, y=211)
#пролистать длительность направо
mus_right = PhotoImage(file = 'src/mus_right.png')
btn_mus_right = Button(can, image = mus_right, highlightthickness=0, bd = 0, bg = 'white', command = c_mus_right)
btn_mus_right.place(x= 300, y=245)
#пролистать длительность направо
mus_left = PhotoImage(file = 'src/mus_left.png')
btn_mus_left = Button(can, image = mus_left, highlightthickness=0,bg='white', bd = 0, command = c_mus_left)
btn_mus_left.place(x= 30, y=245)
#скачиватель музыки
mus_downloader = PhotoImage(file = 'src/mus_download.png')
btn_mus_downloader = Button(can, image=mus_downloader, highlightthickness=0, bg='white', bd=0, command=fun_mus_downloader)
btn_mus_downloader.place(x=350, y=115)
#кнопка плейлиста
playlist = []
im_playlist = PhotoImage(file = 'src/mus_playlist.png')
btn_playlist = Button(can, image= im_playlist, highlightthickness=0, bd=0, bg='white', command=move_remove_playlist )
btn_playlist.place(x=204, y=165)
var_btn_playlist = 0
#отображение списка в плейлисте
listplaylist = Listbox(can, width=22, height=13, selectmode=EXTENDED, font = ('Nunito', 10))
listplaylist.place(x = 488, y = 38)
#лабель о плейлисте
lbl_playlist = Label(text='Плейлист', bg = 'white', font = ('Nunito', 10))
lbl_playlist.place(x=550, y=15)
#смена темы интерфейса
loonico = PhotoImage(file = 'src/icon_loon.png')
sunico = PhotoImage(file = 'src/icon_sun.png')
btn_theme = Button(can, image = loonico, highlightthickness = 0, bg = 'white', bd = 0, command = replace_theme)
btn_theme.place(x = 254,y = 165)
#эквалайзер
mus_equolizer = PhotoImage(file = 'src/mus_equolizer.png')
btn_mus_equolizer = Button(can, image = mus_equolizer, highlightthickness = 0, bg = 'white', bd = 0, command = equo)
btn_mus_equolizer.place(x = 304, y = 165)
#кнопка "l" 
des.bind('<l>', l_load_mus)
#кнопка "s"
des.bind('<s>', s_mus_stop)
#кнопка "escape"
des.bind('<Escape>', esc_mus_exit)
#кнопка "r"
des.bind('<r>', r_mus_update)
#кнопка "space"
des.bind('<space>', space_mus_play_pause)
#вывод гуая
des.mainloop()
