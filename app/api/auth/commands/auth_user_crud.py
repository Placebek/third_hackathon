from fastapi import HTTPException
from sqlalchemy import insert, select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from app.context.context import create_access_token, hash_password, verify_password
from app.api.auth.shemas.create import UserBase, UserCreate
from app.api.auth.shemas.response import TokenResponse, TokenResponseLogin
from app.model.model import Users


async def user_register(user: UserCreate, db: AsyncSession):
    stmt = await db.execute(
        select(Users)
        .filter(
            Users.email==user.email,
        )
    )
    existing_user = stmt.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_password = hash_password(user.password)


    new_user = await db.execute(
        insert(Users)
        .values(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password,
            age=user.age
        )
        .returning(Users.id)
    )
    await db.commit()
    user_id = new_user.fetchone()[0]

    access_token, expire_time = create_access_token(data={"sub": str(user_id)})

    return TokenResponse(
        access_token=access_token,
        access_token_expire_time=expire_time
    )
    

async def user_login(user: UserBase, db: AsyncSession):
    try:
        result = await db.execute(
            select(Users).filter(
                or_(
                    Users.email == user.email_or_username,
                    Users.username == user.email_or_username
                )
            )
        )
        db_user = result.scalar_one_or_none()

        if not db_user or not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="Invalid username or password"
            )

        access_token, expire_time = create_access_token(data={"sub": str(db_user.id)})

        return TokenResponseLogin(
            access_token=access_token,
            access_token_expire_time=expire_time
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during login: {str(e)}"
        )

