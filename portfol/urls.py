from django.urls import path
from .views import index_view,contact_view,blog_view,blogg_view,about_view,portfolio_view
from . import views


urlpatterns = [
    path('',views.index_view, name="index-page"),
    path('blog/',views.blog_view,  name="blog-page"),
    path('blogg/',blogg_view, name="blogg-page"),
    path('contact/',contact_view, name="cantact-page"),
    path('about/',about_view, name="about-page"),
    path('portfolio/',portfolio_view, name="portfolio-page"),
]