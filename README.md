# Pasar audio a texto con Pyton 

Código Generado Con Copilot

Asegúrate de que el archivo MP3 esté en el mismo directorio llamado input.mp3 o proporcionar la ruta correcta. Instala las dependencias si no lo has hecho:

```bash
pip install speechrecognition pydub googletrans==4.0.0-rc1
```
Instala FFmpeg si no lo has hecho:

- En macOS (usando Homebrew):
```zsh
brew install ffmpeg
```
- En Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```
Luego el proyecto se corre con el siguiente comando
```zsh
python audio_to_text.py
```
Al final genera un archivo 

translated_text.texto

Hay una parte en el codigo que permite traducir el texto a ingles u otro idioma pero por el momento lo deshabilite porque ya tenia lo que necesitaba.
