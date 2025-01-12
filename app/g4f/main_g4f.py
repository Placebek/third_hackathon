from app.model.db_config import DatabaseManager
import asyncio
from app.g4f.update import update_story_translations, update_story_text

db_manager = DatabaseManager()

def get_db():
    """Получает сессию базы данных."""
    db = db_manager.Session()
    try:
        yield db
    finally:
        db.close()

def main_update_translations():
    """Обновление переводов."""
    db = next(get_db())
    update_story_translations(db)
    print("Translations updated successfully.")

def main_update_text():
    """Обновление текста."""
    db = next(get_db())
    asyncio.run(update_story_text(db))
    print("Text updated successfully.")
