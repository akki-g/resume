from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib import messages
from .models import (
    UserProfile,
    Portfolio,
    Lifting,
    Testimonial,
    Certificate,
    Education,
    LiftingGallery
)
from django.views import generic
from . forms import ContactForm

class IndexView(generic.TemplateView):
    template_name="main/index.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        portfolios = Portfolio.objects.filter(is_active=True)
        lifting = Lifting.objects.filter(is_active=True)
        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["projects"] = portfolios
        context["lifting"] = lifting
        return context

class ContactView(generic.FormView):
     template_name="main/contact.html"
     form_class=ContactForm
     success_url="/"
     def form_valid(self, form):
          form.save()
          messages.sucess(self.request, 'Thank you. We will be in touch soon.')
          return super().form_vaild(form)
    
class LiftingView(generic.ListView):
     model=Lifting
     template_name="main/lifting.html"
     paginate_by=10

     def get_queryset(self) -> QuerySet[Any]:
          return super().get_queryset().filter(is_active=True)
class LiftingDetailView(generic.DetailView):
     model=Lifting
     template_name="main/lifting-detail.html"

class PortfolioView(generic.ListView):
     model=Portfolio
     template_name="main/portfolio.html"
     paginate_by=10

     def get_queryset(self) -> QuerySet[Any]:
          return super().get_queryset().filter(is_active=True)
class PortfolioDetailView(generic.DetailView):
     model=Portfolio
     template_name="main/portfolio-detail.html"

class EducationView(generic.ListView):
     model=Education
     template_name="main/education.html"
     paginate_by=10
     
     def get_queryset(self) -> QuerySet[Any]:
          return super().get_queryset().filter(is_active=True)
     
class EducationDetailView(generic.DetailView):
     model=Education
     template_name="main/education-detail.html"

class LiftingGalleryView(generic.ListView):
     model=LiftingGallery
     template_name="main/lifting-gallery.html"