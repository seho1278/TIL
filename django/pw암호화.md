# pw 암호화

## make_password
- Django에서 지원해주고 있는 'make_password'는 사용자 비밀번호를 안전하게 해싱하는 함수이다.
- Django의 인증 시스템과 함께 사용되어 사용자의 비밀번호를 저장할 때 보안을 강화하는 데 사용됩니다.

<br>

- Django는 기본적으로 사용자 비밀번호를 평문으로 저장하지 않고, 해싱(hashing)된 형태로 저장하여 보안성을 높인다. 해싱은 일방향 함수로, 입력된 비밀번호를 변환하여 다시 원래의 비밀번호를 추출하는 것이 거의 불가능하다.

- 'make_password' 함수를 사용하려면 먼저 Django의 'django.contrib.auth'모듈에서 해당 함수를 가져와야 한다.
```python
from django.contrib.auth.hashers import make_password

raw_password = 'user_password'
hashed_password = make_password(raw_password)
# raw_password가 해싱되어 hashed_password변수에 저장
```
- 이렇게 해싱하여 DB에 저장하면 사용자의 비밀번호를 안전하게 보호할 수 있다.
- make_password 함수는 내부적으로 무작위의 salt를 생성하여 비밀번호를 보안하게 해싱하는데 Salt는 해시를 더욱 안전하게 만드는 데 사용되는 임의의 데이터 조각이다.

- Django의 인증 시스템은 make_password함수와 함께 해시된 비밀번호를 저장하고, 사용자가 로그인할 때 비밀번호를 동일하게 해싱하여 저장된 해시와 비교한다.

<br>

## check_password
- 'check_password'는 사용자가 입력한 비밀번호와 DB에 저장된 해시된 비밀번호를 비교하여 일치 여부를 확인하는 함수다.
- 주로 django 인증 시스템과 함께 사용되어 사용자가 로그인 시 올바른 비밀번호를 입력했는지를 검증하는데 사용된다.

- 'check_password' 함수를 사용하려면 먼저 Django의 'django.contrib.auth'모듈에서 해당 함수를 가져와야 한다.
```python
from django.contrib.auth.hashers import check_password

raw_password = 'user_input_password'
hashed_password_from_db = 'hashed_password_stored_in_database'

password_match = check_password(raw_password, hashed_password_from_db)
# 사용자가 입력한 비밀번호(raw_password)와 DB에 해시되어 저장된 비밀번호(hashed_password_from_db)를 인자로 전달

# 두 비밀번호가 일칳하면 'True'를 반환, 불일치시 'False'를 반환
```

<br>

- 이를 통해 로그인 시 사용자가 올바른 비밀번호를 입력했는지를 확인하여 인증 과정에서 보안성을 강화할 수 있다.
- 'check_password'함수는 사용자 비밀번호의 해시와 입력된 비밀번호를 비교해야하기 때문에 사용자에게 잘못된 비밀번호를 제공해도 정확한 비밀번호인지 여부를 알 수 없기 때문에 사용자 비밀번호를 안전하게 보호할 수 있다.

<br>

<br>

<br>

### [위로](#pw-암호화) / [뒤로](/README.md/#)