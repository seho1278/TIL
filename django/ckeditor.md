# CKEditor 적용

- CKEditor란 웹 기반의 리치 텍스트 에디터로, 사용자가 웹 페이지에 복잡한 서식과 내용을 작성하고 편집할 수 있도록 도와준다
- CKEditor는 HTML편집기보다 강력한 기능을 제공하며, 사용자가 텍스트를 편집할 때 서식, 이미지 삽입, 표 작성 등 다양한 기능을 지원한다.

<br>

- CKEditor란 JavaScript 기반으로 작성되어 있으며 웹 페이지에서 쉽게 통합할 수 있고, Django 등 다양한 웹 프레임워크 및 콘텐츠 관리 시스템에서도 CKEditor를 통합하여 사용할 수 있다.

<br>

### 1. pip를 이용한 설치
- 일반적으로 pip를 통해 Django CKEditor를 설치할 수 있다.
```bash
pip install django-ckeditor==(version)
```

<br>

### 2. settings.py 파일 수정
- 설치 후 settings.py 파일의 'INSTALLED_APPS'에 'ckeditor'를 추가해준다.
```python
# settings.py

INSTALLED_APPS = [
    # 기존 앱들을 포함한 리스트
    'ckeditor',
]

# ...

# 업로드된 이미지 파일이 저장될 경로를 지정
CKEDITOR_UPLOAD_PATH = 'uploads/'
# 이미지 처리 백엔드를 지정 'pillow'라는 라이브러리 사용
CKEDITOR_IMAGE_BACKEND = "pillow"
# CKEditor의 정적 파일이 위치한 경로를 지정
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'

# CKEditor의 설정을 지정 'default'를 통해 에디터의 동작과 모양을 지정할 수 있다.
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', 'Outdent', 'Indent'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Source'],
        ],
        'height': 300,
        'width': '100%',
        'skin': 'moono-lisa',
        'removePlugins': 'exportpdf',
    }
}

```

<br>

### 3. CKEditor 정적 파일 추가
- 프로젝트 디렉토리 내에 'static' 폴더를 생성하고, 그 안에 CKEditor의 정적 파일을 저장한다.

<br>

### 4. migrate 명령 실행
- CKEditor 패키지 설치 후에 DB에 필요한 테이블을 생성하기 위해 makemigrations와 migrate 명령을 실행해야 할 수도 있다.
```bash
python manage.py makemigrations
python manage.py migrate

```

- 패키지 버전, 의존성, 변경 사항 등이 변경될 수 있으므로, 공식 문서나 GitHub 저장소 등을 참고하여 해당 버전에 맞게 진행하는 것이 좋다.

