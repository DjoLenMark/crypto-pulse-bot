# 🚀 Crypto Pulse Bot — Telegram бот для криптовалют

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Aiogram](https://img.shields.io/badge/Aiogram-2.25.1-orange)
![Deploy](https://img.shields.io/badge/Deployed-Render-success)
![Status](https://img.shields.io/badge/Status-Production-green)

Бот показывает **актуальные цены на криптовалюту** по данным CoinGecko API, работает в Telegram и идеально подойдёт как основа для автоматизации крипто-сообщества.

---

## ✨ Функции

- 📈 Получение цены 10 популярных криптовалют (USD и RUB)
- 🤖 Умная клавиатура с быстрым выбором монет
- 💬 Автоматическое описание и приветствие в Telegram-чате
- ⚙️ Полностью асинхронный `aiohttp` + `aiogram`
- ☁️ Автоматический деплой на Render

---

## 📸 Скриншоты

| Меню старта | Курс BTC | Приветствие |
|------------|----------|-------------|
| ![start](https://i.imgur.com/1aXsXUe.png) | ![btc](https://i.imgur.com/7ErMWWM.png) | ![hello](https://i.imgur.com/RAwOwBl.png) |

---

## ⚙️ Установка и запуск

### 🔧 Локально

```bash
git clone https://github.com/DjoLenMark/crypto-pulse-bot.git
cd crypto-pulse-bot
pip install -r requirements.txt
python main.py
```

Создай бота в BotFather и вставь свой `API_TOKEN` в `main.py`.

---

### ☁️ Деплой на Render

1. Зарегистрируйся на [Render.com](https://render.com/)
2. Создай **Web Service**
3. Заполни поля:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python main.py`
   - Instance type: Free
4. Готово!

ℹ️ [Инструкция по деплою Telegram-бота на Render](https://render.com/docs/deploy-python-telegram-bot)

---

## 🧠 Технологии

- Python 3.11
- aiogram 2.25.1
- aiohttp
- CoinGecko API
- Telegram Bot API
- Render.com

---

## 🚀 Планы на будущее

- [ ] Добавить поддержку подписки на обновления курса
- [ ] Хранить историю запросов в базе данных
- [ ] Панель администратора
- [ ] Автоматическая публикация новостей
- [ ] Интерфейс на английском

---

## 🧑‍💻 Автор

Разработано с умом и душой: [DjoLen](https://t.me/DjoLenMark)

---

## 📄 Лицензия

MIT © DjoLen
