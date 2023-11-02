from fastapi import FastAPI
import uvicorn
from app.db.db_startup import db_startup

app = FastAPI()


@app.on_event('startup')
async def startup():
    await db_startup()


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
