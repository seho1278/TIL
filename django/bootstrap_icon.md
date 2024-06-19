# Django에서 npm으로 bootstrap_icon 관리하기

<br>

### 1. 명령어를 통해 bootstrap-icons npm 설치

```cmd
npm i bootstrap-icons
```
* bootstrap icon은 static 폴더를 통해 관리가 가능하므로 node.js 설치가 필수는 아니다.

<br>

### 2. node_modules / bootstrap-icons 폴더를 static 폴더에 복사해준다.

<br>

### 3. settings.py에서 static 경로를 지정해준다.
```python
# settings.py

STATIC_URL = '/static/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
```

<br>

### 4. template에 static 로드 후 css를 불러온다.
```html
template.html

{% load static %}
<link href="{% static 'bootstrap-icons/font/bootstrap-icons.css' %}" rel="stylesheet">
...

```

<br>

<br>

<br>

### [위로](#django에서-npm으로-bootstrap_icon-관리하기) / [뒤로](/README.md/#)