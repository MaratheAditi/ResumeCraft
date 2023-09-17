from django.urls import path, re_path
from . import views


app_name = "main"

urlpatterns = [
	re_path('', views.IndexView.as_view(), name="home"),
	re_path('contact/', views.ContactView.as_view(), name="contact"),
	re_path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	re_path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	re_path('blog/', views.BlogView.as_view(), name="blogs"),
	re_path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	]