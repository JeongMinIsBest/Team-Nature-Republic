# 온보딩과 업무를 빠르게! 효율적으로! - “Boarding Pass 🎫”

**2023 KPMG Ideathon 본선 TOP 11 진출 작품**, **Team Nature Republic**의 **Bording Pass** 프로젝트 레포지터리입니다.  
**신입사원의 온보딩 문제를 해결**하기 위해 **자연어처리(NLP) 기반**의 **문서 이해 챗봇 시스템**을 개발했습니다.
<br/>
<br/>


## 📌 프로젝트 소개

- 평균 **32일**, **1,300만원**의 신입 채용 비용
- **증가하는 이직률**과 **낮은 정보 전파 효율**
- 기존 노션 기반 가이드는 **실질적인 업무 도움 부족**

**Boarding Pass**는 신입 직원 및 협업 직원들이 기업 문서를 보다 빠르게 이해하고,  
필요한 정보를 쉽게 찾을 수 있도록 도와주는 **지능형 챗봇 서비스**입니다.
<br/>
<br/>


## 🎯 핵심 기능

| 기능명 | 설명 |
|--------|------|
| 🔍 키워드 추출 | KeyBERT를 활용한 문서 핵심 키워드 자동 추출 |
| 📄 문서 요약 | KoBART를 활용한 기업 문서 요약 제공 |
| 🗂 유사 문서 추천 | LDA 토픽모델을 통해 유사한 문서 자동 분류 및 추천 |
| 🧑‍💼 워크스페이스 Catch-Up | Slack 기반 이슈 메시지 정리 및 실시간 공유 |
| 💬 질의응답 챗봇 | 회사 관련 정보에 대해 언제든지 질의 가능한 FAQ 챗봇 |
<br/>
<br/>


## 🛠 사용 기술

| 분류 | 기술 |
|------|------|
| 자연어 처리 | KeyBERT, KoBART, GPT-3 (text-davinci-003) |
| 문서 분류 | LDA Topic Modeling, SVM, Naive Bayes |
| 백엔드 | Python, Django (MTV 패턴) |
| 데이터베이스 | 재무제표 주석 데이터, Slack 메시지 가상 DB |
| 기타 | Crawling, 텍스트 요약, 문서 유사도 계산 등 |
<br/>
<br/>


## 🧪 실행 방법

1. 저장소 클론  
```
git clone https://github.com/JeongMinIsBest/Team-Nature-Republic.git
cd Team-Nature-Republic
```

2. 라이브러리 설치
```
pip install -r requirements.txt
```

3. Django 서버 실행
```
python manage.py runserver
```

4. 브라우저에서 접속
```
http://127.0.0.1:8000/
```
<br/>
<br/>

## 📈 기대 효과
- 신입 직원의 빠른 적응과 독립적 업무 수행 가능 🆗
- ESG 기반의 지속 가능한 스마트 업무 환경 조성 🌱
- 조직 내 정보 격차 해소 및 업무 효율성 증대 💪🏻
