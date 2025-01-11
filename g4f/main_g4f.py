from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from db_config import DatabaseManager
import asyncio 


from update import update_story_translations, update_story_text

db_manager = DatabaseManager()
def get_db():
    db = db_manager.Session()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    db = next(get_db())
    asyncio.run(update_story_text(db))
    print("All stories updated successfully.")
