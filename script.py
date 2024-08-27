import yt_dlp
import tkinter as tk
from tkinter import filedialog

def baixar_musica_mp3():
    url = entry_url.get()
    caminho_destino = filedialog.askdirectory()

    try:
        # Configuração do yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            resultado_label.config(
                text=f"Download concluído: {info_dict['title']} (formato MP3)"
            )
    except Exception as e:
        resultado_label.config(text=f"Erro durante o download: {e}")

# Criar a janela principal
janela = tk.Tk()
janela.title("Baixar Música MP3")

# Criar e posicionar widgets
label_url = tk.Label(janela, text="URL do vídeo:")
label_url.pack(pady=10)

entry_url = tk.Entry(janela, width=50)
entry_url.pack(pady=10)

button_procurar = tk.Button(
    janela, text="Procurar Destino", command=baixar_musica_mp3)
button_procurar.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

# Iniciar o loop da interface gráfica
janela.mainloop()
