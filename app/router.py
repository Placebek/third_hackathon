from fastapi import APIRouter

from app.api.auth.auth_user import router as auth_user_router
from app.api.user.user import router as user_router


route = APIRouter() 

route.include_router(auth_user_router, prefix="/auth", tags=["ClientAuthentication"])
# route.include_router(auth_driver_router, prefix="/auth/driver", tags=["DriverAuthentication"])
route.include_router(user_router, prefix="/user", tags=["Client"])
# route.include_router(driver_router, prefix="/driver", tags=["Driver"])
