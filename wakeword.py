def wakeWord(text):
    Wake_Words = ['alexis'] # A list of wake words

    text = text.lower() # Converting the text to all lower case words

    # Check to see if the users command/text contains a wake word/phrase
    for phrase in Wake_Words:
        if phrase in text:
            return True

    # If the wake word isn't found in the text from the loop
    return False