from django.urls import path

from .views import blog_index, blog_post

app_name = "blog"
urlpatterns = [
    path('', blog_index, name='index'),
    path('category/<category>', blog_index, name='blog_category'),
    path('post/<slug>.html', blog_post, name='blog_post')
]
