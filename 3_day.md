# **Git(2)**

## **학습목표**
---
1. 원격저장소 활용
  * GitHub에 원격저장소를 생성하고 로컬저장소를 올려 관리하기

  * 원격저장소 활용 명령어를 이해하고 설명하기

<br>

2. 분산버전관리 시스템 이해

## 1. 원격저장소 활용
---
>원격저장소(Remote Repository) : 파일이 원격 저장소 전용 서버에서 관리되며 여러 사람이 함께 공유하기 위한 저장소이다.

<br>

### **1) 로컬저장소에 원격저장소 정보 설정하기**
* 설정 : $ git remote add origin + URL

  * 로컬저장소에는 한번만 설정하면 된다.

```bash
$ git remote add origin https://github.com/seho1278/TIL.git
# 깃 원격저장소 추가해 Origin으로    URL / github user name / 저장소 이름.git

$ git remote add origin https://github.com/seho1278/TIL.git # 한번더 입력한 경우
error: remote origin already exists. # 이미 존재한다고 나온다.
```

* 확인 : $ git remote -v

```bash
$ git remote -v
origin  https://github.com/seho1278/TIL.git (fetch)
origin  https://github.com/seho1278/TIL.git (push)
```

* 삭제 : # git remote rm 원격저장소

```bash
$ git remote rm origin
# 삭제 후 다시 $ git remote -v 하게되면 저장소가 없기 때문에 아무것도 나오지 않는다.
$ git remote -v
```
### **2) 로컬저장소의 버전을 원격저장소로 보내기**
* 보내기 : $ git push 원격저장소이름 / 브랜치 이름
```bash
$ git push origin master