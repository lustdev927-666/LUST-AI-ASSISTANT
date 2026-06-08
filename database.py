"""
Database module for LUST AI Assistant
Manages SQLite database for users, conversations, and settings
"""

import sqlite3
import os
import json
from datetime import datetime
from config import DATABASE_PATH


class Database:
    """Handle all database operations"""
    
    def __init__(self, db_path=DATABASE_PATH):
        self.db_path = db_path
        # Ensure data directory exists
        os.makedirs(os.path.dirname(db_path) or '.', exist_ok=True)
        self.init_db()
    
    def get_connection(self):
        """Create database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):
        """Initialize database tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_interaction TIMESTAMP,
                personality TEXT DEFAULT 'lust',
                language TEXT DEFAULT 'en'
            )
        ''')
        
        # Conversations table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                message TEXT,
                response TEXT,
                personality TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )
        ''')
        
        # Settings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL UNIQUE,
                personality TEXT DEFAULT 'lust',
                language TEXT DEFAULT 'en',
                response_type TEXT DEFAULT 'normal',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_user(self, user_id, username=None, first_name=None, last_name=None):
        """Add or update user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO users 
            (user_id, username, first_name, last_name, last_interaction)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, username, first_name, last_name, datetime.now()))
        
        # Ensure settings exist for user
        cursor.execute('''
            INSERT OR IGNORE INTO settings (user_id)
            VALUES (?)
        ''', (user_id,))
        
        conn.commit()
        conn.close()
    
    def get_user(self, user_id):
        """Get user information"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        user = cursor.fetchone()
        conn.close()
        
        return dict(user) if user else None
    
    def add_conversation(self, user_id, message, response, personality):
        """Save conversation"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO conversations 
            (user_id, message, response, personality)
            VALUES (?, ?, ?, ?)
        ''', (user_id, message, response, personality))
        
        conn.commit()
        conn.close()
    
    def get_conversation_history(self, user_id, limit=10):
        """Get user conversation history"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT message, response, personality, created_at 
            FROM conversations 
            WHERE user_id = ? 
            ORDER BY created_at DESC 
            LIMIT ?
        ''', (user_id, limit))
        
        history = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return list(reversed(history))  # Return in chronological order
    
    def set_personality(self, user_id, personality):
        """Set user personality"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE settings 
            SET personality = ?, updated_at = ? 
            WHERE user_id = ?
        ''', (personality, datetime.now(), user_id))
        
        conn.commit()
        conn.close()
    
    def get_personality(self, user_id):
        """Get user personality"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT personality FROM settings WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        conn.close()
        
        return result['personality'] if result else 'lust'
    
    def reset_user_history(self, user_id):
        """Clear user conversation history"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM conversations WHERE user_id = ?', (user_id,))
        
        conn.commit()
        conn.close()
    
    def get_stats(self):
        """Get bot statistics"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) as total_users FROM users')
        users_count = cursor.fetchone()['total_users']
        
        cursor.execute('SELECT COUNT(*) as total_conversations FROM conversations')
        conversations_count = cursor.fetchone()['total_conversations']
        
        conn.close()
        
        return {
            'total_users': users_count,
            'total_conversations': conversations_count
        }
