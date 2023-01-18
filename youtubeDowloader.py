from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil

#Função que permite ao usuário selecionar um caminho do diretório
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

#Função que permite ao usuário fazer o dowload

def download_file():
    get_link = link_field.get() # caminho do usuario

    #obter caminho selecionado
    user_path = path_label.cget("text")
    screen.title('Baixando...')

    #Baixar o video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

    shutil.move(mp4_video, user_path)
    screen.title('Download completo! Baixar outro arquivo...')

screen = Tk()
titulo = screen.title('Youtube Dowload')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#Logo
logo_img = PhotoImage(file='yt.png')
logo_img = logo_img.subsample(4,4) #redimencionar tamanho
canvas.create_image(250, 80, image = logo_img) #adicionar a imagem na tela de layout

#Campo do Link
link_field = Entry(screen, width=40, font=('Arial', 12))
link_label = Label(screen, text="Insira o link de download: ", font=('Arial', 12))

#Selecione o caminho para salvar o arquivo
path_label = Label(screen, text="Selecione o caminho para download", font=('Arial', 12))
select_btn = Button(screen, text="Selecione o caminho", bg='red', padx='22', pady='5',font=('Arial', 12), fg='#fff', command=select_path)

#Adicionar a Janela
canvas.create_window(250, 280 , window=path_label )
canvas.create_window(250, 330 , window=select_btn )

#Adicionar widgets à janela
canvas.create_window(250, 170 , window=link_label )
canvas.create_window(250, 220 , window=link_field )

#Botão de Dowload
dowload_btn = Button(screen, text="⇬ Download",bg='green', padx='22', pady='5',font=('Arial', 12), fg='#fff', command=download_file)
canvas.create_window(250, 390, window=dowload_btn) #add no canvas

screen.mainloop()