from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def baixar_musica_mp3():
    url = entry_url.get()
    caminho_destino = filedialog.askdirectory()

    try:
        # Cria um objeto YouTube com a URL do vídeo
        video = YouTube(url)

        # Obtém o stream de áudio com o formato MP3
        stream = video.streams.filter(
            only_audio=True, file_extension='mp4').first()

        # Baixa o áudio para o diretório especificado
        stream.download(output_path=caminho_destino)

        resultado_label.config(
            text=f"Download concluído: {video.title} (formato MP3)")
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
