##  버전1
## FastAPI 애플리케이션을 AKS에서 실행하기 위한 기본 코드
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"message": "Hello from FastAPI on AKS!"}

# ---------------------------------------------------------------------------------------- #

# 버전2
# os.getenv()로 환경변수 읽을 수 있도록 수정
from fastapi import FastAPI
import os

app = FastAPI()

GREETING_MESSAGE = os.getenv("GREETING_MESSAGE", "Hello from FastAPI on AKS!")

@app.get("/")
async def read_root():
    return {"message": GREETING_MESSAGE}
