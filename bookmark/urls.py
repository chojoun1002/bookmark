from django.urls import path, re_path
from .views import BookmarkListView, BookmarkCreateView, BookmarkUpdateView, BookmarkDetailView, BookmarkDeleteView

app_name = 'bookmark'

urlpatterns = [
    # http://localgost:8000/bookmark/
    path('', BookmarkListView.as_view(), name='index'),
    path('create/', BookmarkCreateView.as_view(), name='create'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),



]
