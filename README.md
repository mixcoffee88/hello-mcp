# Hello MCP

FastAPI를 사용한 간단한 Python 웹 애플리케이션 샘플 프로젝트입니다.

## 설치 방법

```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

## 실행 방법

```bash
uvicorn main:app --reload
```

서버가 실행되면 다음 URL에서 확인할 수 있습니다:
- API 문서: http://localhost:8000/docs
- 메인 페이지: http://localhost:8000

## API 엔드포인트

- GET `/`: 환영 메시지 반환
- GET `/items/{item_id}`: 특정 아이템 정보 반환