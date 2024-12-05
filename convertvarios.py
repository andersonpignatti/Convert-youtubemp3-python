import os
import yt_dlp

def download_youtube_video_yt_dlp(urls, output_folder="downloads"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    for url in urls:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Baixando e convertendo o vídeo: {url}")
                ydl.download([url])
                print("Download e conversão concluídos!")
        except Exception as e:
            print(f"Erro ao processar o vídeo ({url}): {e}")

def read_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Divide as URLs usando vírgulas como separador e remove espaços extras
            urls = [url.strip() for url in content.split(',')]
            return urls
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []

def main():
    file_path = input("Digite o caminho do arquivo de texto com as URLs: ")
    urls = read_urls_from_file(file_path)
    
    if urls:
        print(f"Encontradas {len(urls)} URLs no arquivo.")
        download_youtube_video_yt_dlp(urls)
    else:
        print("Nenhuma URL válida encontrada.")

if __name__ == "__main__":
    main()
