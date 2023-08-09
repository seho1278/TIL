# Pagination

## view code
```python
from django.core.paginator import Paginator
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-id')

    # 페이지네이션
    page = request.GET.get('page', '1')
    # 사용자의 요청(request)에서 'page'라는 GET 파라미터 값을 가져온다
    # GET 파라미터는 URL에 포함된 쿼리 문자열로 전달되며, 페이지 번호를 나타낸다
    # PAGE 파라미터가 존재하지 않는다면 기본값으로 '1'을 사용한다.

    per_page = 10
    # 한 페이지에 표시할 항목의 수를 지정

    paginator = Paginator(posts, per_page)
    # Paginator 객체를 생성
    # 첫 번째 인자로 페이지네이션을 적용할 전체 데이터(posts)를 전달하고,
    # 페이지에 표시할 항목의 수(per_page)를 전달

    page_obj = paginator.get_page(page)
    # Paginator 객체의 'get_page()'메서드를 사용하여 요청된 페이지의 데이터를 가져온다.
    # page 값을 인자로 전달하여 해당 페이지의 데이터를 반환 'page'값이 유효하지 않은 경우
    # 첫 번째 페이지를 반환

    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)
```
### add
* 템플릿에서 page_obj.has_previous() 및 'page_obj.has.next()' 메서드를 사용하여 이전 페이지와 다음 페이지가 있는지 확인 할 수 있다.
*  page_obj.previous_page_number() 및 page_obj.next_page_number() 메서드를 사용하여 이전 페이지와 다음 페이지의 페이지 번호를 가져올 수 있다.

## template code
```html
<div class="pagination mt-4">
      <div class="mx-auto dark:text-white">
        {% if page_obj.has_previous %}
          <a href="?page=1" class="page__btn"><i class="bi bi-chevron-double-left" style="font-size: 15px;"></i></a>
          <a href="?page={{ page_obj.previous_page_number }}" class="page__btn"><i class="bi bi-chevron-left" style="font-size: 15px; margin-right: 10px;"></i></a>
        {% endif %}
        {% for page_number in page_obj.paginator.page_range %}
          {% if page_number >= page_obj.number|add:'-5' and page_number <= page_obj.number|add:'4' %}
            {% if page_number == page_obj.number %}
              <span class="page__btn pagination__link--active">{{ page_number }}</span>
            {% else %}
              <a href="?page={{ page_number }}" class="page__btn">{{ page_number }}</a>
            {% endif %}
          {% endif %}
        {% endfor %}
        {% if page_obj.has_next %}
          <a href="?page={{ page_obj.next_page_number }}" class="page__btn"><i class="bi bi-chevron-right" style="font-size: 15px; margin-left: 10px;"></i></a>
          <a href="?page={{ page_obj.paginator.num_pages }}" class="page_btn"><i class="bi bi-chevron-double-right" style="font-size: 15px;"></i></a>
        {% endif %}
      </div>
    </div>
```

## css code
```css
/* paginator */
.page__btn {
  font-weight: bold; 
  padding: 3px;  
}

.page__btn:hover {
  color: gray;
}

.pagination__link--active{
  color: rgb(63 131 248);
  font-size: 20px;
}
```

<br>

<br>

<br>

### [위로](#pagination) / [뒤로](/django/README.md)