# **Git**

## **1. 개요**
---
* Git은 [분산 버전 관리](https://ko.wikipedia.org/wiki/%EB%B6%84%EC%82%B0_%EB%B2%84%EC%A0%84_%EA%B4%80%EB%A6%AC) 시스템으로 코드의 버전을 관리하는 도구이다.

* 2005년 [리눅스 커널](https://ko.wikipedia.org/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_%EC%BB%A4%EB%84%90)을 위한 도구로 [리누스 토르발스](https://ko.wikipedia.org/wiki/%EB%A6%AC%EB%88%84%EC%8A%A4_%ED%86%A0%EB%A5%B4%EB%B0%9C%EC%8A%A4)가 개발했다.

* 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기도 한다.

<br>

## **2. 분산버전관리시스템(DVCS)**
---
* 중앙 집중식 버전 관리 시스템은 중앙에서 버전을 관리하고 파일을 받아서 사용한다.

* [분산 버전 관리](https://ko.wikipedia.org/wiki/%EB%B6%84%EC%82%B0_%EB%B2%84%EC%A0%84_%EA%B4%80%EB%A6%AC) 시스템은 원격 저장소(remote repository)를 통하여 협업하고, <br>모든 히스토리를 클라이언트들이 공유한다.

<br>

## **3. Git 버전 관리 흐름**

> 쉽게 설명하면 다음과 같다. <br> 1. 작업을 하고 <br> 2. 변경된 파일을 모아(add) <br> 3. 버전으로 남긴다.(commit)
* 버전(Repository)은 작업(수정)한 파일상태(Working directory)를 커밋할 파일 상태 목록(Staging area로) add한 뒤 commit으로 기록한다.

* Git은 파일을  modified, staged, committed로 관리한다

  * modified : 파일이 수정된 상태 (add 명령어를 통하여 staging area로)
  * staged : 수정한 파일을 곧 커밋할 것이라고 표시한 상태 (commit 명령어로 저장소)
  * committed : 커밋이 된 상태

<br>

## **4. Git 필수 설정 정보**

* 사용자 정보 (commit author) : 커밋을 하기 위해 반드시 필요

  * git config --global user.email `"my@email.com"`
  * git config --global user.name `"username"`

<br>

* 설정 확인

  * git config -l
  * git config --global -l
  * git config user.name

  <br>

## **5. Git 명령어**

1. **init** (저장소 생성) 

> **`$ git init`**
* 특정 폴더에 git 저장소(repository)를 만들고 버전 관리

  * .git 폴더가 생성되며
  * git bash에서는 `(master)`라는 표기를 확인할 수 있다

  <br>

2. **add** (커밋 대상 기록) 
> **`$ git add <파일>`**
* working directory 상의 변경 내용을 staging area에 추가하기 위해 사용한다.

  * untracked 상태의 파일을 staged로 변경
  * modified 상태의 파일을 staged로 변경

<br>

3. **commit** (버전 기록)
> **`$ git commit -m <커밋메시지>`**
* staged 상태의 파일들을 커밋을 통해 버전으로 기록할 수 있다.

* SHA-1 해시를 사용하여 40자 길이의 체크섬을 생성하여 고유한 커밋을 표기한다.

* 커밋 메시지는 변경 사항을 나타낼 수 있도록 명확하게 작성해야 한다.


<br>

4. **log** (커밋 기록 조회)
> **`$ git log`**
* 현재 저장소에 기록된 커밋을 조회

* 다양한 옵션을 통해 로그를 조회할 수 있음
  * $ git log -1 (최근 한개)
  * $ git log --oneline (한줄로)
  * $ git log -2 --oneline (최근 두개를 한줄로)

<br>

5. **status** (파일 변경 상태)
> **`$ git status`**

* Git 저장소에 있는 파일의 상태를 확인하기 위해 활용된다.

  * 파일의 상태를 알 수 있음
    * Untracked files
    * Changes not staged for commit
    * Changes to be committed
  * Noting to commit, working tree clean

<br>

### **[명령어 정리]**
  
| **`명령어`** | **`내용`** |
| ----------- | ----------- |
| git init | 로컬 저장소 생성 |
| git add <파일명> | 특정 파일/폴더의 변경사항 추가 |
| git commit -m '<커밋메시지>' | 커밋 (버전 기록) |
| git status | 상태 확인 |
| git log | 버전 확인 |