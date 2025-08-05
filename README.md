# 온보딩과 업무를 빠르게! 효율적으로! - “Boarding Pass 🎫”
<br/>

**2023 KPMG Ideathon 본선 TOP 11 진출 작품**, **Team Nature Republic**의 **Bording Pass** 프로젝트 레포지터리입니다.  
**신입사원의 온보딩 문제를 해결**하기 위해 **자연어처리(NLP) 기반**의 **문서 이해 챗봇 시스템**을 개발했습니다.

![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0001](https://github.com/user-attachments/assets/758942da-9535-4dbd-adf6-a4a63f4aa4f1)
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0010](https://github.com/user-attachments/assets/66b7d205-a67a-4715-af35-1f3413c005a1)
<br/>
<br/>


## 📌 프로젝트 소개
<br/>

- 평균 **32일**, **1,300만원**의 신입 채용 비용 🧑🏻‍💼
- **증가하는 이직률**과 **낮은 정보 전파 효율** ⬇️
- 기존 노션 기반 가이드는 **실질적인 업무 도움 부족** 😫

**Boarding Pass**는 신입 직원 및 협업 직원들이 기업 문서를 보다 빠르게 이해하고,  
필요한 정보를 쉽게 찾을 수 있도록 도와주는 **지능형 챗봇 서비스**입니다.

![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0004](https://github.com/user-attachments/assets/523acd54-5ed9-4aed-8fa7-866e4c74b7a2)
<br/>
<br/>


## 🎯 핵심 기능
<br/>

### 1. 💬 질의응답 챗봇 - 회사 관련 정보에 대해 언제든지 질의 가능한 FAQ 챗봇
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0027](https://github.com/user-attachments/assets/72167a92-a0b0-47f6-9479-d7807e23dccb)

### 2. 📄 문서 요약 및 미리보기 - KoBART를 활용한 기업 문서 요약 제공
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0028](https://github.com/user-attachments/assets/348f53aa-e05f-470d-8fbb-0ef8dd4e9e8b)

### 3. 🗂 유사 문서 추천 - LDA 토픽모델을 통해 유사한 문서 자동 분류 및 추천
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0029](https://github.com/user-attachments/assets/874402b6-490d-4d77-b503-73a6db293d4c)

### 4. 🧑‍💼 워크스페이스 실시간 Catch up - Slack 기반 이슈 메시지 정리 및 실시간 공유
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0030](https://github.com/user-attachments/assets/98846c04-f099-4242-b5f8-c20aa1f12d24)
<br/>
<br/>


## 🛠 사용 기술
<br/>

| 분류 | 기술 |
|------|------|
| 자연어 처리 | KeyBERT, KoBART, GPT-3 (text-davinci-003) |
| 문서 분류 | LDA Topic Modeling, SVM, Naive Bayes |
| 백엔드 | Python, Django (MTV 패턴) |
| 데이터베이스 | 재무제표 주석 데이터, Slack 메시지 가상 DB |
| 기타 | Crawling, 텍스트 요약, 문서 유사도 계산 등 |

![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0014](https://github.com/user-attachments/assets/300f238a-2f4e-4cda-a9ef-38f9b34f09a2)
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0032](https://github.com/user-attachments/assets/6ec2fb99-b7bf-4750-93f2-639d93ba2ec5)
<br/>
<br/>


## 🧪 실행 방법
<br/>

### 1. 저장소 클론  
```
git clone https://github.com/JeongMinIsBest/Team-Nature-Republic.git
cd Team-Nature-Republic
```

### 2. 라이브러리 설치
```
pip install -r requirements.txt
```

### 3. Django 서버 실행
```
python manage.py runserver
```

### 4. 브라우저에서 접속
```
http://127.0.0.1:8000/
```

![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0033](https://github.com/user-attachments/assets/f8100354-53fb-427a-a886-480df4dfa85c)
<br/>
<br/>


## 📈 기대 효과
<br/>

- 신입 직원의 빠른 적응과 독립적 업무 수행 가능 🆗
- ESG 기반의 지속 가능한 스마트 업무 환경 조성 🌱
- 조직 내 정보 격차 해소 및 업무 효율성 증대 💪🏻
<br/>
<br/>


## 👥 TEAM Nature Republic 소개
<br/>

**TEAM Nature Republic**은 **“자연”**어 처리를 위해 **“자연”**스레 모인 융합형 팀입니다.  
**문헌정보학**, **소프트웨어공학(컴퓨터공학)** 전공의 협업을 통해 **신입사원 온보딩 문제**를 **해결**하고자 했습니다.

![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0003](https://github.com/user-attachments/assets/5928f819-b813-4213-8094-44c2c5fb1582)
<br/>
<br/>

