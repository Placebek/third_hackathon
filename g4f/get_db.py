from sqlalchemy.orm import Session
from db_pars import StoryBerries

def get_stories_for_translation(db: Session):
    """
    Получает истории, у которых еще нет перевода (title_kz и subtitle_kz пусты).
    """
    return db.query(StoryBerries).filter(
        StoryBerries.title_kz.is_(None),
        StoryBerries.subtitle_kz.is_(None),
        StoryBerries.prologue_kz.is_(None)
    ).all()
