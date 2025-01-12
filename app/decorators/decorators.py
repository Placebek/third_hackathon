from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError

from app.context.context import validate_access_token
from app.model.model import Users
from sqlalchemy import select


async def validate_user_from_token(access_token: str, db: AsyncSession) -> Users:
    try:
        user_id = (await validate_access_token(access_token=access_token)).get('user_id')

        stmt = await db.execute(
            select(Users)
            .filter(Users.id == user_id)
        )
        user = stmt.scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        return user

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
