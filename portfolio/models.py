from django.db import models
from django.core.validators import URLValidator
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    """
    Model to store personal information and social links.
    """
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField(help_text="A short bio about yourself")
    email = models.EmailField()
    location = models.CharField(max_length=100, blank=True)
    github_url = models.URLField(blank=True, validators=[URLValidator()])
    linkedin_url = models.URLField(blank=True, validators=[URLValidator()])
    twitter_url = models.URLField(blank=True, validators=[URLValidator()])
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    
    # Metadata
    class Meta:
        verbose_name_plural = "Profile"
    
    def __str__(self):
        return self.name

class Project(models.Model):
    """
    Model to store portfolio projects.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    demo_url = models.URLField(blank=True, validators=[URLValidator()])
    source_code_url = models.URLField(blank=True, validators=[URLValidator()])
    status = models.CharField(max_length=20, choices=[
        ('completed', 'Completed'),
        ('development', 'In Development'),
        ('planning', 'Planning Phase')
    ], default='development')
    technologies = models.CharField(max_length=200, help_text="Comma-separated list of technologies used")
    completion_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0, help_text="Higher number appears first")
    challenges = models.TextField(blank=True, help_text="Describe the challenges faced during the project.")
    solution = models.TextField(blank=True, help_text="Describe the solution implemented to overcome the challenges.")
    
    class Meta:
        ordering = ['-display_order', '-completion_date']
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        """Return technologies as a list"""
        return [tech.strip() for tech in self.technologies.split(',')]
    
    def is_completed(self):
        """Check if project is completed"""
        return self.status == 'completed'
    
    def has_live_links(self):
        """Check if project has working demo or source code links"""
        return (self.demo_url and self.demo_url != '#') or (self.source_code_url and self.source_code_url != '#')
    


class ProjectImage(models.Model):
    """
    Model to store multiple images for a project.
    """
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/screenshots/')
    caption = models.CharField(max_length=200, blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"Image for {self.project.title}"

class Skill(models.Model):
    """
    Model to store skills with proficiency levels.
    """
    SKILL_CATEGORIES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('devops', 'DevOps'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, default='other')
    proficiency = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Proficiency level from 1-100%"
    )
    display_order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['category', '-proficiency', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()}) - {self.proficiency}%"

class Education(models.Model):
    """
    Model to store education history.
    """
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"

class Experience(models.Model):
    """
    Model to store work experience.
    """
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return f"{self.title} at {self.company}"

class Document(models.Model):
    """
    Model to store documents like resume, certificates, etc.
    """
    DOCUMENT_TYPES = [
        ('resume', 'Resume/CV'),
        ('certificate', 'Certificate'),
        ('transcript', 'Transcript'),
        ('portfolio', 'Portfolio Document'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES, default='other')
    file = models.FileField(upload_to='documents/')
    is_public = models.BooleanField(default=True, help_text="Whether this document is publicly viewable")
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_file_extension(self):
        """Return the file extension"""
        return self.file.name.split('.')[-1].lower() if self.file else ''
    
    def is_pdf(self):
        """Check if the document is a PDF"""
        return self.get_file_extension() == 'pdf'
    
    def can_be_embedded(self):
        """Check if the document can be embedded in an iframe"""
        embeddable_extensions = ['pdf', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']
        return self.get_file_extension() in embeddable_extensions


class ContactMessage(models.Model):
    """
    Model to store contact form submissions.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.subject} - {self.name}"
