# pygame fish-hunting-adventure 🐧🎣

## 📌프로젝트 소개
본 프로젝트는 성공회대학교 오픈소스SW개발 과목의 게임 개발 프로젝트입니다. 


## 📌스토리 소개

### Title: 물고기 사냥 대작전-★
**Information**
* 장르 : 액션, 장애물 뛰어넘기
* 형태 : 가로형
* 스테이지 : 0단계

**Game Story**
> 펭귄의 꿈은 우주로 떠나는 겁니다
펭귄이 포식자들을 피해 무사히 우주로 갈 수 있도록  도와주세요!


## Get Started
> recommend environment <br>
[![Python version](https://img.shields.io/badge/python-3.17.16-brightgreen.svg)](https://www.python.org) [![Pygame version](https://img.shields.io/badge/pygame-2.5.2-yellow.svg)](http://pygame.org)

### 1. Install python<br/>
pygame을 설치하기 위해선 python이 필요합니다. 먼저 컴퓨터에 python이 설치되어 있는지 확인하세요.
```sh
python --version
```
Python 3.17.16" 라는 메세지가 나오면 Python이 올바르게 설치된 것입니다. 오류 메시지가 뜨면 공식 문서를 참고하십시오.

### 2. Install pip<br/>
pygame을 설치하려면 pip이 필요합니다.
pip이 설치되어 있는지 확인하세요.
```sh
pip --version
```
"pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)"와 같은 메시지가 나타나면 pygame을 설치할 준비가 된 것입니다!

### 3. Install pygame
다음 명령어로 pygame을 설치하세요.
```sh
pip install pygame
```
terminal에서 위 명령어로 pygame을 설치하세요.

### 4. Run game
```sh
python main.py
```
실행했을 때 다음과 같이 뜨면 게임이 실행됩니다.
```sh
[Running] python -u "/Usr/username/dir/pygame-fish-hunting-adventure/main.py"
pygame 2.5.2 (SDL 2.28.3, Python 3.11.4)
Hello from the pygame community. https://www.pygame.org/contribute.html
2023-10-23 17:27:33.542 python[41546:6087355] TSM AdjustCapsLockLEDForKeyTransitionHandling - _ISSetPhysicalKeyboardCapsLockLED Inhibit

[Done] exited with code=0 in 5.093 seconds
```


## Screen
### Information

### Character
#### player : 펭귄
<img src="./img/player1.png" width="100" height="100">

- <span style = "background-color: rgb(255, 255, 200)">점프하는</span> 펭귄

#### stumbling block : 바다표범, 갈매기
<p align="left">
<img src="./img/seal.png" width="100" height="100">
<img src="./img/seagull.gif" width="100" height="100">
</p>

- 바닥에 <span style = "background-color: rgb(255, 255, 200)">앉아있는</span> 바다표범
- 펭귄을 향해 <span style = "background-color: rgb(255, 255, 200)">날아오는</span> 갈매기

#### score : 물고기
<img src="./img/fish.png" width="100" height="100">

- 펭귄의 점수이다.

#### key : 점프, 더블점프
<p align="left">
<img src="./img/arrow_key.png" width="45%" height="100%">
<img src="./img/spacebar_key.png" width="45%" height="100">
</p>

- 스페이스바를 사용해 점프할 수 있다.

## Team
| [Daeyeol Sung](https://github.com/Daeye0l) |[Yuna kim](kkiwiio)|[Eunchong Kim](https://github.com/rltgjqmtkdydwk) |
|:----------------------------------------------:|:---:|:-----------------------------------------------:|
|  <img src="https://github.com/Daeye0l.png">  |<img src="https://github.com/kkiwiio.png">| <img src="https://github.com/rltgjqmtkdydwk.png"> |
|                    Frontend                     |Frontend|                    Frontend                     |

#### Contact
if you have some feedback, use github review.