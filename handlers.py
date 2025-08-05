from telegram import Update, ParseMode, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, KeyboardRemove
from telegram.ext import CallbackContext


def handle_photo(update: Update, context: CallbackContext):
    photo = update.message.photo[0]

    update.message.reply_photo(
        photo=photo,
        caption="siz <b>yuborgan</b> rasm",
        parse_mode=ParseMode.HTML
    )


def handle_contact(update: Update, context: CallbackContext):
    contact = update.message.contact

    update.message.reply_contact(
        first_name=contact.first_name,
        phone_number=contact.phone_number
    )


def handle_dice(update: Update, context: CallbackContext):
    dice = update.message.dice

    update.message.reply_dice(
        emoji=dice.emoji
    )


def handle_text(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2(
        text=">Block quotation started"
    )
    update.message.reply_html(
        text='<b>bold</b>',
    )


def handle_main_menu(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2(
        text=">Siz Bosh Menuni Tanldingiz",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Mahsulotlar")]
            ]
        )
    )


def start(update: Update, context: CallbackContext):
    bot = context.bot
    user = update.effective_user
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user  # foydalanuvchi haqida ma'lumot
    full_name = user.full_name    # bu foydalanuvchining telegramda qanday ko‘rinayotgan ismi

    context.bot.send_message(
        chat_id=user.id,
        text=f"Assalomu aleykum, {full_name}!\nMenu Tanlang:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Bosh Menu"), KeyboardButton("Buyurtma Berish")],
                [KeyboardButton("location", request_location= True), KeyboardButton("Contact", request_contact= True)],
                [KeyboardButton("Close")]

            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
    )

def remove_keyboard (update: Update, context: CallbackContext):
    update.message.replay_text(
        'Closed Keyboard',
        repley_markup=ReplyKeyboardRemove()
    )

