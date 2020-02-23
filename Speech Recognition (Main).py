from speech_recognition import Recognizer , Microphone , UnknownValueError
from Techmodule.MusicPlayer import *
from Techmodule.FunModule import *

R = Recognizer()

while True:
    try:
        with Microphone() as source:
            print("Adjust-noise...") ; R.adjust_for_ambient_noise(source)
            print('ready to listen!') ; S1 = R.listen(source)
            print('Done!') 
            Lis = R.recognize_google(S1,language = "th-TH")
            T = DialogFlow(Lis)
            if T == "Ok":
                playSound("InYourCommand.wav")
                print("Adjust-noise...") ; R.adjust_for_ambient_noise(source)
                print("In your command!") ; S2 = R.listen(source)
                print('Done!')
                T2 = R.recognize_google(S2,language = "th-TH")
                CommandLine(DialogFlow(T2))
            elif T == "M-ON":
                print("Adjust-noise...") ; R.adjust_for_ambient_noise(source)
                print("Listen Musicname") ; S3 = R.listen(source)
                print('Done!')
                T3 = R.recognize_google(S3,language = "th-TH")
                try:
                    Mi.music.unload()
                    remove("$music_temp.mp3")
                except: pass
                finally: to_mp3(T3)
            elif T == "M-OFF":
                Mi.music.stop()
                print("Music Stopped")
                Mi.music.unload()
                remove("$music_temp.mp3")
            else:
                TextToSpeech(DialogFlow(Lis))
    except UnknownValueError:
        continue 