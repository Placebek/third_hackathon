from app.tasks.celery_config import celery_app
from app.parsing.story_berries_pars import StoryBerries
from app.g4f.main_g4f import main_update_translations, main_update_text

@celery_app.task
def run_parsing_and_translation():
    """Основная задача: запускает парсер -> затем переводчик."""
    # Парсинг
    news = StoryBerries()
    news.run()
    print("Парсер завершил работу и сохранил данные в базу.")

    # Перевод
    main_update_translations()
    main_update_text()
    print("Переводчик завершил обработку пустых записей.")