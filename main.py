import os
import telebot

bot = telebot.Telibot("Api Key Here")

@bot.message_hendler(command=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello I'm Rash Chat Bot")

@bot.message_hendler(command=["Y-Web"])
def send_message(message):
    bot.send_message(message, "https://masterweb-000.000webhostapp.com")

bot.polling()
