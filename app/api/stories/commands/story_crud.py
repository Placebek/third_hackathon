from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.stories.schemas.response import FairyTailsResponse, FairyTailsForReads
from app.model.model import StoryBerries, StoriesCategory, Categories, Authors, AgeCategories



async def all_fairy_tails(skip: int, limit: int, db: AsyncSession):
    query = await db.execute(
        select(
            StoryBerries.id,
            StoryBerries.title,
            StoryBerries.subtitle,
            StoryBerries.initial_picture,
            StoryBerries.story_reads,
            AgeCategories.name.label("age_category_name"),
            Authors.name.label("author_name"),
            func.json_agg(
                func.json_build_object(
                    'id', Categories.id,
                    'name_category', Categories.name
                )
            ).label("categories")
        ).offset(skip)
        .limit(limit)
        .join(StoriesCategory, StoriesCategory.story_berries_id == StoryBerries.id)
        .join(Categories, Categories.id == StoriesCategory.category_id)
        .join(Authors, Authors.id == StoryBerries.author_id)
        .join(AgeCategories, AgeCategories.id == StoryBerries.age_category_id)
        .group_by(
            StoryBerries.id,
            StoryBerries.title,
            StoryBerries.subtitle,
            StoryBerries.initial_picture,
            StoryBerries.story_reads,
            AgeCategories.name,
            Authors.name
        )
    )

    result = query.all()

    return [
        FairyTailsResponse(
            id=row.id,
            title=row.title,
            subtitle=row.subtitle,
            initial_picture=row.initial_picture,
            story_reads=row.story_reads,
            age_category=row.age_category_name,
            author_name=row.author_name,
            category=row.categories
        )
        for row in result
    ]


async def one_fairy_tail(db: AsyncSession, fairy_tail_id: id):
    query = await db.execute(
        select(
            StoryBerries.id,
            StoryBerries.title,
            StoryBerries.subtitle,
            StoryBerries.initial_picture,
            StoryBerries.story_reads,
            AgeCategories.name.label("age_category_name"),
            Authors.name.label("author_name"),
            func.json_agg(
                func.json_build_object(
                    'id', Categories.id,
                    'name_category', Categories.name
                )
            ).label("categories")
        )
        .join(StoriesCategory, StoriesCategory.story_berries_id == StoryBerries.id)
        .join(Categories, Categories.id == StoriesCategory.category_id)
        .join(Authors, Authors.id == StoryBerries.author_id)
        .join(AgeCategories, AgeCategories.id == StoryBerries.age_category_id)
        .where(StoryBerries.id == fairy_tail_id)
        .group_by(
            StoryBerries.id,
            StoryBerries.title,
            StoryBerries.subtitle,
            StoryBerries.initial_picture,
            StoryBerries.story_reads,
            AgeCategories.name,
            Authors.name
        )
    )

    result = query.first()

    return (
        FairyTailsResponse(
            id=result.id,
            title=result.title,
            subtitle=result.subtitle,
            initial_picture=result.initial_picture,
            story_reads=result.story_reads,
            age_category=result.age_category_name,
            author_name=result.author_name,
            category=result.categories
        )
    )



async def one_fairy_tail_for_read(db: AsyncSession, fairy_tail_id: id):
    query = await db.execute(
        select(
            StoryBerries.id,
            StoryBerries.title,
            StoryBerries.title_kz,
            StoryBerries.subtitle,
            StoryBerries.subtitle_kz,
            StoryBerries.text,
            StoryBerries.text_kz,
            StoryBerries.prologue_kz,
            StoryBerries.story_reads,
            AgeCategories.name.label("age_category_name"),
            func.json_agg(
                func.json_build_object(
                    'id', Categories.id,
                    'name_category', Categories.name
                )
            ).label("categories")
        )
        .join(StoriesCategory, StoriesCategory.story_berries_id == StoryBerries.id)
        .join(Categories, Categories.id == StoriesCategory.category_id)
        .join(AgeCategories, AgeCategories.id == StoryBerries.age_category_id)
        .where(StoryBerries.id == fairy_tail_id)
        .group_by(
            StoryBerries.id,
            StoryBerries.title,
            StoryBerries.title_kz,
            StoryBerries.subtitle,
            StoryBerries.subtitle_kz,
            StoryBerries.text,
            StoryBerries.text_kz,
            StoryBerries.prologue_kz,
            StoryBerries.story_reads,
            AgeCategories.name,

        )
    )

    result = query.first()

    return (
        FairyTailsForReads(
            id=result.id,
            title=result.title,
            subtitle=result.subtitle,
            story_reads=result.story_reads,
            age_category=result.age_category_name,
            title_kz=result.title_kz,
            subtitle_kz=result.subtitle_kz,
            text=result.text,
            text_kz=result.text_kz,
            prologue_kz=result.prologue_kz,
            
        )
    )



  

