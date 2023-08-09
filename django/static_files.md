# Static Files

## **-INDEX-**
1. [개요](#1-개요)
2. [static files 제공](#2-가상환경-생성-및-활성화)
3. [Media files](#3-django-설치)
4. [이미지 업로드 및 제공](#4-의존성-파일-생성)

## **1. 개요**
* static files는 JS, CSS, Img 파일 등 처럼 서버 측에서 변경되지 않고 고정적으로 제공되는 정적 파일이다.

<br>

![이미지](static01.png)
* 웹 서버의 기본동작은
  * 특정 위치(URL)에 있는 자원을 요청(HTTP request) 받아서
  * 응답(HTTP request)을 처리하고 제공(serving)하는 것

* 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공해주기 때문에
* 정적 파일을 제공하기 위한 경로(URL)가 있어야 한다.

<br>

## 2. static files 제공
* 기본 경로 : app/static/

* 추가 경로 : settings.py에 STATICFILES_DIRS를 리스트 형태로 추가해 준다.
  * URL 검색시 

<br>

## collectstatic
* collectstatic은 정적파일(static files)을 수집하여 하나의 장소로 모으는 도구이다.
* 주로 개발 환경에서 정적 파일을 분산하여 관리하기 어렵거나 복잡한 상황에서 유용하게 사용된다.
* collectstatic 명령은 배포 또는 프로덕션 환경에서 사용될 때 특히 유용하며, 개발 서버에서는 개발용 static 파일 서빙 기능을 사용하는 것이 바람직 하다.

<br>

* 일반적으로, 정적 파일들은 Django 앱의 'static' 디렉토리 내부에 위치해 있으나 개발 중에는 각 앱의 static 디렉토리에 위치한 파일들을 모두 참조하기 보다는 개발 서버의 설정으로 부터 직접 정적 파일들을 제공하는 것이 편리하다
* collectstatic 명령을 사용하면 각 앱의 static 디렉토리와 프로젝트 설정에 지정된 추가적인 디렉토리로부터 모든 정적 파일들을 한 곳으로 복사되고, 이러한 파일들은 일반적으로 프로덕션 환경에서 사용하는 웹 서버의 static 디렉토리로 복사되어 서빙된다.

```python
# collectstatic 명령어
python manage.py collectstatic
```

<br>

* 명령을 실행할 경우 Django는 모든 정적 파일들을 설정된 STATIC_ROOT 경로로 복사한다.
* STATIC_ROOT는 Django 설정 파일(settings.py)에서 지정해야 한다.
```python
# settings.py

STATIC_URL = '/static/'
STATIC_ROOT = '/path/to/your/static/folder/'    # 모든 정적 파일들이 복사되는 위치
```

<br>

* 주의할 점은 명령을 실행하기 전 각 앱의 static 디렉토리와 설정 파일의 STATIC_ROOT 경로를 적절하게 설정해야 한다.

<br>

<br>

<br>

### [위로](#static-files) / [뒤로](/django/README.md)