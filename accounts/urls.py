from django.urls import path
from .views import user_login, user_logout, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]