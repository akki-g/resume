from django.urls import path
from . import views

app_name='main'

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('lifting/', views.LiftingView.as_view(), name="liftings"),
	path('lifting/<slug:slug>', views.LiftingDetailView.as_view(), name="lifting"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
    path('education/', views.EducationView.as_view(), name="educations"),
    path('education/<slug:slug>', views.EducationDetailView.as_view(), name="education"),
    path('lifting-gallery/', views.LiftingGalleryView.as_view(), name="galleries")
]