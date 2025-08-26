import os
import json
from django.core.management.base import BaseCommand
from django.conf import settings
from portfolio.models import Profile, Project, Skill, ContactMessage
from django.core.files import File

class Command(BaseCommand):
    help = 'Load initial data for the portfolio app'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to load initial data...'))
        
        # Load sample profile
        self.load_profile()
        
        # Load sample skills
        self.load_skills()
        
        # Load sample projects
        self.load_projects()
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data!'))
    
    def load_profile(self):
        if Profile.objects.exists():
            self.stdout.write(self.style.WARNING('Profile already exists, skipping...'))
            return
            
        profile_data = {
            'name': 'Your Name',
            'title': 'Web Developer',
            'bio': 'A passionate developer with experience in building web applications.',
            'email': 'your.email@example.com',
            'location': 'City, Country',
            'github_url': 'https://github.com/yourusername',
            'linkedin_url': 'https://linkedin.com/in/yourusername',
            'twitter_url': 'https://twitter.com/yourusername',
        }
        
        profile = Profile.objects.create(**profile_data)
        
        # To add a profile image, you would do something like:
        # profile_image_path = os.path.join(settings.BASE_DIR, 'portfolio', 'fixtures', 'profile.jpg')
        # if os.path.exists(profile_image_path):
        #     with open(profile_image_path, 'rb') as img_file:
        #         profile.profile_image.save('profile.jpg', File(img_file), save=True)
        
        self.stdout.write(self.style.SUCCESS('Created sample profile'))
    
    def load_skills(self):
        if Skill.objects.exists():
            self.stdout.write(self.style.WARNING('Skills already exist, skipping...'))
            return
            
        skills_data = [
            {'name': 'Python', 'category': 'backend', 'proficiency': 90, 'display_order': 1},
            {'name': 'Django', 'category': 'backend', 'proficiency': 85, 'display_order': 2},
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 80, 'display_order': 3},
            {'name': 'React', 'category': 'frontend', 'proficiency': 75, 'display_order': 4},
            {'name': 'HTML/CSS', 'category': 'frontend', 'proficiency': 85, 'display_order': 5},
            {'name': 'PostgreSQL', 'category': 'backend', 'proficiency': 80, 'display_order': 6},
            {'name': 'Docker', 'category': 'devops', 'proficiency': 70, 'display_order': 7},
            {'name': 'AWS', 'category': 'devops', 'proficiency': 65, 'display_order': 8},
        ]
        
        for skill_data in skills_data:
            Skill.objects.create(**skill_data)
            
        self.stdout.write(self.style.SUCCESS('Created sample skills'))
    
    def load_projects(self):
        if Project.objects.exists():
            self.stdout.write(self.style.WARNING('Projects already exist, skipping...'))
            return
            
        projects_data = [
            {
                'title': 'Portfolio Website',
                'description': 'A personal portfolio website built with Django and Tailwind CSS to showcase my projects and skills.',
                'technologies': 'Django, Python, HTML, CSS, JavaScript, Tailwind CSS',
                'completion_date': '2023-01-15',
                'is_featured': True,
                'display_order': 1,
                'demo_url': 'https://yourportfolio.com',
                'source_code_url': 'https://github.com/yourusername/portfolio',
            },
            {
                'title': 'E-commerce Platform',
                'description': 'A full-featured e-commerce platform with user authentication, product catalog, and payment integration.',
                'technologies': 'Django, Django REST Framework, React, PostgreSQL, Stripe',
                'completion_date': '2022-11-30',
                'is_featured': True,
                'display_order': 2,
                'demo_url': 'https://example-ecom.com',
                'source_code_url': 'https://github.com/yourusername/ecommerce',
            },
            {
                'title': 'Task Management App',
                'description': 'A task management application with real-time updates and team collaboration features.',
                'technologies': 'Django, Django Channels, WebSockets, JavaScript, PostgreSQL',
                'completion_date': '2022-09-15',
                'is_featured': True,
                'display_order': 3,
                'demo_url': 'https://taskapp.example.com',
                'source_code_url': 'https://github.com/yourusername/taskapp',
            },
            {
                'title': 'Recipe Sharing Platform',
                'description': 'A platform for users to share and discover recipes with advanced search and filtering.',
                'technologies': 'Django, PostgreSQL, Elasticsearch, JavaScript',
                'completion_date': '2022-07-20',
                'is_featured': False,
                'display_order': 4,
                'demo_url': 'https://recipes.example.com',
                'source_code_url': 'https://github.com/yourusername/recipes',
            },
        ]
        
        for project_data in projects_data:
            Project.objects.create(**project_data)
            
        self.stdout.write(self.style.SUCCESS('Created sample projects'))
