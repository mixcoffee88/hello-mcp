# Hello MCP

FastAPI를 사용한 간단한 Python 웹 애플리케이션 샘플 프로젝트입니다.

## 개발 환경

- Python: 3.13.2
- 운영체제: Windows 10
- 주요 패키지 버전:
  - FastAPI: 0.115.12
  - Uvicorn: 0.34.0
  - Pydantic: 2.11.1

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

## 프로젝트 구조

```
hello-mcp/
├── main.py           # FastAPI 애플리케이션 메인 파일
├── requirements.txt  # 프로젝트 의존성 목록
└── README.md        # 프로젝트 문서
```

## 주의사항

- Python 3.13 이상 버전에서 테스트되었습니다.
- 최신 버전의 FastAPI와 관련 패키지들이 필요합니다.