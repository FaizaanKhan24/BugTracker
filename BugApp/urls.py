from django.urls import path
from . import views

urlpatterns = [
    path('',views.LoginPage,name='start'),
    path('register',views.Register,name='register'),
    path('logout',views.Logout,name='logout'),
    path('home',views.Home,name='home'),
    path('bug/<int:bug_id>',views.SingleBugReport,name='bug_page'),
    path('bug/<int:bug_id>/update/<int:engineer_id>/<str:status>',views.UpdateBugReport, name='update_bug')
]