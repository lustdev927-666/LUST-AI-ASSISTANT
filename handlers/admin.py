"""
Admin handler for LUST AI Assistant
Manages personality switching, stats, reset, and ping
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database import Database
from config import PERSONALITIES
import logging

logger = logging.getLogger(__name__)


async def personality_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /personality command"""
    user = update.effective_user
    db = Database()
    
    current_personality = db.get_personality(user.id)
    current_name = PERSONALITIES.get(current_personality, {}).get('name', 'Inconnue')
    
    text = f"""
╔═══════════════════════════════════════╗
║       🎭 SELECTIONNER PERSONNALITE   ║
╚═══════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ **Actuelle:** {current_name}

🎯 **Choisissez la nouvelle personnalite:**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    keyboard = []
    for i, (key, personality) in enumerate(PERSONALITIES.items()):
        if i % 2 == 0:
            keyboard.append([])
        
        prefix = personality['prefix']
        name = personality['name']
        if key == current_personality:
            button_text = f"✅ {prefix} {name}"
        else:
            button_text = f"{prefix} {name}"
        
        keyboard[-1].append(InlineKeyboardButton(
            button_text,
            callback_data=f"personality_{key}"
        ))
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )


async def personality_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle personality selection callback"""
    query = update.callback_query
    user = query.from_user
    
    personality_key = query.data.split('_')[1]
    
    if personality_key not in PERSONALITIES:
        await query.answer("❌ Personnalite invalide", show_alert=True)
        return
    
    db = Database()
    db.set_personality(user.id, personality_key)
    
    personality = PERSONALITIES[personality_key]
    
    response_text = f"""
╔═══════════════════════════════════════╗
║      ✅ PERSONNALITE MISE A JOUR     ║
╚═══════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{personality['prefix']} **Nouvelle personnalite:**
{personality['name']}

📝 **Description:**
{personality['description']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Toutes les reponses prochaines utiliseront cette personnalite! ✨

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    await query.edit_message_text(
        response_text,
        parse_mode='Markdown'
    )
    
    await query.answer("✅ Succes!")
    
    logger.info(f"User {user.id} switched to {personality_key}")


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /stats command"""
    db = Database()
    stats = db.get_stats()
    
    avg_messages = round(stats['total_conversations'] / max(stats['total_users'], 1), 2) if stats['total_users'] > 0 else 0
    
    stats_text = f"""
╔═══════════════════════════════════════╗
║        📊 STATISTIQUES DU BOT         ║
╚═══════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👥 **Total d'utilisateurs**
{stats['total_users']} utilisateurs actifs

💬 **Conversations echangees**
{stats['total_conversations']} messages

🤖 **Moyenne**
{avg_messages} messages par utilisateur

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ **Etat:** Actif ✅
🎭 **Personnalites:** 7 Disponibles
🌐 **Langues:** Anglais, Francais

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Merci de soutenir LUST AI! 🙏

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    await update.message.reply_text(stats_text, parse_mode='Markdown')
    logger.info(f"Stats requested by user {update.effective_user.id}")


async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /reset command"""
    user = update.effective_user
    db = Database()
    
    db.reset_user_history(user.id)
    
    reset_text = """
╔═══════════════════════════════════════╗
║      🔄 HISTORIQUE SUPPRIME          ║
╚═══════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ **Tout votre historique de conversation**
a ete definitivement supprime.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💬 Pret a recommencer! ✨

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    await update.message.reply_text(reset_text, parse_mode='Markdown')
    
    logger.info(f"User {user.id} reset their history")


async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /ping command"""
    ping_text = """
╔═══════════════════════════════════════╗
║       🟢 PONG - JE SUIS VIVANT       ║
╚═══════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ **Le bot est actif et repond normalement.**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Connecte aux serveurs IA.
Tous les systemes fonctionnent a la perfection! 🚀

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    await update.message.reply_text(ping_text, parse_mode='Markdown')
    logger.info(f"Ping from user {update.effective_user.id}")
