"""
Management command to load portfolio data from fixtures.
This command provides an easy way to populate the database with initial data.

Usage:
    python manage.py load_portfolio_data
    python manage.py load_portfolio_data --clear  # Clear existing data first
"""

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction
from portfolio.models import Profile, Project, Skill, ContactMessage, Document, Education, Experience


class Command(BaseCommand):
    help = 'Load portfolio data from fixtures'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before loading fixtures',
        )

    def handle(self, *args, **options):
        """
        Load portfolio data from fixtures.
        """
        self.stdout.write(
            self.style.SUCCESS('Starting portfolio data loading...')
        )

        try:
            with transaction.atomic():
                if options['clear']:
                    self.stdout.write('Clearing existing data...')
                    # Clear data in reverse dependency order
                    ContactMessage.objects.all().delete()
                    Project.objects.all().delete()
                    Skill.objects.all().delete()
                    Education.objects.all().delete()
                    Experience.objects.all().delete()
                    Document.objects.all().delete()
                    Profile.objects.all().delete()
                    self.stdout.write(
                        self.style.WARNING('Existing data cleared.')
                    )

                # Load fixtures in order
                fixtures = [
                    'portfolio/fixtures/profile.json',
                    'portfolio/fixtures/skills.json',
                    'portfolio/fixtures/projects.json',
                    'portfolio/fixtures/education.json',
                    'portfolio/fixtures/experience.json',
                    'portfolio/fixtures/documents.json',
                ]

                for fixture in fixtures:
                    self.stdout.write(f'Loading {fixture}...')
                    call_command('loaddata', fixture, verbosity=0)

                self.stdout.write(
                    self.style.SUCCESS(
                        'Successfully loaded all portfolio data!'
                    )
                )

                # Display summary
                self.stdout.write('\nData Summary:')
                self.stdout.write(f'  - Profiles: {Profile.objects.count()}')
                self.stdout.write(f'  - Projects: {Project.objects.count()}')
                self.stdout.write(f'  - Skills: {Skill.objects.count()}')
                self.stdout.write(f'  - Education: {Education.objects.count()}')
                self.stdout.write(f'  - Experience: {Experience.objects.count()}')
                self.stdout.write(f'  - Documents: {Document.objects.count()}')
                self.stdout.write(f'  - Contact Messages: {ContactMessage.objects.count()}')

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error loading data: {str(e)}')
            )
            raise
