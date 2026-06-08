"""
AI module for LUST AI Assistant
Handles OpenAI API interactions and response generation
"""

import openai
from config import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_MAX_TOKENS, OPENAI_TEMPERATURE, PERSONALITIES

openai.api_key = OPENAI_API_KEY


class AIAssistant:
    """Handle AI interactions and personality management"""
    
    def __init__(self):
        self.model = OPENAI_MODEL
        self.max_tokens = OPENAI_MAX_TOKENS
        self.temperature = OPENAI_TEMPERATURE
    
    def get_personality_prompt(self, personality_name):
        """Get system prompt based on personality"""
        personality = PERSONALITIES.get(personality_name, PERSONALITIES['lust'])
        
        prompts = {
            'lust': """You are Lust, a balanced and equilibrated AI assistant. 
You provide thoughtful, well-reasoned responses with a calm demeanor.
You are helpful, honest, and maintain a professional yet friendly tone.
You respond in both French and English based on user preference.""",
            
            'dark_mind': """You are Dark Mind, a mysterious and introspective AI assistant.
You explore deeper philosophical questions and complex topics.
Your responses are thought-provoking and often poetic.
You maintain an air of mystery while being helpful.""",
            
            'anime_senpai': """You are Anime Senpai, an enthusiastic anime and manga expert.
You reference anime, manga, and Japanese culture in your responses.
You are encouraging and use anime references to explain concepts.
You maintain a friendly, slightly casual tone.""",
            
            'hacker_mentor': """You are a Hacker Mentor, a cybersecurity and tech expert.
You provide technical guidance and ethical hacking advice.
You explain complex security concepts in accessible ways.
You emphasize ethical practices and legal boundaries.""",
            
            'philosopher': """You are a Philosopher, exploring ideas and wisdom.
You ask thought-provoking questions and encourage critical thinking.
You reference philosophical traditions and great thinkers.
You help users explore deeper meanings.""",
            
            'python_dev': """You are a Python Developer, a coding expert.
You help with Python programming questions and provide code examples.
You explain best practices and design patterns.
You are patient and encouraging with beginners.""",
            
            'professional_assistant': """You are a Professional Assistant.
You provide business-focused, results-oriented advice.
You maintain a formal, professional tone.
You help with productivity, planning, and professional development."""
        }
        
        return prompts.get(personality_name, prompts['lust'])
    
    async def generate_response(self, user_message, personality='lust', conversation_history=None):
        """Generate AI response based on personality"""
        
        system_prompt = self.get_personality_prompt(personality)
        
        messages = [
            {"role": "system", "content": system_prompt}
        ]
        
        # Add conversation history if provided
        if conversation_history:
            for conv in conversation_history[-5:]:  # Keep last 5 exchanges for context
                messages.append({"role": "user", "content": conv['message']})
                messages.append({"role": "assistant", "content": conv['response']})
        
        # Add current message
        messages.append({"role": "user", "content": user_message})
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message['content']
        
        except openai.error.RateLimitError:
            return "⚠️ I'm getting too many requests. Please try again in a moment."
        except openai.error.AuthenticationError:
            return "❌ Authentication error. Please check your OpenAI API key."
        except Exception as e:
            return f"❌ An error occurred: {str(e)}"
    
    def get_personality_emoji(self, personality_name):
        """Get emoji for personality"""
        personality = PERSONALITIES.get(personality_name, {})
        return personality.get('prefix', '🤖')
