import uvicorn

if __name__ == "__main__":
    # Замените host="0.0.0.0" на ваш IP-адрес, если хотите использовать конкретный IP
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    # uvicorn.run("main:app", host="192.168.193.31", port=8000, reload=True, ssl_certfile='cert.pem', ssl_keyfile='key.pem')
    # uvicorn.run("main:app", host="172.20.10.3", port=8000, reload=True, ssl_certfile='cert.pem', ssl_keyfile='key.pem')
    # uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn.run("main:app", host="192.168.237.182", port=8000, reload=True)

