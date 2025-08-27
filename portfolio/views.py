from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Profile, Project, Skill, ContactMessage, Document, Education, Experience
from .forms import ContactForm

class HomeView(TemplateView):
    """
    Home page view that displays featured projects and profile information.
    """
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['featured_projects'] = Project.objects.filter(is_featured=True).order_by('-display_order')[:3]
        context['skills'] = Skill.objects.all().order_by('category', '-proficiency')
        return context

class AboutView(TemplateView):
    """
    About page view that displays profile and skills.
    """
    template_name = 'portfolio/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        
        # Group skills by category
        skills = {}
        for skill in Skill.objects.all().order_by('category', '-proficiency'):
            category = skill.get_category_display()
            if category not in skills:
                skills[category] = []
            skills[category].append(skill)
            
        context['skills_by_category'] = skills
        context['education_history'] = Education.objects.all().order_by('-end_date', '-start_date')
        context['experience_history'] = Experience.objects.all().order_by('-end_date', '-start_date')
        return context

class ProjectListView(ListView):
    """
    View to display all projects.
    """
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    ordering = ['display_order', '-completion_date']
    # paginate_by = 6  # Removed pagination to show all projects on one page
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context

class ProjectDetailView(DetailView):
    """
    View to display a single project in detail.
    """
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context

class ContactView(FormView):
    """
    Contact form view with email sending functionality.
    """
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('portfolio:contact')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
    
    def form_valid(self, form):
        # Save the contact message to the database
        contact_message = form.save()

        # Prepare and send the email
        subject = f"New Portfolio Contact: {contact_message.subject}"
        message_body = f"""
        You received a new message from {contact_message.name} ({contact_message.email}).

        Message:
        {contact_message.message}
        """
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [admin[1] for admin in settings.ADMINS]

        try:
            send_mail(
                subject,
                message_body,
                from_email,
                recipient_list,
                fail_silently=False,
            )
            messages.success(self.request, 'Your message has been sent successfully! I will get back to you shortly.')
        except Exception as e:
            # In a real app, you'd want to log this error more robustly
            print(f"Error sending email: {e}")
            messages.error(self.request, 'Sorry, there was an error sending your message. Please try again later.')

        return super().form_valid(form)


class DocumentListView(ListView):
    """
    View to display all public documents.
    """
    model = Document
    template_name = 'portfolio/documents.html'
    context_object_name = 'documents'
    
    def get_queryset(self):
        return Document.objects.filter(is_public=True).order_by('display_order', '-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context


class DocumentDetailView(DetailView):
    """
    View to display a single document with iframe viewer.
    """
    model = Document
    template_name = 'portfolio/document_detail.html'
    context_object_name = 'document'
    
    def get_queryset(self):
        return Document.objects.filter(is_public=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
