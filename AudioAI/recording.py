import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from gtts import gTTS

def transcribe_audio(audio_file):
    r = sr.Recognizer()
     try:
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print("Error occurred during speech recognition: {0}".format(e))

def recording(duration, recorded_audio_file):
    duration = 5
    sample_rate = 44100
    channels = 2

    print("Recording started...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)

    sd.wait()
    output_file = recorded_audio_file
    sf.write(output_file, audio, sample_rate,format='wav')

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

