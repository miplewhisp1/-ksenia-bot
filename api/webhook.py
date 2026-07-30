import json
from fastapi import FastAPI, Request, Response
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
import os
import asyncio

from bot import dp, bot

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    try:
        body = await request.json()
        update = Update(**body)
        await dp.feed_update(bot, update)
        return Response(status_code=200, content="OK")
    except Exception as e:
        print(f"Ошибка: {e}")
        return Response(status_code=200, content="OK")

@app.get("/")
async def root():
    return {"status": "Ксюша бот работает на Vercel"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)