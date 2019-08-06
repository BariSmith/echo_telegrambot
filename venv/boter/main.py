from telegram import Bot
from telegram import Update
from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler

from boter.config import TG_TOKEN

# callback_data - це те що верне телеграм при нажатті на кожну кнопку
#через це кожен ідентифікатор повинен бути унікальним
CALLBACK_BUTTON1_1000CC = "callback_button1_1000cc"
CALLBACK_BUTTON2_600CC = "callback_button2_600cc"
CALLBACK_BUTTON3_300CC = "callback_button3_300cc"
CALLBACK_BUTTON4_150CC = "callback_button4_150cc"
CALLBACK_BUTTON5_INFO_OF_POWER = "callback_button5_info_of_power"
CALLBACK_BUTTON6_100KM = "callback_button6_100km"
CALLBACK_BUTTON7_200KM = "callback_button7_200km"
CALLBACK_BUTTON8_300KM = "callback_button8_300km"
CALLBACK_BUTTON9_400KM = "callback_button9_400km"
CALLBACK_BUTTON10_500KM = "callback_button10_500km"
CALLBACK_BUTTON11_BACK = "callback_button11_BACK"


TITLES = {
    CALLBACK_BUTTON1_1000CC: "1000cc 🏍",
    CALLBACK_BUTTON2_600CC: "600cc 🏍",
    CALLBACK_BUTTON3_300CC: "300cc 🏍",
    CALLBACK_BUTTON4_150CC: "150cc 🏍",
    CALLBACK_BUTTON5_INFO_OF_POWER: "Info of power ℹ️",
    CALLBACK_BUTTON6_100KM: "100 km 🛣",
    CALLBACK_BUTTON7_200KM: "200 km 🛣",
    CALLBACK_BUTTON8_300KM: "300 km 🛣",
    CALLBACK_BUTTON9_400KM: "400 km 🛣",
    CALLBACK_BUTTON10_500KM: "500 km 🛣",
    CALLBACK_BUTTON11_BACK: "BACK 🔙"
}

def get_base_inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_1000CC], callback_data=CALLBACK_BUTTON1_1000CC),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_600CC], callback_data=CALLBACK_BUTTON2_600CC),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_300CC], callback_data=CALLBACK_BUTTON3_300CC),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_150CC], callback_data=CALLBACK_BUTTON4_150CC),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_INFO_OF_POWER],callback_data=CALLBACK_BUTTON5_INFO_OF_POWER),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON6_100KM], callback_data=CALLBACK_BUTTON6_100KM),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON7_200KM], callback_data=CALLBACK_BUTTON7_200KM),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON8_300KM], callback_data=CALLBACK_BUTTON8_300KM),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON9_400KM], callback_data=CALLBACK_BUTTON9_400KM),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON10_500KM], callback_data=CALLBACK_BUTTON10_500KM),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON11_BACK], callback_data=CALLBACK_BUTTON11_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

#@debug_requests
def keyboadr_callback_hendler(bot: Bot, update: Update, chat_data=None, **kwargs):
    """Обробник УСІХ кнопок з УСІХ клавіатур
    """
    query = update.callback_query
    data = query.data
    now = datatime.datatime.now()

    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text




    if data == CALLBACK_BUTTON1_1000CC:
        query.edit_message_text(
            text='Please choose range what do you need.',
            reply_markup=get_keyboard(),
        )

        bot.send_message(
            chat_id=chat_id,
            text="You are choose \n callback_query.data{}". format(data),
            reply_markup=get_keyboard(),
        )

    elif data == CALLBACK_BUTTON2_600CC:
        query.edit_message_text(
            text='Please choose range what do you need.',
            reply_markup=get_keyboard(),
        )

        bot.send_message(
            chat_id=chat_id,
            text="You are choose \n callback_query.data{}".format(data),
            reply_markup=get_keyboard(),
        )

    elif data == CALLBACK_BUTTON3_300CC:
        query.edit_message_text(
            text='Please choose range what do you need.',
            reply_markup=get_keyboard(),
        )

        bot.send_message(
            chat_id=chat_id,
            text="You are choose \n callback_query.data{}".format(data),
            reply_markup=get_keyboard(),
        )

    elif data == CALLBACK_BUTTON4_150CC:
        query.edit_message_text(
            text='Please choose range what do you need.',
            reply_markup=get_keyboard(),
        )

        bot.send_message(
            chat_id=chat_id,
            text="You are choose \n callback_query.data{}".format(data),
            reply_markup=get_keyboard(),
        )
    elif data == CALLBACK_BUTTON5_INFO_OF_POWER:
        query.edit_message_text(
            text=current_text,
            parse_mode=ParseMode.MARKDOWN,
        )
        bot.send_message(
            chat_id=chat_id,
            text="125 – 150 см3, що приблизно дорівнює 6 - 15 kW (8-25 HP) потужності\n\
                    250 – 300 см3, що приблизно дорівнює 20 - 45 kW (25-60 HP) потужності\n\
                    500 – 750 см3, що приблизно дорівнює 55 – 80 kW (70-110 HP) потужності\n\
                    1000 – 1300 см3, що приблизно дорівнює 90 - 150 kW (120-200 HP) потужності\n\
                    Ці позиції закривають основні категорії напрямків розробки.\n\ncallback_query.data{}".format(data),
            reply_markup=get_base_inline_keyboard(CALLBACK_BUTTON11_BACK),
        )
    elif data == CALLBACK_BUTTON11_BACK:
        query.edit_message_text(
            text=current_text,
            reply_markup=get_base_inline_keyboard(),
        )







def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Hello! Which model do you want to change?",
        reply_markup=get_base_inline_keyboard()
    )
def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = update.message.text
    if text == BUTTON1_HELP:
        return do_help(bot=bot, update=update)
    elif text == BUTTON2_TIME:
        return do_time(bot=bot, update=update)
    else:
        reply_text = "Ваш ID = {}\n\n{}".format(chat_id, text)
        bot.send_message(
            chat_id=chat_id,
            text=reply_text,
            reply_markup=get_base_inline_keyboard(),
        )

def main():
    bot = Bot(
        token=TG_TOKEN,
    )
    updater = Updater(
        bot=bot,
    )

    start_handler = CommandHandler("start", do_start)
    message_hendler = MessageHandler(Filters.text, do_echo)
    buttons_handler = CallbackQueryHandler(callback=keyboadr_callback_hendler, pass_chat_data=True)


    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_hendler)
    updater.dispatcher.add_handler(buttons_handler)


    updater.start_polling()
    updater.idle()

if __name__ =='__main__':
    main()

