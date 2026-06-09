"""
Main bot file for LUST AI Assistant
Entry point for the Telegram bot
"""

import logging
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config import TELEGRAM_BOT_TOKEN, LOG_LEVEL
from handlers.start import start_command, help_command, about_command
from handlers.ai_handler import ai_command, handle_message, history_command
from handlers.admin import personality_command, personality_callback, stats_command, reset_command, ping_command

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, LOG_LEVEL)
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot"""
    
    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("ai", ai_command))
    application.add_handler(CommandHandler("personality", personality_command))
    application.add_handler(CommandHandler("history", history_command))
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CommandHandler("reset", reset_command))
    application.add_handler(CommandHandler("ping", ping_command))

    # Callback handler for personality selection
    application.add_handler(CallbackQueryHandler(personality_callback, pattern="^personality_"))

    # Message handler for regular text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    logger.info("Starting LUST AI Assistant Bot...")
    application.run_polling(allowed_updates=['message', 'callback_query'])


if __name__ == '__main__':
    main()
