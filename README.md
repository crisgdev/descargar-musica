# descargar-musica

Script en Python para descargar audio (m4a) de YouTube y asignar metadatos
(titulo y artista) usando yt-dlp y mutagen.

## Requisitos

- Python 3.x
- yt-dlp
- mutagen

## Uso

1. Edita la lista urls en youtube_m4a.py con los enlaces de YouTube.
2. Ejecuta: python youtube_m4a.py
3. Ingresa titulo y artista personalizados cuando se solicite
   (o deja vacio para usar los del video).

El audio se guarda en C:\Users\<usuario>\Music
(ajusta la ruta en el script si es necesario).
