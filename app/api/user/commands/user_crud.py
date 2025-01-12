from fastapi import HTTPException
from jose import JWTError
from sqlalchemy import select, update, delete, func
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
import json

from app.api.user.schemas.response import FairyTailsResponse, StatusResponse, GetUserData, CategoryStoryInfo
from app.api.user.schemas.create import FavoriteCreate, UserData
from app.context.context import validate_access_token
from app.decorators.decorators import validate_user_from_token
from app.model.model import Users, Favorites, StoryBerries, StoriesCategory, Categories, Authors, AgeCategories



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
            StoryBerries.subtitle,
            StoryBerries.text,
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




async def post_favorite_create(request: FavoriteCreate, access_token: str, db: AsyncSession):
    user = await validate_user_from_token(access_token=access_token, db=db)

    db_request = Favorites(
        user_id=user.id,
        story_berries_id=request.story_berries_id
    )

    db.add(db_request)
    await db.commit()
    await db.refresh(db_request)

    return StatusResponse(status_code=201, status_msg="Request saved successfully.")


async def delete_favorite_story(favorite_id: int, access_token: str, db: AsyncSession):
    await validate_user_from_token(access_token=access_token, db=db)
    stmt = await db.execute(
        select(Favorites).filter(Favorites.id == favorite_id.id)
    )
    order = stmt.scalars().first()
    if not order:
        raise HTTPException(status_code=404, detail="Favorite story not found")
    await db.delete(order)
    await db.commit()
    return StatusResponse(status_code=200, status_msg="Favorite story deleted successfully")



async def get_all_favorite_story(access_token: str, db: AsyncSession):
    user = await validate_user_from_token(access_token=access_token, db=db)

    try:
        result = await db.execute(
            select(Favorites)
            .options(
                select(Favorites.story_berry), 
            ).where(Favorites.user_id==user.id)

        )
        favorite_stories = result.scalars().all()

        if not favorite_stories:
            raise HTTPException(status_code=404, detail="No favorite_stories found")

        return favorite_stories

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    


async def update_user_data(user_data: UserData, access_token: str, db: AsyncSession):
    user = await validate_user_from_token(access_token=access_token, db=db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_fields = {key: value for key, value in user_data.items() if value is not None}

    if not update_fields:
        return {"status": "nothing_to_update"}

    await db.execute(
        update(Users)
        .where(Users.id == user.id)
        .values(**update_fields)
    )
    await db.commit()

    return StatusResponse(status_code=200, status_msg="Driver location updated successfully")



async def get_user_data(access_token: str, db: AsyncSession):
    user = await validate_user_from_token(access_token=access_token, db=db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    result = await db.execute(
        select(Users).where(Users.id == user.id)
    )

    user_data = result.scalar_one_or_none()
    if not user_data:
        raise HTTPException(status_code=404, detail="User data not found")
    
    print('rrrrr', user_data)
    return GetUserData(
        id=user_data.id,
        username=user_data.username,
        email=user_data.email,
        age=user_data.age,
    )
