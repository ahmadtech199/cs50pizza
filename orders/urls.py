from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="orders_index"),
    path("login", views.login_view, name="login_view"),
    path("blog", views.blog, name="blog"),
    path("menu", views.menu, name="menu"),
    path("services", views.services, name="services"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("contactSubmitted", views.contactSubmitted, name="contactSubmitted"),
    path("logout", views.logout_view, name="logout_view"),
    path("signup", views.signup, name="signup")
]
