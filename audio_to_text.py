import speech_recognition as sr
from pydub import AudioSegment
from googletrans import Translator
import os

def mp3_to_text(mp3_file, chunk_length_ms=60000):  # Divide into 60-second chunks
    try:
        audio = AudioSegment.from_mp3(mp3_file)
        chunks = [audio[i:i+chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
        
        recognizer = sr.Recognizer()
        full_text = ""
        
        for i, chunk in enumerate(chunks):
            chunk.export(f"temp{i}.wav", format="wav")
            with sr.AudioFile(f"temp{i}.wav") as source:
                audio_data = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio_data, language='es-ES')
                    full_text += text + " "
                except sr.RequestError as e:
                    print(f"Request error: {e}")
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio in chunk {i}")
                os.remove(f"temp{i}.wav")
        
        return full_text.strip() if full_text else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def translate_text(text, src_lang='es', dest_lang='en'):
    try:
        translator = Translator()
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return None

def save_to_file(text, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def main(mp3_file, output_file, src_lang='es', dest_lang='en'):
    text = mp3_to_text(mp3_file)
    if text:
        save_to_file(text, output_file)
        # translated_text = translate_text(text, src_lang, dest_lang)
        # if translated_text:
        #     save_to_file(translated_text, output_file)
        # else:
        #     print("Translation failed. Saving original text.")
        #     save_to_file(text, output_file)
    else:
        print("No text was extracted from the audio.")

if __name__ == "__main__":
    mp3_file = "input.mp3"  # Change to your MP3 file name
    output_file = "translated_text.txt"
    output_file_original = "translated_text.txt"
    main(mp3_file, output_file)
