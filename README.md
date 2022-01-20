# Text2Game

## 프로젝트 소개

* 머신러닝과 게임을 접목시키자!  
* 선택지를 고르는 건 따분해! -> 문장을 이해하는 인공지능 모델로 게임을 진행한다면?

## 문제제기

* 게임산업과 인공지능 기술 모두 급격히 발전하고 있으나, 정작 머신러닝이 적용된 게임은 극소수이다.
* NLP 기반 머신러닝 기술이 적용된 소수의 사례도 문장 생성형 모델이 갖는 한계점에서 벗어나지 못함.

## 해결방안
<ceter><img src="https://github.com/OverFlow37/images/blob/main/%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4%20%EA%B8%B0%EB%B0%98%20%EB%AA%A8%EB%8D%B8%20%ED%99%98%EB%A5%98%20%EB%AA%A8%ED%98%95.png?raw=true" width="450" height="400"/></center>
* 문장 생성을 포기하는 대신 BERT를 이용해 자연어 감성분석 모델을 제작하여 사용.  
* 머신러닝 모델과 게임 시스템이 서로 input과 output을 주고받으면서 상호작용.

## 예시
<ceter><img src="https://github.com/OverFlow37/images/blob/main/%EC%84%A0%ED%83%9D%EC%A7%80%20%EC%88%98%EC%A0%95%20%EC%9D%B4%EC%A0%84.jpg?raw=true" width="600" height="340"/></center>
<ceter><img src="https://github.com/OverFlow37/images/blob/main/%EC%84%A0%ED%83%9D%EC%A7%80%20%EC%88%98%EC%A0%95%20%EC%9D%B4%ED%9B%84.jpg?raw=true" width="600" height="340"/></ceter>

  
그림과 같이 기존 게임에서 객관식 선택지를 요구하는 상황에서 머신러닝 모델을 사용하여 주관식 문장을 입력받는 방식으로 변경

## 모델 파이프라인
<img src="https://github.com/OverFlow37/images/blob/main/%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4%20%EA%B8%B0%EB%B0%98%20%EB%AA%A8%EB%8D%B8%20%EC%9B%90%EB%A6%AC.png?raw=true" width="450" height="400"/>
두 개의 BERT 모델을 활용하여 플레이어의 문장을 인식한다.  
첫 번째 Check Conversation Context 모델은 문장이 맥락에 맞는 문장인지 판별한다.  
두 번째 sentiment-analysis 모델은 문장의 의미가 긍정인지, 혹은 부정인지 감성분석을 수행한다.  
이 두 가지 모델을 결합하여 플레이어가 어떤 의도로 문장을 입력했는지 판단하여 게임 시스템에 값을 전달한다.  

## 참조 코드
