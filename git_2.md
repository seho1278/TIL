# **Git(2)**

## 1. 원격저장소란

>원격저장소(Remote Repository) : 파일이 원격 저장소 전용 서버에서 관리되며 여러 사람이 함께 공유하기 위한 저장소이다.

<br>

## 2. **원격저장소 관련 명령어**

1. **원격저장소 설정**

> **`$ git remote add origin <URL>`**

* 로컬저장소에는 한번만 설정하면 된다.

<br>

2. **원격저장소 확인**

> **`$ git remote -v`**

<br>

3. **원격저장소 삭제**

> **`$ git remote rm <원격저장소>`**

<br>

4. **Push**(보내기)

> **`$ git push <원격저장소이름> <브랜치이름>`**
* 원격 저장소로 커밋을 올려 로컬저장소의 버전을 관리한다.

* 보내기전에 저장소가 있는지 확인해야한다.
```bash
$ git push origin master
remote: Repository not found. # 원격저장소가 없는 경우
fatal: repository 'https://github.com/seho1278/TIL.git/' not found
```

<br>

5. **Pull**(받기)

> **`$ git pull <원격저장소이름> <브랜치이름>`**
* 원격 저장소로 변경된 내역을 받아온다.

<br>

6. **Clone**(복제)

> **`$ git clone <원격저장소주소>`**
* 원격 저장소를 복제하여 가져온다.

<br>

### **[명령어 정리]**
  
| **`명령어`** | **`내용`** |
| ----------- | ----------- |
| git remote add <원격저장소> `<URL>` | 원격저장소 추가 |
| git remote -v | 원격저장소 정보 확인 |
| git remote rm <원격저장소> | 원격저장소 삭제 |
| git push <원격저장소> <브랜치이름> | 원격저장소에 보내기 |
| git pull <원격저장소> <브랜치이름> | 원격저장소로부터 받기 |
| git clone <원격저장소> | 원격저장소 복제 |

  <br>

## **3gitignore**

* 버전 관리와 상관없는 파일들을 관리해주는 기능이다.
  * Git 저장소에 .gitignore 파일을 생성하고 해당 내용을 관리한다.
  * 커밋된 파일은 .gitignore 되지않으니 반드시 삭제후 적용해야 한다.

  <br>

* 작성예시
  * 특정 파일 : a.txt (모든 a.txt), test/a.txt(test 폴더의 a.txt)
  * 특정 디렉토리 : /my_secret
  * 특정 확장자 : *.exe
  * 예외 처리 : !b.exe

  <br>

* 일반적으로 개발언어나 개발환경 등의 파일이 있다.
  * 개발언어 예시) 파이썬 : venv/, 자바스크립트 : node_modules/
  * 개발환경
    * 운영체제 (windows, max, linux)
    * 텍스트 에디터 / IDE (visual studio code 등)