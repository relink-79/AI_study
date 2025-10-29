<div align="center">

<h1>EmotLink</h1>

감정을 연결하는 FastAPI 기반 웹 · 모바일 프로젝트<br/>
<b>확장 가능. 빠른 성능. 모바일/웹 통합.</b>

<br/>

<a href="https://github.com/relink-79/EmotLink/stargazers"><img alt="GitHub Stars" src="https://img.shields.io/github/stars/relink-79/EmotLink?color=ffd24d" /></a>
<a href="https://github.com/relink-79/EmotLink/network/members"><img alt="GitHub Forks" src="https://img.shields.io/github/forks/relink-79/EmotLink?color=9ecbff" /></a>
<a href="https://github.com/relink-79/EmotLink/issues"><img alt="GitHub Issues" src="https://img.shields.io/github/issues/relink-79/EmotLink?color=ff9b9b" /></a>
<img alt="Last Commit" src="https://img.shields.io/github/last-commit/relink-79/EmotLink?color=9dffb0" />
<br/>
<img alt="Python" src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white" />
<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white" />
<img alt="MongoDB" src="https://img.shields.io/badge/MongoDB-7+-4EA94B?logo=mongodb&logoColor=white" />
<img alt="Redis" src="https://img.shields.io/badge/Redis-7+-DC382D?logo=redis&logoColor=white" />
<img alt="Docker" src="https://img.shields.io/badge/Docker%20Compose-ready-2496ED?logo=docker&logoColor=white" />
<img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-ff69b4" />

<br/>

<a href="#-quick-start">빠른 시작</a> ·
<a href="#-features">기능</a> ·
<a href="#%EF%B8%8F-environment">환경변수</a> ·
<a href="#-docker">Docker</a> ·
<a href="#-contributing">기여하기</a>

</div>

<details open>
<summary><strong>Table of Contents</strong></summary>

- [🌈 Highlights](#-highlights)
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Environment](#%EF%B8%8F-environment)
- [📦 Docker](#-docker)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)

</details>

## 🌈 Highlights

- ⚡ FastAPI 기반의 고성능 백엔드와 Jinja 템플릿 웹 UI
- 🧩 MongoDB + Redis 통합으로 세션/캐시 및 데이터 저장 지원
- 📱 Capacitor 연동으로 Android 앱 개발 워크플로우 제공 (`run_app.py`)
- 🐳 Docker Compose로 로컬 개발·실행을 간단히 구성
- 🛡️ 이메일 인증·로그인 등 인증 흐름 내장

## ✨ Features

- 사용자 인증: 회원가입, 로그인, 이메일 인증
- 감정 다이어리/통계, AI 연동(서버 설정에 따라)
- 반응형 템플릿 페이지(`templates/`)와 정적 파일 제공(`static/`)
- 예외 처리, 파일 사이즈 제한 등 프로덕션 유틸리티 내장

## 🚀 Quick Start

로컬 개발을 위한 두 가지 방법을 지원합니다.

1) Python 로컬 실행 (권장)

```bash
# 1) 클론 및 진입
git clone https://github.com/relink-79/EmotLink.git
cd EmotLink

# 2) 가상환경 & 의존성 설치 (Python 3.11)
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3) 환경변수(.env) 준비
cp .env.example .env  # 내용 채우기 필수

# 4) 서버 실행 (웹)
python -m uvicorn webserver.main:app --host 0.0.0.0 --port 8000
# 브라우저: http://127.0.0.1:8000
```

모바일(Android) 개발 흐름 실행:

```bash
# 사전 준비: Node.js, Android Studio, Capacitor CLI
python run_app.py  # FastAPI 서버 + Android 런치 스크립트
```

2) Docker Compose 실행

```bash
docker compose up -d --build
# 웹: http://127.0.0.1:8001 (컨테이너 내부는 8000)
```

## ⚙️ Environment

아래 항목을 참고하여 루트에 `.env` 파일을 준비하세요. 민감한 키는 공유/커밋 금지입니다.

```dotenv
# 서버/외부 API
SOLAR_API_KEY=
GOOGLE_STT_KEY=

# SMTP
MAIL_USERNAME=
MAIL_ADDRESS=
MAIL_PASSWORD=
MAIL_FROM=
MAIL_PORT=587

# (선택) Cloudflare Tunnel
# CF_TUNNEL_TOKEN=
```

Docker Compose에서 사용하는 기본 환경:

- `MONGO_URL=mongodb://mongo:27017/`
- `REDIS_HOST=redis`
- `REDIS_PORT=6379`

## 📦 Docker

`docker-compose.yml` 구성 요약:

- `app`: FastAPI 서버 (포트 매핑 `8001:8000`)
- `mongo`: MongoDB 7 (로컬 `27018` → 컨테이너 `27017`)
- `redis`: Redis 7 (로컬 `21102` → 컨테이너 `6379`)
- `cloudflared`: 선택 구성. `CF_TUNNEL_TOKEN` 필요

명령어:

```bash
docker compose up -d     # 백그라운드 실행
docker compose logs -f   # 로그 확인
docker compose down      # 종료
```

## 📁 Project Structure

```
EmotLink/
├─ webserver/           # FastAPI 엔트리포인트 및 라우터/설정
├─ templates/           # Jinja 템플릿 뷰
├─ static/              # 정적 리소스
├─ android/             # Android/Capacitor 관련 파일
├─ scripts/             # 유틸 스크립트
├─ run_app.py           # 모바일 개발 런처
├─ requirements.txt     # Python 의존성
├─ docker-compose.yml   # 로컬 통합 실행
└─ Dockerfile           # 앱 컨테이너 빌드
```

## 🤝 Contributing

이슈/PR 환영합니다! 버그 리포트, 문서 개선, 기능 제안 모두 환영합니다.

가이드라인:

- 기능/버그 단위로 브랜치 생성 후 PR 생성
- 커밋 메시지는 동사 원형 중심으로 간결하게
- 민감 정보(.env)는 절대 커밋 금지

---

문의/피드백은 GitHub Issues를 이용해주세요. 감사합니다! 🙌
