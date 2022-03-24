## <b> 💼 Contents </b>
-   ### <b> <a href="#0"> 📎Team introduce </a> </b>
-   ### <b> <a href="#0.5"> 📎 Introduction </a> </b>
-   ### <b> <a href="#1"> 📎 Data </a> </b>
-   ### <b> <a href="#2"> 📎 Tech stack </a> </b>
-   ### <b> <a href="#3"> 📎 Reference </a> </b>
-   ### <b> <a href="#4"> 📎 Result </a> </b>

<hr>

<h2 id="0">
    <b>💁 Team  introduce </b>
</h2>

| Name               | Roll                                               |
| -------------------- | --------------------------------------------------- |
| **권오준**<a href="https://github.com/H43RO"> | 프로젝트 리더, Front 개발 총괄</a>      |
| **고재승**<a href="https://github.com/pukuba"> | 데이터 엔지니어링, Front개발, 백엔드 개발</a>     |
| **박장호**<a href="https://github.com/Jongminfire"> | 데이터 엔지니어링, 시나리오 기획</a> |
| **정연걸**<a href="https://github.com/Jongminfire"> | 데이터 리서치</a> |
| **최슬기** <a href="https://github.com/Jongminfire"> | 데이터 엔지니어링, 백엔드 개발</a> |

<hr>

<h2 id="0.5">
    <b>💁 Introduction</b>
</h2>




### 본 프로젝트는 기존 텍스트 기반 시뮬레이터에서 유저가 주어진 선택지만 선택할 수 있는 수동적인 시스템을 개선하여, 유저에게 직접 텍스트를 입력받아 진행하는 게임 서비스입니다.

+ 유저가 직접 입력한 텍스트로 게임을 진행할 수 있음.
+ 입력된 텍스트를 BERT모델로 ‘ 문맥, 유사도, 감정, 감성’을 분류할 수 있음
+ ‘문맥, 유사도’ 모델은 이진 분류 모델로, 문장의 문맥과 유사성을 파악할 수 있음. 
+ ‘감정, 감성’ 모델은 다중 분류 모델로 7가지의 감정과 문장 긍부정을 분류할 수 있음
+ 게임 서비스에 모델을 자유롭게 추가하여 기능을 확장할 수 있음

<h2 id="1">
	<b> 🛢Data</b>
</h2>


|                dataset                |  category   |     records      |                                     source                                      |
| :-----------------------------------: | :---------: | :--------------: | :-----------------------------------------------------------------------------: |
|         감성 분석 말뭉치 2020         |    감성     |      19,531      |                  [모두의 말뭉치](https://corpus.korean.go.kr/)                  |
|                챗봇QA                 |    감성     |      11,823      |                [GitHub](https://github.com/songys/Chatbot_data)                 |
|      감정 분류를 위한 대화 음성       |    감정     |      43,991      |       [AIHub](https://aihub.or.kr/keti_data_board/language_intelligence#)       |
| 한국어 감정 정보가 포함된 연속적 대화 |    감정     |      55,600      | [AIHub](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-010) |
| 한국어 감정 정보가 포함된 단발성 대화 | 감정 / 문맥 | 38,594 /  25,472 | [AIHub](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-009) |
|           감성 대화 말뭉치            | 감정 / 문맥 | 11,823 / 118,112 |                    [AIHub](https://aihub.or.kr/aidata/7978)                     |
|         일상 대화 말뭉치 2020         |    문맥     |      17,184      |                  [모두의 말뭉치](https://corpus.korean.go.kr/)                  |
|              한국어 SNS               |    문맥     |      60,288      |                    [AIHub](https://aihub.or.kr/aidata/30718)                    |
|               KLUE-STS                | 문장 유사도 |      12,187      |          [KLUE](https://klue-benchmark.com/tasks/67/data/description)           |
|               KLUE-NLI                | 문장 유사도 |      27,998      |          [KLUE](https://klue-benchmark.com/tasks/68/data/description)           |


<div><h2 id="2">🚀 Tech Stack</h2></div>
<div align=center>
<img src="https://img.shields.io/badge/unity-000000?style=for-the-badge&logo=unity&logoColor=white">
<img src="https://img.shields.io/badge/csharp-77216F?style=for-the-badge&logo=csharp&logoColor=white">
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/googlecloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white">
<br>
<img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
<img src="https://img.shields.io/badge/jupyter-FF6F00?style=for-the-badge&logo=jupyter&logoColor=white">
<img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white">
<br>
<code>transformers</code>, <code>Logging</code>, <code>socket</code>
</div>

<hr>

<h2 id="3">🏆 Reference</h2>

[HuggingFace klue/bert-base](https://huggingface.co/klue/bert-base)\
[AI 허브](https://aihub.or.kr/)\
[모두의 말뭉치](https://corpus.korean.go.kr/)

<hr>
<h2 id="4">🏆 Result </h2>
<div align=center>
<img width="45%" src="https://user-images.githubusercontent.com/57059776/159938156-7693e82f-7191-4264-a847-e5244db0b5d6.png"><img width="45%" src="https://user-images.githubusercontent.com/57059776/159938841-075cf71d-60fc-451c-8e17-27fa4af69b0c.png">
</div>
