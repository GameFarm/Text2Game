## <b> ๐ผ Contents </b>
-   ### <b> <a href="#0"> ๐Team introduce </a> </b>
-   ### <b> <a href="#0.5"> ๐ Introduction </a> </b>
-   ### <b> <a href="#1"> ๐ Data </a> </b>
-   ### <b> <a href="#2"> ๐ Tech stack </a> </b>
-   ### <b> <a href="#3"> ๐ Reference </a> </b>
-   ### <b> <a href="#4"> ๐ Result </a> </b>

<hr>

<h2 id="0">
    <b>๐ Team  introduce </b>
</h2>

| Name               | Roll                                               |
| -------------------- | --------------------------------------------------- |
| **๊ถ์ค์ค**<a href="https://github.com/H43RO"> | ํ๋ก์ ํธ ๋ฆฌ๋, ๊ฒ์ ๊ฐ๋ฐ ์ด๊ด</a>      |
| **๊ณ ์ฌ์น**<a href="https://github.com/pukuba"> | ๋ฐ์ดํฐ ์์ง๋์ด๋ง, ๊ฒ์ ๊ฐ๋ฐ</a>     |
| **๋ฐ์ฅํธ**<a href="https://github.com/Jongminfire"> | ๋ฐ์ดํฐ ๋ฆฌ์์ฒ, ์๋๋ฆฌ์ค ๊ธฐํ</a> |
| **์ ์ฐ๊ฑธ**<a href="https://github.com/Jongminfire"> | ๋ฐ์ดํฐ ๋ฆฌ์์ฒ</a> |
| **์ต์ฌ๊ธฐ** <a href="https://github.com/Jongminfire"> | ๋ฐ์ดํฐ ์ฌ์ด์ธ์ค</a> |

<hr>

<h2 id="0.5">
    <b>๐ Introduction</b>
</h2>




### ๋ณธ ํ๋ก์ ํธ๋ ๊ธฐ์กด ํ์คํธ ๊ธฐ๋ฐ ์๋ฎฌ๋ ์ดํฐ์์ ์ ์ ๊ฐ ์ฃผ์ด์ง ์ ํ์ง๋ง ์ ํํ  ์ ์๋ ์๋์ ์ธ ์์คํ์ ๊ฐ์ ํ์ฌ, ์ ์ ์๊ฒ ์ง์  ํ์คํธ๋ฅผ ์๋ ฅ๋ฐ์ ์งํํ๋ ๊ฒ์ ์๋น์ค์๋๋ค.

+ ์ ์ ๊ฐ ์ง์  ์๋ ฅํ ํ์คํธ๋ก ๊ฒ์์ ์งํํ  ์ ์์.
+ ์๋ ฅ๋ ํ์คํธ๋ฅผ BERT๋ชจ๋ธ๋ก โ ๋ฌธ๋งฅ, ์ ์ฌ๋, ๊ฐ์ , ๊ฐ์ฑโ์ ๋ถ๋ฅํ  ์ ์์
+ โ๋ฌธ๋งฅ, ์ ์ฌ๋โ ๋ชจ๋ธ์ ์ด์ง ๋ถ๋ฅ ๋ชจ๋ธ๋ก, ๋ฌธ์ฅ์ ๋ฌธ๋งฅ๊ณผ ์ ์ฌ์ฑ์ ํ์ํ  ์ ์์. 
+ โ๊ฐ์ , ๊ฐ์ฑโ ๋ชจ๋ธ์ ๋ค์ค ๋ถ๋ฅ ๋ชจ๋ธ๋ก 7๊ฐ์ง์ ๊ฐ์ ๊ณผ ๋ฌธ์ฅ ๊ธ๋ถ์ ์ ๋ถ๋ฅํ  ์ ์์
+ ๊ฒ์ ์๋น์ค์ ๋ชจ๋ธ์ ์์ ๋กญ๊ฒ ์ถ๊ฐํ์ฌ ๊ธฐ๋ฅ์ ํ์ฅํ  ์ ์์

<h2 id="1">
	<b> ๐ขData</b>
</h2>


|                dataset                |  category   |     records      |                                     source                                      |
| :-----------------------------------: | :---------: | :--------------: | :-----------------------------------------------------------------------------: |
|         ๊ฐ์ฑ ๋ถ์ ๋ง๋ญ์น 2020         |    ๊ฐ์ฑ     |      19,531      |                  [๋ชจ๋์ ๋ง๋ญ์น](https://corpus.korean.go.kr/)                  |
|                ์ฑ๋ดQA                 |    ๊ฐ์ฑ     |      11,823      |                [GitHub](https://github.com/songys/Chatbot_data)                 |
|      ๊ฐ์  ๋ถ๋ฅ๋ฅผ ์ํ ๋ํ ์์ฑ       |    ๊ฐ์      |      43,991      |       [AIHub](https://aihub.or.kr/keti_data_board/language_intelligence#)       |
| ํ๊ตญ์ด ๊ฐ์  ์ ๋ณด๊ฐ ํฌํจ๋ ์ฐ์์  ๋ํ |    ๊ฐ์      |      55,600      | [AIHub](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-010) |
| ํ๊ตญ์ด ๊ฐ์  ์ ๋ณด๊ฐ ํฌํจ๋ ๋จ๋ฐ์ฑ ๋ํ | ๊ฐ์  / ๋ฌธ๋งฅ | 38,594 /  25,472 | [AIHub](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-009) |
|           ๊ฐ์ฑ ๋ํ ๋ง๋ญ์น            | ๊ฐ์  / ๋ฌธ๋งฅ | 11,823 / 118,112 |                    [AIHub](https://aihub.or.kr/aidata/7978)                     |
|         ์ผ์ ๋ํ ๋ง๋ญ์น 2020         |    ๋ฌธ๋งฅ     |      17,184      |                  [๋ชจ๋์ ๋ง๋ญ์น](https://corpus.korean.go.kr/)                  |
|              ํ๊ตญ์ด SNS               |    ๋ฌธ๋งฅ     |      60,288      |                    [AIHub](https://aihub.or.kr/aidata/30718)                    |
|               KLUE-STS                | ๋ฌธ์ฅ ์ ์ฌ๋ |      12,187      |          [KLUE](https://klue-benchmark.com/tasks/67/data/description)           |
|               KLUE-NLI                | ๋ฌธ์ฅ ์ ์ฌ๋ |      27,998      |          [KLUE](https://klue-benchmark.com/tasks/68/data/description)           |


<div><h2 id="2">๐ Tech Stack</h2></div>
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

<h2 id="3">๐ Reference</h2>

[HuggingFace klue/bert-base](https://huggingface.co/klue/bert-base)\
[AI ํ๋ธ](https://aihub.or.kr/)\
[๋ชจ๋์ ๋ง๋ญ์น](https://corpus.korean.go.kr/)

<hr>
<h2 id="4">๐ Result </h2>
<div align=center>
<img width="45%" src="https://user-images.githubusercontent.com/57059776/159938156-7693e82f-7191-4264-a847-e5244db0b5d6.png"><img width="45%" src="https://user-images.githubusercontent.com/57059776/159938841-075cf71d-60fc-451c-8e17-27fa4af69b0c.png">
<br>
<img width="90%" src="https://user-images.githubusercontent.com/57059776/159946979-0c8ca876-1508-4c97-b0b8-85ae1946fb8b.gif">
</div>
