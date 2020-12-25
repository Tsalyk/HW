import telebot
import config
from password_gen import password_gen
from write_read_pass import write_pass, check_pass

print("bot on")

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Welcome when user turn on bot.
    """
    welcome = open('images/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, welcome)

    # keyboard
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("/gen_pass")
    item2 = telebot.types.KeyboardButton("/help")
    item3 = telebot.types.KeyboardButton("easy password")
    item4 = telebot.types.KeyboardButton("normal password")
    item5 = telebot.types.KeyboardButton("strong password")

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(
                    message.chat.id,
                    config.CONGRATULATIONS.format(message.from_user,
                                                  bot.get_me()),
                    reply_markup=markup
                )
    bot.send_message(message.chat.id, config.INSTRUCTION)


@bot.message_handler(commands=['help'])
def send_commands(message):
    """
    Send available commands.
    """
    bot.send_message(message.chat.id, config.INSTRUCTION)


@bot.message_handler(commands=['gen_pass'])
def pass_gen(message):
    """
    Send info about password generation.
    """
    bot.send_message(message.chat.id, config.PASSWORDS, parse_mode="html")


@bot.message_handler(content_types=['text'])
def get_message(message):
    """
    Processing user messages.
    """
    if message.chat.type == "private":
        if message.text == "1" or message.text == "easy password":
            password = password_gen(1)

            while check_pass(password):
                password = password_gen(1)

            bot.send_message(message.chat.id, "Your password: "
                                              f"<b>{password}</b>",
                                              parse_mode="html")
        elif message.text == "2" or message.text == "normal password":
            password = password_gen(2)

            while check_pass(password):
                password = password_gen(2)

            bot.send_message(message.chat.id, "Your password: "
                                              f"<b>{password}</b>",
                                              parse_mode="html")
        elif message.text == "3" or message.text == "strong password":
            password = password_gen(3)

            while check_pass(password):
                password = password_gen(3)

            bot.send_message(message.chat.id, "Your password: "
                                              f"<b>{password}</b>",
                                              parse_mode="html")
        else:
            bot.reply_to(message, "Sorry, I don't know what to "
                                  "say\U0001F622")
        write_pass(password)


if __name__ == '__main__':
    bot.polling()
