# 빠르고 효율적인 온보딩! - "Boarding Pass 🎫"
본 저장소는 Team Nature Republic이 개발한 **Boarding Pass** 프로젝트를 담고 있습니다. Boarding Pass 프로젝트는 **2023 KPMG Ideathon - Top 11 Finalist**로 선정되었습니다.
  
**Boarding Pass**는 **신규 입사자가 겪는 온보딩 과정의 어려움을 해결하기 위해 설계된 NLP 기반 문서 이해 챗봇 시스템**입니다.
  
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0001](https://github.com/user-attachments/assets/758942da-9535-4dbd-adf6-a4a63f4aa4f1)
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0010](https://github.com/user-attachments/assets/66b7d205-a67a-4715-af35-1f3413c005a1)
<br/>
<br/>

## 📌 프로젝트 개요
-   ⏱ **평균 온보딩 기간**: 32일\
-   💰 **1인당 평균 채용 비용**: 약 1,300만 원\
-   📉 증가하는 이직률 및 비효율적인 지식 전달\
-   😫 기존 Notion 기반 가이드는 실질적 지원이 제한적
  
**Boarding Pass**는 신규 입사자 및 협업 구성원이 사내 문서를 빠르게 이해하고, 업무 수행에 필요한 정보를 손쉽게 찾을 수 있도록 돕는 지능형 챗봇 서비스입니다.
  
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0004](https://github.com/user-attachments/assets/523acd54-5ed9-4aed-8fa7-866e4c74b7a2)
<br/>
<br/>

## 🎯 주요 기능

### 1. 💬 질의응답(Question-Answering) 챗봇
회사 정책, 업무 프로세스, 내부 정보 등에 대해 언제든지 질문할 수 있는 FAQ 형태의 챗봇입니다.
  
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0027](https://github.com/user-attachments/assets/72167a92-a0b0-47f6-9479-d7807e23dccb)

### 2. 📄 문서 요약 및 미리보기
KoBART를 활용해 기업 문서를 자동으로 요약하여 사용자가 핵심 내용을 빠르게 파악할 수 있도록 지원합니다.
  
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0028](https://github.com/user-attachments/assets/348f53aa-e05f-470d-8fbb-0ef8dd4e9e8b)

### 3. 🗂 유사 문서 추천
LDA 기반 토픽 모델링을 활용하여 관련 문서를 자동 분류하고 추천합니다.
  
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0029](https://github.com/user-attachments/assets/874402b6-490d-4d77-b503-73a6db293d4c)

### 4. 🧑‍💼 실시간 워크스페이스 캐치업
Slack 기반 메시지의 주요 이슈를 요약·공유하여 팀원들이 실시간으로 상황을 파악하고 정렬을 유지할 수 있도록 돕습니다.
  
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0030](https://github.com/user-attachments/assets/98846c04-f099-4242-b5f8-c20aa1f12d24)
<br/>
<br/>

## 🛠 기술 스택
  구분           기술
  -------------- --------------------------------------------------
  자연어 처리    KeyBERT, KoBART, GPT-3 (text-davinci-003)
  문서 분류      LDA 토픽 모델링, SVM, Naive Bayes
  백엔드         Python, Django (MTV 아키텍처)
  데이터베이스   재무제표 주석 데이터, Slack 메시지 시뮬레이션 DB
  기타           웹 크롤링, 텍스트 요약, 문서 유사도 계산
  
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0014](https://github.com/user-attachments/assets/300f238a-2f4e-4cda-a9ef-38f9b34f09a2)
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0032](https://github.com/user-attachments/assets/6ec2fb99-b7bf-4750-93f2-639d93ba2ec5)
<br/>
<br/>

## 🧪 실행 방법

### 1. 저장소 클론
```
git clone https://github.com/JeongMinIsBest/Team-Nature-Republic.git
cd Team-Nature-Republic
```

### 2. 의존성 설치
```
pip install -r requirements.txt
```

### 3. Django 서버 실행
```
python manage.py runserver
```

### 4. 브라우저에서 실행
```
http://127.0.0.1:8000/
```
<br/>
<br/>

## 🖥️ 프로타입 데모
<br/>

![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0033](https://github.com/user-attachments/assets/f8100354-53fb-427a-a886-480df4dfa85c)
<br/>
<br/>

## 📈 기대 효과
-   🚀 신규 입사자의 빠른 온보딩 및 조기 업무 자립
-   🌱 지속 가능한 ESG 기반 스마트 워킹 환경 조성
-   💪 정보 비대칭 감소 및 조직 효율성 향상

## 👥 TEAM Nature Republic 소개
**Team Nature Republic**은 자연어처리(NLP)에 대한 공통된 관심을 기반으로 자발적으로 결성된 융합 팀입니다. **문헌정보학(Library & Information Science)**과 **소프트웨어공학(컴퓨터공학)**의 전문성을 결합하여, 실제 조직에서 발생하는 온보딩 문제를 해결하고자 하였습니다.
  
![최종본  KPMG_네이처리퍼블릭_BoardingPass_page-0003](https://github.com/user-attachments/assets/5928f819-b813-4213-8094-44c2c5fb1582)
<br/>

이 프로젝트는 NLP 기술이 실제 조직 문제에 어떻게 적용될 수 있는지를 보여주며, 문서 이해, 지식 검색, 협업 워크플로우를 연결하는 사례를 제시합니다.
<br/>
<br/>
