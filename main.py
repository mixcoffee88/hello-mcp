from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Hello MCP API",
    description="FastAPI를 사용한 샘플 API 프로젝트",
    version="1.0.0"
)

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

@app.get("/")
async def read_root():
    return {"message": "안녕하세요! Hello MCP 프로젝트에 오신 것을 환영합니다!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {
        "item": {
            "id": item_id,
            "name": f"아이템 {item_id}",
            "description": f"이것은 아이템 {item_id}의 설명입니다."
        }
    }