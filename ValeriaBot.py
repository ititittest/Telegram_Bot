import telebot
from telebot import types
import random

# Замените 'YOUR_TOKEN' на токен вашего бота
TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(TOKEN)

# Словарь упражнений для различных групп мышц
exercises = {
    "грудь": ["Жим лёжа", "Отжимания на брусьях", "Разводка гантелей"],
    "спина": ["Тяга верхнего блока", "Тяга гантели в наклоне", "Подтягивания"],
    "ноги": ["Приседания", "Выпады", "Жим ногами"],
    "руки": ["Сгибания на бицепс", "Французский жим", "Отжимания"],
    "плечи": ["Жим гантелей сидя", "Махи гантелями в стороны", "Армейский жим"]
}

# Стартовая команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я фитнес-бот. Выберите группу мышц, для которой хотите получить упражнение.")

# Обработка команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Используйте команды:\n"
                          "/start - начать\n"
                          "/help - помощь\n"
                          "/exercises - выбрать упражнение по группе мышц")

# Команда /exercises для выбора группы мышц
@bot.message_handler(commands=['exercises'])
def send_exercise_options(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    buttons = [types.KeyboardButton(text=muscle) for muscle in exercises.keys()]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите группу мышц:", reply_markup=markup)

# Ответ на выбор группы мышц
@bot.message_handler(func=lambda message: message.text in exercises.keys())
def send_exercise(message):
    muscle_group = message.text
    exercise = random.choice(exercises[muscle_group])
    bot.send_message(message.chat.id, f"Упражнение для {muscle_group}: {exercise}")

# Обработка любого другого сообщения
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Используйте команду /exercises, чтобы выбрать группу мышц.")

# Запуск бота
bot.polling()