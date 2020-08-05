import speech_recognition as sr
def recordAudio():

    # Record the audio
    r = sr.Recognizer() # Creating a recognizer object

    # Open the microphone and start recording
    with sr.Microphone() as source:
        print('How can I help you ?')
        audio = r.listen(source)

    # Use Googles speech recognition
    try:
        data = ''
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError: # Check for unknown errors
        print('Google Speech Recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error' + e)

    return data