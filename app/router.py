from fastapi import APIRouter

from app.api.auth.auth_user import router as auth_user_router
from app.api.user.user import router as user_router
from app.api.sort.sort import router as sort_router


route = APIRouter() 

route.include_router(auth_user_router, prefix="/auth", tags=["UserAuthentication"])
# route.include_router(auth_driver_router, prefix="/auth/driver", tags=["DriverAuthentication"])
route.include_router(user_router, prefix="/user", tags=["User"])
route.include_router(sort_router, prefix="/search", tags=["SortSearch"])
