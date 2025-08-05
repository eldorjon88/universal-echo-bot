from config import TOKEN
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from handlers import handle_photo, handle_contact, handle_dice, handle_text, start, handle_main_menu, remove_keyboard


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(['start', 'boshlash'], start))


    dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))
    dispatcher.add_handler(MessageHandler(Filters.contact, handle_contact))
    dispatcher.add_handler(MessageHandler(Filters.dice, handle_dice))
    dispatcher.add_handler(MessageHandler(Filters.text("Bosh Menu"), handle_main_menu))
    dispatcher.add_handler(MessageHandler(Filters.text("Close"), handle_main_menu))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
