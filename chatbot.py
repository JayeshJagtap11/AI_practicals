
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# bot = ChatBot('Bot')
# trainer = ListTrainer(bot)
# trainer.train([
#     "Hi, can I help you",
#     "Who are you?",
#     "I am your virtual assistant. Ask me any questions...",
#     "Where do you operate?",
#     "We operate from Singapore",
#     "What payment methods do you accept?",
#     "We accept debit cards and major credit cards",
#     "I would like to speak to your customer service agent",
#     "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
#     ])
#

# while True:
#     request=input('you :')
#     if request == 'OK' or request == 'ok':
#         print('Bot: bye')
#         break
#     else:
#         response=bot.get_response(request)
#         print('Bot:', response)


from chatterbot import chatbot
from chatterbot.trainers import ListTrainer

bot=chatbot("Bot")
trainer=ListTrainer("Bot")
trainer.train([
        "Hi,can i help you",
        "Who are you ?",
])


while True:
    request=input("you:")
    if request=="OK" or request=="ok":
        print("Bot:Bye")
        break
    else:
        response=bot.get_response(request)
        print("Bot:",response)
