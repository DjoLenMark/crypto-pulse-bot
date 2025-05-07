import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "7501036534:AAGDignMN0t9T3nMTcx-hMzpCeZ-NSSriWY"
ADMIN_ID = 228168100
CHAT_ID = -1002630037123

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

crypto_buttons = [
    ("Bitcoin", "BTC"), ("Ethereum", "ETH"), ("Tether", "USDT"),
    ("BNB", "BNB"), ("Solana", "SOL"), ("XRP", "XRP"),
    ("Cardano", "ADA"), ("Dogecoin", "DOGE"), ("Toncoin", "TON"),
    ("Avalanche", "AVAX")
]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name, code in crypto_buttons:
        keyboard.add(f"💰 {name}")
    await message.answer("Привет! Выбери криптовалюту ниже 👇", reply_markup=keyboard)

@dp.message_handler(lambda message: any(code in message.text for _, code in crypto_buttons))
async def crypto_info(message: types.Message):
    await message.reply(f"🔍 Информация по {message.text} будет здесь... (заглушка)")

@dp.message_handler(commands=['ad'])
async def receive_ad(message: types.Message):
    if message.chat.type != 'private':
        return
    await message.answer("📢 Введите текст рекламного предложения, мы передадим его администратору.")

@dp.message_handler(lambda message: message.chat.type == 'private')
async def forward_ad(message: types.Message):
    if message.text.startswith("/"):
        return
    await bot.send_message(
        ADMIN_ID,
        f"📬 Новое рекламное предложение:

От @{message.from_user.username or 'Без ника'}

{message.text}",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("✅ Разместить", callback_data=f"approve_{message.chat.id}"),
            types.InlineKeyboardButton("❌ Отклонить", callback_data="decline"),
            types.InlineKeyboardButton("✉️ Ответить", callback_data=f"reply_{message.from_user.id}")
        )
    )
    await message.answer("✅ Спасибо! Ваше предложение передано администратору.")

@dp.callback_query_handler(lambda call: call.data.startswith("approve_"))
async def approve_ad(call: types.CallbackQuery):
    chat_id = int(call.data.split("_")[1])
    await bot.send_message(CHAT_ID, f"📢 Рекламное сообщение от админа:

{call.message.text}")
    await call.answer("Размещено ✅")

@dp.callback_query_handler(lambda call: call.data.startswith("reply_"))
async def reply_to_user(call: types.CallbackQuery):
    user_id = int(call.data.split("_")[1])
    await call.message.answer(f"✏️ Напиши сообщение, которое отправить пользователю (ID: {user_id})")
    dp.register_message_handler(lambda msg: send_direct_reply(msg, user_id), content_types=types.ContentTypes.TEXT, state="*")

async def send_direct_reply(message: types.Message, user_id: int):
    await bot.send_message(user_id, f"📩 Администратор: {message.text}")
    await message.answer("✅ Сообщение отправлено.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
