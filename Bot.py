import time

from telebot import TeleBot
import whatsappAuto

TOKEN='1424715494:AAFLZ1DRXBTcYrPb5qHcd2SVEArbuwffqi' #(The token is worng)
bot = TeleBot(token=TOKEN)
flag1=True

@bot.message_handler(commands=['start'])
def replay_for_start(message):
    bot.send_chat_action(message.chat.id,'typing')
    bot.send_message(message.chat.id,f'Hey {message.from_user.first_name} {message.from_user.last_name} please send me phone number or '
                                     f'name of a contact you have on the whatsapp list.\n\n'
                                     f'/help - about this bot.\n'
                                     f'/stop - stop tracking after contact.')

@bot.message_handler(commands=['help'])
def replay_for_start(message):
    bot.send_chat_action(message.chat.id,'typing')
    bot.send_message(message.chat.id,'This bot can tracks after contact from your whatsapp list.\n'
                                     'You just need to send here the name or phone number and wait.\n'
                                     'The bot sends you if the contact is exits or not, if exists it sends you profile image and each 30 seconds'
                                     'you will going to get if contact online or offline.\n'
                                     'If you will want to stop tracking press on /stop .')

@bot.message_handler(commands=['stop'])
def stop_bot(message):
    global flag1
    flag1 = False

@bot.message_handler(func = lambda message : message.text != '/stop',content_types='text')
def send_activity_for_contact(message):
    global flag1
    auto = whatsappAuto.WhatsappAuto(message.text)
    string,flag2=auto.enter_chat()
    bot.send_message(message.chat.id,string)
    try:
        profile_image = open("image.png", 'rb')
        bot.send_document(message.chat.id,data=profile_image)
        profile_image.close()
    except:
        bot.send_message(message.chat.id,'Profile Picture failed to send')

    if flag2 :
        auto.mark_activity()
        while flag1:
            bot.send_message(message.chat.id,auto.copy_and_check_active())
            time.sleep(30)
        else:
            bot.send_message(message.chat.id, 'Stop Tracking')
            bot.send_message(message.chat.id, 'Press on /start')



bot.polling()

