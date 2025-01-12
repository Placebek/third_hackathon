from celery import Celery

celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',  # Подключение к Redis
    backend='redis://localhost:6379/1'  # Хранилище результатов
)

celery_app.conf.update(
    timezone='UTC',
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    beat_schedule={  # Регулярный запуск задач
        "run_parsing_and_translation": {
            "task": "tasks.run_parsing_and_translation",
            "schedule": 60.0 * 2,  # Запуск каждые 2 минут
            # "schedule": 60.0 * 60 * 24 * 7,  #  1 раз в неделю
        },
    },
)
