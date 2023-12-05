from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title('Music Player(mp3)')     ########### TITLE ################
root.geometry("600x460")               ###### H&W ########

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []         ###### ARRAY ####
current_song = "" ########### DEFAULT EMPTY ############
paused = False    ############ BY DEFAULT ###############
################################# LOAD MP3 FUNC ##########################################3
def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    songs.clear()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    songlist.delete(0, END)
    for song in songs:
        songlist.insert(END, song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]
####################################### PLAY ###############################################
def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
############################################# PAUSE ###########################################
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True
######################################## FORWARD (NEXT) ###########################################
def next_music():
    global current_song, paused
    try:
        next_index = (songs.index(current_song) + 1) % len(songs)
        songlist.selection_clear(0, END)
        songlist.selection_set(next_index)
        current_song = songs[next_index]
        play_music()
    except ValueError:
        pass
################################## PREVIOUS MUSIC #####################################################
def prev_music():
    global current_song, paused
    try:
        prev_index = (songs.index(current_song) - 1) % len(songs)
        songlist.selection_clear(0, END)
        songlist.selection_set(prev_index)
        current_song = songs[prev_index]
        play_music()
    except ValueError:
        pass
##########################################  ABOUT SECTION #####################################################
def show_info():
    info_label.config(text="Hello👋, \n I am Rajarshi Sarkar😊.\n I am creating a Python MP3 player GUI😉,\n featuring a user-friendly interface for selecting and playing MP3 files🤗.")

######### label to display (font & size) TEXT #################
info_label = Label(root, text="", font=("Helvetica", 12))
info_label.pack(pady=10)

############## button for ABOUT SECTION #############
info_btn = Button(root, text="About For This Program", command=show_info)
info_btn.pack(pady=5)
#################### MP3 (find) SELECT FOLDER HERE #####################################################################
Browse_menu = Menu(menubar, tearoff=False)
Browse_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Browse', menu=Browse_menu)
############################### BOX (design) FOR MP3 FILES HERE YOU SEE YOUR MP3 FILE'S ####################################################
songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

control_frame = Frame(root)
control_frame.pack()
##########################################  BUTTONS HERE ############################################
play_btn = Button(control_frame, text='Play', command=play_music)
pause_btn = Button(control_frame, text='Pause', command=pause_music)
next_btn = Button(control_frame, text='Next', command=next_music)
prev_btn = Button(control_frame, text='Previous', command=prev_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()
