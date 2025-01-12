from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.author.schemas.response import GetAuthorData, GetAuthorDataAndThemFairyTails
from app.model.model import Authors, StoryBerries




async def get_author_data(id: id, db: AsyncSession):
    try:
        result = await db.execute(
            select(Authors)
            .where(Authors.id==id)

        )
        author = result.one_or_none()

        if not author:
            raise HTTPException(status_code=404, detail="Author is not found")

        return GetAuthorData(
            id=author.id,
            name=author.name,
            photo=author.photo,
            bio=author.bio
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    

async def get_author_data_and_them_fairy_tails(author_id: id, db: AsyncSession):
    try:
        result = await db.execute(
            select(
                Authors.id,
                Authors.bio,
                Authors.name,
                Authors.photo,
                func.json_agg(
                func.json_build_object(
                    'id', StoryBerries.id,
                    'title_eng', StoryBerries.title,
                    'title_kz', StoryBerries.title_kz,
                    'picture', StoryBerries.initial_picture,
                    'subtitle_eng', StoryBerries.subtitle,
                    'subtitle_lz', StoryBerries.subtitle_kz,
                    )
                ).label("fairy_tails")
            )
            .join(StoryBerries, StoryBerries.author_id == author_id)
            .where(Authors.id==author_id)
            .group_by(
                Authors.id,
                Authors.bio,
                Authors.name,
                Authors.photo,
            )

        )
        author = result.first()

        if not author:
            raise HTTPException(status_code=404, detail="Author is not found")

        return GetAuthorDataAndThemFairyTails(
            id=author.id,
            name=author.name,
            photo=author.photo,
            bio=author.bio,
            fairy_tails=author.fairy_tails
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
   


async def get_all_authors(db: AsyncSession):
    try:
        result = await db.execute(select(Authors))
        authors = result.scalars().all()
        
        if not authors:
            raise HTTPException(status_code=404, detail="Author is not found")
        return [
            GetAuthorData(
                id=author.id,
                name=author.name,
                photo=author.photo,
                bio=author.bio,
            )
            for author in authors
        ]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
   