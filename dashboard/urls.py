from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # -------------------------- AUTHENTICATION -----------------------------------

    path('signup', views.Signup.as_view(), name="signup"),
    path('signin', views.Login.as_view(), name="adminlogin"),
    path('logout', views.signout, name="logout"),

    # --------------------------Forget Password-----------------------------
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password-reset/password_reset.html',
             subject_template_name='commons/password-reset/password_reset_subject.txt',
             email_template_name='commons/password-reset/password_reset_email.html',

         ),
         name='reset_password'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    # path('home', views.Dashboard.as_view(), name="dashboard"),

    #------------------------------ DASHBOARD --------------------------------------

    path('admin', views.Dashboard.as_view(), name="dashboard"),

#-------------------------- Food Category -----------------------------------

    path('category/add', views.AddcategoryView.as_view(), name="add_category"),
    path('category', views.ListcategoryView.as_view(), name="category"),
    path('category/edit/<int:id>', views.EditcategoryView.as_view(), name="edit_category"),
    path('category/delete/<int:id>',views.delete_category,name="delete_category"),

#-------------------------- Food -----------------------------------

    path('food/add', views.AddFoodView.as_view(), name="add_food"),
    path('food', views.ListFoodView.as_view(), name="food"),
    path('food/edit/<int:id>', views.EditFoodView.as_view(), name="edit_food"),
    path('food/delete/<int:id>',views.delete_food,name="delete_food"),

#-------------------------- Users -----------------------------------

    path('users', views.ListUserView.as_view(), name="users"),



]