# authenticate

- Django에서 지원하고 있는 'authenticate()' 함수는 사용자 인증에 사용되는 함수중 하나다 사용자의 자격 증명을 검증하고, 유효한 사용자인지 확인하는데 사용된다.

```python
from django.contrib.auth import authenticate

user = authenticate(request, username=None, password=None)
```

request