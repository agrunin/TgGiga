import os  # Импортируем стандартный модуль для работы с операционной системой и переменными окружения
from dotenv import load_dotenv  # Импортируем функцию для загрузки переменных окружения из файла .env

load_dotenv()  # Загружаем переменные окружения из файла .env в текущую рабочую среду

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Получаем токен для Telegram-бота
GIGACHAT_CREDENTIALS = os.getenv("GIGACHAT_CREDENTIALS")  # Получаем учетные данные для GigaChat
