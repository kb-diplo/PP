from django.contrib import admin
from .models import Profile, Project, ProjectImage, Skill, ContactMessage, Document, Education, Experience


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for Profile model.
    Provides a user-friendly interface for managing profile information.
    """
    list_display = ('name', 'title', 'email', 'location')
    search_fields = ('name', 'title', 'email')
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'bio', 'email', 'location')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url')
        }),
        ('Media', {
            'fields': ('profile_image', 'resume')
        }),
    )


class ProjectImageInline(admin.TabularInline):
    """
    Inline admin configuration for ProjectImage model.
    Allows managing project images directly within the Project admin page.
    """
    model = ProjectImage
    extra = 1  # Number of empty forms to display
    fields = ('image', 'caption', 'display_order')
    ordering = ('display_order',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    """
    Admin configuration for Project model.
    Provides comprehensive project management with filtering and search.
    """
    list_display = ('title', 'completion_date', 'is_featured', 'display_order')
    list_filter = ('is_featured', 'completion_date')
    search_fields = ('title', 'description', 'technologies')
    list_editable = ('is_featured', 'display_order')
    ordering = ('-display_order', '-completion_date')
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Challenges & Solutions', {
            'fields': ('challenges', 'solution'),
            'classes': ('collapse',)
        }),
        ('Links', {
            'fields': ('demo_url', 'source_code_url')
        }),
        ('Technical Details', {
            'fields': ('technologies', 'completion_date')
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'display_order')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Admin configuration for Skill model.
    Organized by category with proficiency management.
    """
    list_display = ('name', 'category', 'proficiency', 'display_order')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('proficiency', 'display_order')
    ordering = ('category', '-proficiency', 'name')
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'category', 'proficiency')
        }),
        ('Display Settings', {
            'fields': ('display_order',)
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """
    Admin configuration for Education model.
    """
    list_display = ('institution', 'degree', 'field_of_study', 'end_date', 'display_order')
    search_fields = ('institution', 'degree', 'field_of_study')
    list_editable = ('display_order',)
    ordering = ('-end_date',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """
    Admin configuration for Experience model.
    """
    list_display = ('company', 'title', 'end_date', 'display_order')
    search_fields = ('company', 'title')
    list_editable = ('display_order',)
    ordering = ('-end_date',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for ContactMessage model.
    Provides message management with read status tracking.
    """
    list_display = ('subject', 'name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Message Details', {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )
    
    def has_add_permission(self, request):
        """Disable adding messages through admin (they come from the contact form)"""
        return False


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """
    Admin configuration for Document model.
    Provides document management with type filtering and public visibility control.
    """
    list_display = ('title', 'document_type', 'is_public', 'display_order', 'created_at')
    list_filter = ('document_type', 'is_public', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_public', 'display_order')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('display_order', '-created_at')
    
    fieldsets = (
        ('Document Information', {
            'fields': ('title', 'description', 'document_type', 'file')
        }),
        ('Display Settings', {
            'fields': ('is_public', 'display_order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
