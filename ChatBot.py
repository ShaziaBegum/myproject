import random
import time
current_time=time.ctime()

Ques_responses={
    "hi":"Hello!!",
    "how are you":"Iam Fine ,thanks!!",
    "what is your age":"Iam not a human,but i was developed in 1990s ",
    "what is your name":"People Call Me ChatBot!!!",
    "what is the time now":current_time,
    "bye":"Goodbye,Have a Great day!",
    "default":"Sorry,I didn't Understand that.Can you pleas repeat??",
}
print("Welcome to the Chatbot!! type hi to start the conversation.")
while  True:
    Questions=input()
    
    if( Questions=="quit"):
      print("Thank you for using ChatBot,See you again!!")
      break
    else:
        print(Ques_responses[Questions])

