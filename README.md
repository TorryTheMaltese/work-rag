# 🤖 Work RAG

> 업무 문서를 기반으로 답변을 생성하는 RAG 기반 생성형 AI 챗봇

업로드한 업무 문서에서 질문과 관련된 내용을 검색하고, 검색 결과를 바탕으로 답변을 생성하는 개인 학습용 프로젝트임.

보고서 및 민원 답변 작성 지원을 주요 목적으로 하며, 생성된 답변에 참고 문서명을 함께 표시하여 원문 검토가 가능하도록 구현할 예정임.

---

## 🎯 프로젝트 목표

- 업무 문서를 활용한 생성형 AI 챗봇 구현
- 문서 검색과 생성형 AI를 결합한 RAG 구조 학습
- 보고서 및 민원 답변 초안 작성 지원
- 답변의 근거가 된 문서명 표시
- 데스크톱 및 모바일 환경 지원
- 로컬 개발 완료 후 웹서비스 배포

---

## ✨ 주요 기능

### 🔐 사용자 인증

- [ ] 접속 비밀번호 인증
- [ ] 로그인 상태 유지
- [ ] 인증되지 않은 사용자의 API 접근 제한

### 🤖 AI 챗봇

- [ ] 생성형 AI API 연동
- [ ] 사용자 질문 입력
- [ ] AI 답변 출력
- [ ] 답변 스트리밍
- [ ] 대화 기록 저장
- [ ] 새 대화 생성
- [ ] 이전 대화 조회 및 삭제

### 📄 문서 관리

- [ ] 여러 문서 파일 업로드
- [ ] 업로드 문서 목록 조회
- [ ] 업로드 진행 상태 표시
- [ ] 문서 처리 상태 표시
- [ ] 업로드 문서 삭제
- [ ] 문서 재처리
- [ ] 문서별 검색 활성화 및 비활성화

### 🔍 RAG

- [ ] 문서 텍스트 추출
- [ ] 추출된 텍스트 분할
- [ ] 문서 조각 임베딩 생성
- [ ] 임베딩 벡터 저장
- [ ] 질문과 관련된 문서 조각 검색
- [ ] 검색 결과 기반 답변 생성
- [ ] 답변에 참고 문서명 표시
- [ ] 문서에 근거가 없는 질문에 대한 응답 제한

### 📱 사용자 화면

- [ ] 반응형 웹페이지
- [ ] 모바일 화면 지원
- [ ] 채팅 화면
- [ ] 문서 관리 화면
- [ ] 대화 목록 사이드바
- [ ] 오류 및 처리 상태 안내

---

## 📑 지원 예정 문서 형식

### 1차 지원

- [ ] PDF
- [ ] DOCX
- [ ] TXT
- [ ] Markdown

### 추후 지원 검토

- [ ] XLSX
- [ ] PPTX
- [ ] HWPX
- [ ] HWP
- [ ] 이미지 파일
- [ ] 스캔 PDF OCR

---

## 🛠 기술 스택

### Frontend

- Vue 3
- TypeScript
- Vite
- Pinia
- Axios
- Vuetify 또는 Tailwind CSS

### Backend

- Python
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic

### Database

- PostgreSQL
- pgvector

### File Storage

- 로컬 개발: Docker Volume
- 배포 환경: Supabase Storage

### AI

- 생성형 AI API
- 임베딩 API
- RAG
- Vector Search

### Document Processing

- PyMuPDF
- python-docx

### Development

- Docker
- Docker Compose
- Git
- GitHub

---

## 🏗 서비스 구성

```text
사용자
  ↓
Vue 3 웹페이지
  ↓
FastAPI 백엔드
  ├─ 사용자 인증
  ├─ 생성형 AI API
  ├─ 임베딩 API
  ├─ 문서 텍스트 추출
  ├─ PostgreSQL + pgvector
  └─ 파일 저장소
```

---

## 🔄 답변 생성 과정

```text
1. 사용자의 문서 파일 업로드
2. 업로드 파일의 형식 및 크기 검증
3. 문서에서 텍스트 추출
4. 추출된 텍스트를 작은 문서 조각으로 분할
5. 각 문서 조각의 임베딩 생성
6. PostgreSQL 및 pgvector에 문서 정보 저장
7. 사용자의 질문 입력
8. 질문 임베딩 생성
9. 질문과 유사한 문서 조각 검색
10. 검색 결과와 질문을 생성형 AI API에 전달
11. 문서 내용을 바탕으로 답변 생성
12. 답변과 참고 문서명 표시
```

---

## 🚀 배포 계획

| 구분          | 기술 및 서비스                   |
| ------------- | -------------------------------- |
| Frontend      | Vue 3 · GitHub Pages             |
| Backend       | FastAPI · Render Free            |
| Database      | Supabase PostgreSQL              |
| Vector Search | Supabase pgvector                |
| File Storage  | Supabase Storage                 |
| AI            | 지원받은 생성형 AI 및 임베딩 API |

```text
Vue 3
→ GitHub Pages

FastAPI
→ Render Free

PostgreSQL + pgvector + 파일 저장소
→ Supabase Free

생성형 AI + 임베딩
→ 지원받은 API
```

로컬 환경에서 주요 기능 구현 및 테스트 후 각 서비스를 배포할 계획임.

---

## 📁 프로젝트 구조

```text
work-rag/
├── frontend/              # Vue 3 프론트엔드
├── backend/               # FastAPI 백엔드
├── docs/                  # 프로젝트 문서
├── screenshots/           # 실행 화면
├── .env.example           # 환경변수 예시
├── .gitignore
├── docker-compose.yml
└── README.md
```

---

## 🐳 로컬 개발 환경

Docker Compose를 활용하여 FastAPI, PostgreSQL 및 pgvector 실행 예정.

```bash
docker compose up --build
```

프론트엔드는 별도 개발 서버로 실행 예정.

```bash
cd frontend
npm install
npm run dev
```

백엔드 단독 실행 시 아래 명령어 사용 예정.

```bash
cd backend
uvicorn app.main:app --reload
```

---

## 🔑 환경변수

```env
DATABASE_URL=
AI_API_KEY=
AI_MODEL=
EMBEDDING_MODEL=

APP_PASSWORD_HASH=
JWT_SECRET=

SUPABASE_URL=
SUPABASE_SERVICE_KEY=
SUPABASE_STORAGE_BUCKET=
```

실제 환경변수 파일인 `.env`는 GitHub 저장소에서 제외함.

저장소에는 필요한 환경변수의 이름만 작성한 `.env.example` 파일 제공 예정.

---

## 🔒 보안 원칙

- 생성형 AI API 키의 프론트엔드 저장 금지
- 모든 AI API 요청의 FastAPI 백엔드 처리
- 서버 환경변수를 통한 비밀정보 관리
- 비밀번호 원문 저장 금지
- 비밀번호 해시값 저장
- 로그인 토큰을 활용한 사용자 인증
- 업로드 파일 형식 및 용량 제한
- 업로드 파일명의 안전한 변환
- 인증되지 않은 사용자의 문서 및 API 접근 제한
- GitHub 저장소에 `.env` 및 인증정보 업로드 금지
- 개인정보 및 비공개 자료의 무단 외부 업로드 금지

---

## 📌 답변 생성 원칙

- 업로드된 문서 내용을 우선 근거로 활용
- 문서에서 확인되지 않는 사실의 임의 생성 제한
- 근거가 부족한 경우 확인 불가 사실 안내
- 날짜와 수치는 검색된 원문 기준으로 작성
- 답변에 참고한 문서명 표시
- 문서 간 내용이 충돌하는 경우 충돌 사실 안내
- 생성 결과에 대한 사용자의 최종 검토 필요

---

## 🗺 개발 로드맵

### v0.1 · 기본 프로젝트 구성

- [x] Vue 3 프로젝트 생성
- [x] FastAPI 프로젝트 생성
- [ ] Docker Compose 구성
- [ ] 프론트엔드와 백엔드 연결
- [ ] 기본 채팅 화면 구현

### v0.2 · AI 챗봇

- [ ] 생성형 AI API 연동
- [ ] 채팅 요청 및 응답 처리
- [ ] 답변 스트리밍 구현
- [ ] 오류 처리

### v0.3 · 문서 관리

- [ ] 문서 업로드
- [ ] 문서 목록 조회
- [ ] 문서 삭제
- [ ] PDF 및 DOCX 텍스트 추출
- [ ] 문서 처리 상태 관리

### v0.4 · RAG

- [ ] 문서 분할
- [ ] 임베딩 생성
- [ ] pgvector 저장
- [ ] 유사 문서 검색
- [ ] 검색 결과 기반 답변 생성
- [ ] 답변 출처명 표시

### v0.5 · 서비스 기능

- [ ] 비밀번호 인증
- [ ] 대화 기록 저장
- [ ] 반응형 웹 구현
- [ ] 모바일 UI 개선

### v1.0 · 배포

- [ ] Vue 3 GitHub Pages 배포
- [ ] FastAPI Render 배포
- [ ] Supabase 연동
- [ ] 배포 환경 테스트
- [ ] 프로젝트 실행 화면 추가

---

## 📷 Screenshots

개발 진행 후 주요 화면 이미지 추가 예정.

### 로그인 화면

```text
추가 예정
```

### AI 채팅 화면

```text
추가 예정
```

### 문서 관리 화면

```text
추가 예정
```

### 답변 출처 표시

```text
추가 예정
```

---

## ⚠️ 참고 사항

개인 학습 및 기능 검증을 위한 토이 프로젝트임.

생성형 AI의 답변은 최종 결과물이 아닌 업무 작성 보조자료이며, 원문 확인과 사용자 검토가 필요함.

---

## 📊 프로젝트 상태

> 프로젝트 기획 및 로컬 개발 환경 구성 단계
