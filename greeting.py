import random
def greeting(text):

    # Greeting inputs
    Greeting_Inputs = ['hi','hey','hello','hola','greetings','wassup','hai']

    # Greeting responses
    Greeting_responses = ['How are you?','Hello','Hey there','Hi']

    # If the users input is a greeting, then return a randomly chosen greeting response
    for word in text.split():
        if word.lower() in Greeting_Inputs:
            return random.choice(Greeting_responses) + '.'

    # If no greeting was detected then return an empty string
    return ''