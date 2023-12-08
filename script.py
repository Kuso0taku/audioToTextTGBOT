import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence


class STT:

    def AudioFile(self, path, language='ru-RU'):
        r = sr.Recognizer()
        with sr.AudioFile(path) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language=language)
            return text


    def LargeAudioFile(self, path, language='ru-RU'):
        sound = AudioSegment.from_file(path)
        chunks = split_on_silence(
            sound,
            min_silence_len=500,
            silence_thresh=sound.dBFS-14,
            keep_silence=500
        )
        folder_name = 'audio-chunks'
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)

        whole_text = ''
        for i, audio_chunk in enumerate(chunks):
            chunk_filename = os.path.join(folder_name, f'chunk{i}.wav')
            audio_chunk.export(chunk_filename, format='wav')

            try:
                text = self.AudioFile(chunk_filename, language)
            except sr.UnknownValueError as error:
                # print(f'Error: {str(error)}')
                pass
            else:
                text = f'{text.capitalize()}. '
                whole_text += text

        for file in os.listdir(folder_name):
            file = os.path.join(folder_name, file)
            os.remove(file)
        os.rmdir(folder_name)

        return whole_text
