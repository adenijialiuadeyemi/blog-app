from django.urls import path
from .views import (PostListView, 
                    PostDetailView,
                    BlogCreateView,
                    BlogDeleteView,
                    BlogUpdateView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>',PostDetailView.as_view(), name='post_detail'),
    path('post/new_post', BlogCreateView.as_view(), name='new_post'),
    path('post/<int:pk>/update', BlogUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='delete_post'),
]
