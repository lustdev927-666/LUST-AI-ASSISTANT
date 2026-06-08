"""
Configuration module for LUST AI Assistant
Loads environment variables and sets up bot configuration
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not found in environment variables")

# OpenAI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Database Configuration
DATABASE_PATH = os.getenv('DATABASE_PATH', 'data/users.db')

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Bot Configuration
BOT_NAME = "LUST AI Assistant"
BOT_VERSION = "1.0.0"

# Personalities
PERSONALITIES = {
    'lust': {
        'name': 'Lust',
        'description': 'Équilibré - Balanced personality',
        'prefix': '⚖️'
    },
    'dark_mind': {
        'name': 'Dark Mind',
        'description': 'Mystérieux - Mysterious personality',
        'prefix': '🌑'
    },
    'anime_senpai': {
        'name': 'Anime Senpai',
        'description': 'Anime fan personality',
        'prefix': '🎌'
    },
    'hacker_mentor': {
        'name': 'Hacker Mentor',
        'description': 'Tech expert personality',
        'prefix': '🔒'
    },
    'philosopher': {
        'name': 'Philosopher',
        'description': 'Philosophical personality',
        'prefix': '🧠'
    },
    'python_dev': {
        'name': 'Python Developer',
        'description': 'Python development expert',
        'prefix': '🐍'
    },
    'professional_assistant': {
        'name': 'Professional Assistant',
        'description': 'Professional helper',
        'prefix': '💼'
    }
}

# Default personality
DEFAULT_PERSONALITY = 'lust'

# OpenAI Model Configuration
OPENAI_MODEL = 'gpt-3.5-turbo'
OPENAI_MAX_TOKENS = 2000
OPENAI_TEMPERATURE = 0.7
