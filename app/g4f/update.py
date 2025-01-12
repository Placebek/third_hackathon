from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from app.database.db import get_db
from app.model.model import StoryBerries

from .translate_titles import translate_to_kazakh, translate_large_text, translate_text_to_kazakh



def update_story_translations(db):
    # Получение историй, которые ещё не переведены
    stories = db.query(StoryBerries).where(
        or_(
        StoryBerries.prologue_kz.is_(None),
        StoryBerries.prologue_kz == ''
    )
    ).all()
    for story in stories:
        # Перевод данных
        print('do work with id', story.id)
        title_kz, subtitle_kz, prologue_kz = translate_to_kazakh(story.title, story.subtitle)
        
        # Обновление записи
        story.title_kz = title_kz
        story.subtitle_kz = subtitle_kz
        story.prologue_kz = prologue_kz
        print('did work with id', story.id)

        db.add(story)
        db.commit()

async def update_story_text(db):
    # Получение историй, которые ещё не переведены
    stories = db.query(StoryBerries).where(
        StoryBerries.text_kz.is_(None)
    ).all()

    for story in stories:
        print('do work with id', story.id)
        
        # Асинхронный вызов функции перевода
        text_kz = await translate_text_to_kazakh(story.text)
        
        story.text_kz = text_kz
        print('did work with id', story.id)

        db.add(story)
        db.commit()
