import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Кнопка "Написать @thecreator01"
keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton("💬 Написать @thecreator01", url="https://t.me/thecreator01")
)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user = message.from_user
    name = user.full_name
    username = f"@{user.username}" if user.username else "—"
    user_id = user.id

    # Отправка уведомления владельцу
    await bot.send_message(
        OWNER_ID,
        f"📥 Новый клиент:\n👤 {name}\n🔗 {username}\n🆔 {user_id}"
    )

    # Ответ клиенту
    await message.answer(
        "Привет! Я помогу тебе быстро и надежно обменять крипту? Нажми кнопку ниже 👇🏻",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
