import os
import yt_dlp

def download_youtube_video_yt_dlp(url, output_folder="downloads"):
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

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Baixando e convertendo o vídeo para MP3...")
            ydl.download([url])
            print("Download e conversão concluídos!")
    except Exception as e:
        print(f"Erro ao baixar/converter o vídeo: {e}")

def main():
    url = input("Digite a URL do vídeo do YouTube: ")
    download_youtube_video_yt_dlp(url)

if __name__ == "__main__":
    main()
