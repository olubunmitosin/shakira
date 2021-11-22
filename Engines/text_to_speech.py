import pyttsx3

engine = pyttsx3.init(driverName=None, debug=True)


def configure_engine():
    """ RATE"""
    engine.setProperty("rate", 220)  # setting up new voice rate
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
    voices = engine.getProperty("voices")  # getting details of current voice
    engine.setProperty("voice", voices[6].id) # favourite 6
    return engine
