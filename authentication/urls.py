from . import views
from django.urls import path


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup_page'),
    path('login/', views.CustomLoginView.as_view(), name='login_page'),
    path('logout/decision/', views.LogoutDecisionView.as_view(), name='logout_decision'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

]