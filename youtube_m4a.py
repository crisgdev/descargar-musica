import subprocess
import json
import os
from mutagen.mp4 import MP4


def get_video_info(url):
    cmd = ["yt-dlp", "--dump-json", "--no-download", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Error al obtener info: {result.stderr.strip()}")
    return json.loads(result.stdout)


def download_m4a(url, output_path):
    cmd = [
        "yt-dlp",
        "-f", "worstaudio[ext=m4a]/worstaudio",
        "-o", output_path,
        "--no-playlist",
        url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Error al descargar: {result.stderr.strip()}")


def set_metadata(filepath, title, artist):
    audio = MP4(filepath)
    audio["\xa9nam"] = [title]
    audio["\xa9ART"] = [artist]
    audio.save()


def main():
    urls = ["https://www.youtube.com/watch?v=IN22qZp2Szk",
            "https://www.youtube.com/watch?v=FiNSN7fCUYY"]

    if not urls:
        print("No hay links. Agrega URLs en la lista 'urls' del script.")
        return

    print(f"=== Descargando {len(urls)} video(s) ===\n")

    for i, url in enumerate(urls, 1):
        try:
            info = get_video_info(url)

            original_title = info.get("title", "Sin titulo")
            original_artist = info.get("uploader", "Desconocido")

            print(f"[{i}/{len(urls)}] {original_title}")

            custom_title = input("  Titulo personalizado: ").strip()
            final_title = custom_title if custom_title else original_title

            custom_artist = input("  Artista personalizado: ").strip()
            final_artist = custom_artist if custom_artist else original_artist

            safe_title = "".join(c for c in final_title if c.isalnum() or c in " -_").strip()
            output_path = os.path.join(r"C:\Users\USER\Music", f"{safe_title}.m4a")

            download_m4a(url, output_path)

            if os.path.exists(output_path):
                set_metadata(output_path, final_title, final_artist)
                print("  DESCARGA COMPLETADA\n")
            else:
                print("  Error: archivo no encontrado\n")

        except Exception as e:
            print(f"  Error: {e}\n")

    print("=== Listo ===")


if __name__ == "__main__":
    main()
