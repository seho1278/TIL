# search 기능 구현하기

### view Code
```python

from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    posts = Post.objects.all().order_by('-id')

    # 페이지네이션
    page = request.GET.get('page', '1')
    per_page = 10
    paginator = Paginator(posts, per_page)
    page_obj = paginator.get_page(page)

    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def search(request):
    query = request.GET.get('q')
    search_option = request.GET.get('search_option')

    if query and search_option:
        if search_option == 'title':
            filtered_posts = Post.objects.filter(title__contains=query).order_by('-id')
        elif search_option == 'author':
            filtered_posts = Post.objects.filter(user__username__icontains=query).order_by('-id')
        elif search_option == 'content':
            filtered_posts = Post.objects.filter(content__contains=query).order_by('-id')
        elif search_option == 'title_content':
            filtered_posts = Post.objects.filter(Q(title__contains=query) | Q(content__contains=query)).order_by('-id')
    else:
        filtered_posts = Post.objects.order_by('-id')

    # 페이지네이션
    page = request.GET.get('page', '1')
    per_page = 10
    paginator = Paginator(filtered_posts, per_page)
    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj,
        'query': query,
        'search_option': search_option,
    }
    return render(request, 'posts/index.html', context)
```

<br>

### url Code
```python
from django.urls import path, include

from . import views


app_name = 'posts'
urlpatterns = [    
    ...
    path('search/', views.search, name='search'),
    ...
]
```

<br>

### html Code
```html
{% comment %} search {% endcomment %}
    <div class="posts__post--searchwrap">
      <form action="{% url 'posts:search' %}" method="GET">
        <div class="posts--post--searchbox">
          <select name="search_option" id="" class="posts__post--searchlist">
            <option value="title">제목</option>
            <option value="author">작성자</option>
            <option value="content">내용</option>
            <option value="title_content">제목+내용</option>
          </select>
          <input type="text" name="q" value="{{ query|default:'' }}" placeholder="검색어를 입력하세요" class="posts__post--searchbar dark:tw-ring-blue-400 tw-ring-opacity-50">
          <button type="submit" class="posts__post--search"><i class="bi bi-search"></i></button>
        </div>
      </form>
    </div>
```