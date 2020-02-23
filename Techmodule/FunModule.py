import dialogflow
from os import remove , environ
from pygame import mixer as Mi
from time import sleep
from pydub import AudioSegment
from gtts import gTTS
from google.api_core.exceptions import InvalidArgument

Mi.init()
environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'Private_Key.json' #! API Access Key ID Client Access
Project_ID = 'aiz-pjeiis'
Language_code = 'th'
Session_ID = 'me'
session_client = dialogflow.SessionsClient()
session = session_client.session_path(Project_ID, Session_ID)

def playMusic(name):
    Mi.music.load(name)
    Mi.music.play()

def playSound(name):
    G = Mi.Sound(name)
    G.play()
    sleep(2)

def DialogFlow(Listen):
    text_input = dialogflow.types.TextInput(text = Listen, language_code = Language_code)
    query_input = dialogflow.types.QueryInput(text = text_input)
    try: response = session_client.detect_intent(session = session, query_input = query_input)
    except InvalidArgument: raise
    return response.query_result.fulfillment_text

def CommandLine(Text):
    if Text == "ON-01":
        print("LED on")
    elif Text == "OFF-01":
        print("LED off")
    else:
        pass

def TextToSpeech(Text):
    t = gTTS(Text,lang ="th")
    t.save("$Temp.mp3")
    sound = AudioSegment.from_mp3("$Temp.mp3")
    sound.export("$Temp.WAV", format="wav")
    remove("$Temp.mp3")
    G = Mi.Sound("$Temp.WAV")
    G.play()
    sleep(2.5)
    remove("$Temp.WAV")
