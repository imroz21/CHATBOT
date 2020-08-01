import webbrowser
import random




GREETING_RESPONSES = ["Hi, How can i help you?", "Hey, How can i help you?", "Hi there", "Hello", "I am glad! You are talking to me", "Hey there", "Hi, How’s it going?"]
BYE_INPUTS = ("bye","tata","bye bye","good bye","bye ")
BYE_RESPONSE = "Bye! take care.."
SAD_INPUT = ("bad", "sad", "not well", "angry", "felling bored", "bored", "bore","i am sad", "iam sad")
SAD_RESPONSE = ["Please visit this website it make you smile https://img.buzzfeed.com/buzzfeed-static/static/2019-11/25/21/campaign_images/05b93f3247fb/50-pictures-guaranteed-to-make-you-laugh-every-ti-2-9107-1574716723-0_dblbig.jpg", "Please visit this website it make you smile https://i.pinimg.com/originals/52/8a/4d/528a4d1bcabc37c0f1036e6f29955059.jpg", "Please visit this website it make you smile https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTq8Y7bcBF5xRoyJUIcPwzc2qHfRjlmSbiO9Q&usqp=CAU", "Please visit this website it make you smile https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTMLqZG5Ldym-Wi6y2AwwXl6y27gC-kU0B80Q&usqp=CAU", "Please visit this website it make you smile https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQxN6wJEQFhaUTTRrwVS3bXmACLEjrdWJeTZQ&usqp=CAU"]


def bye():
    for word in response.split():
        if word.lower() in BYE_INPUTS:
            return BYE_RESPONSE

def sad():
    """If user's input is a greeting, return a greeting response"""
    for word in response.split():
        if word.lower() in SAD_INPUT:
            return random.choice(SAD_RESPONSE)

def chat(user_response):
    global  response
    response = user_response

    if "hi" in user_response.lower() or "hello" in user_response.lower() or "hey" in user_response.lower():
        flag = False
        return random.choice(GREETING_RESPONSES)
    elif user_response.lower() in BYE_INPUTS:
        flag = False
        return bye()
    elif user_response.lower() in SAD_INPUT:
        flag = False
        return sad()
    elif "google" in user_response.lower():
        flag = False
        return web()
    else:
        flag = False
        return "Cannot understand, for more details type SERVICE NAME or HELP"


def web():
    if "google" in response.lower():
        webbrowser.open("www.google.com")
        CHAT = "Opening Google"
        return CHAT