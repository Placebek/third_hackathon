from fastapi import APIRouter

from app.api.auth.auth_user import router as auth_user_router
from app.api.user.user import router as user_router
from app.api.stories.story import router as story_router
from app.api.author.author import router as author_router


route = APIRouter() 

route.include_router(auth_user_router, prefix="/auth", tags=["UserAuthentication"])
# route.include_router(auth_driver_router, prefix="/auth/driver", tags=["DriverAuthentication"])
route.include_router(user_router, prefix="/user", tags=["User"])
route.include_router(story_router, prefix="/stories", tags=["Ертегілердің бір бәлелері"])
route.include_router(author_router, prefix="/author", tags=["Ертегі жазушылары"])
