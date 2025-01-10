from fastapi import FastAPI
from fastapi.openapi.models import HTTPBearer as HTTPBearerModel
from fastapi.middleware.cors import CORSMiddleware
import ssl
from app.router import route
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

origins = [
    # "http://localhost:3000",
    # "http://172.20.10.3:3000", 
    # "http://172.25.192.1:3000", 
    # "https://172.20.10.8:3000",
    # "https://localhost:3000/",
    # "https://172.25.192.1:3000/",
    # "https://192.168.193.31:3000/",
]

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('cert.pem', keyfile='key.pem')

media_folder = "media/"
app.mount("/media", StaticFiles(directory=media_folder), name="media")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

app.include_router(route)
