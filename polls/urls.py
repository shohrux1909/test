from django.urls import path
from .views import CategoryList, CategoryDetail, PostList, PostDetail, CommentList, CommentDetail, ReytingList, ReytingDetail, BannerList, BannerDetail, ContactList, ContactDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('comments/', CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path('reyttings/', ReytingList.as_view(), name='reyting_list'),
    path('reyttings/<int:pk>/', ReytingList.as_view(), name='reytings_list'),
    path('banners/', BannerList.as_view(), name='banner_list'),
    path('banners/<int:pk>/', BannerDetail.as_view(), name='banner_detail'),
    path('contacts/', ContactList.as_view(), name='contact_list'),
    path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact_detail'),
]