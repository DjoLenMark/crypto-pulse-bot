import logging
import aiohttp
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "7501036534:AAGDignMN0t9T3nMTcx-hMzpCeZ-NSSriWY"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

crypto_buttons = [
    ("Bitcoin", "bitcoin"), ("Ethereum", "ethereum"), ("Tether", "tether"),
    ("BNB", "binancecoin"), ("Solana", "solana"), ("XRP", "ripple"),
    ("Cardano", "cardano"), ("Dogecoin", "dogecoin"), ("Toncoin", "the-open-network"),
    ("Avalanche", "avalanche-2")
]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name, _ in crypto_buttons:
        keyboard.add(f"💰 {name}")
    await message.answer("Привет! Выбери криптовалюту ниже 👇", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text.startswith("💰"))
async def crypto_info(message: types.Message):
    name = message.text.replace("💰 ", "").strip()
    match = next((slug for label, slug in crypto_buttons if label == name), None)
    if not match:
        await message.reply("⚠️ Неизвестная криптовалюта.")
        return

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={match}&vs_currencies=usd,rub"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            if match in data:
                price_usd = data[match]['usd']
                price_rub = data[match]['rub']
                await message.reply(
                    f"💸 *{name}*\nUSD: `${price_usd}`\nRUB: `₽{price_rub}`",
                    parse_mode="Markdown"
                )

            else:
                await message.reply("❌ Не удалось получить цену.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
