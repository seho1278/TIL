# get_user_model

- Django의 'get_user_model'함수는 사용자 모델을 가져오는 유틸리티 함수다
- Django에서 기본적으로 제공하는 User 모델 대신 사용자가 커스텀한 사용자 모델을 가져올 때 유용하게 사용된다.
- User 모델은 username, password, email 등의 필드를 포함하고 있으며, 프로젝트의 특정 요구사항에 따라 사용자 모델을 커스터마이징해야 할 경우가 많다.

- 'get_user_model'함수는 현재 활성화된 사용자 모델 클래스를 반환한다. 이를 통해 다른 곳에서도 현재 사용 중인 사용자 모델을 참조하거나 사용자 모델과 관련된 작업을 수행할 수 있다.

```python
from django.contrib.auth import get_user_model

User = get_user_model()
```

<br>

- 커스텀 사용자 모델을 만들어 사용할 때는 AbstractBaseUser 또는 AbstractUser를 상속받아서 사용자 모델을 정의하고, AUTH_USER_MODEL 설정을 프로젝트의 설정 파일(settings.py)에 지정해야 합니다.
```python
# settings.py
AUTH_USER_MODEL = 'myapp.CustomUser'  # 앱 이름과 함께 커스텀 사용자 모델 지정
```

<br>

<br>

<br>

### [위로](#get_user_model) / [뒤로](/django/README.md)