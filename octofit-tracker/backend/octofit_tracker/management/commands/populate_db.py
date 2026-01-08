from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Define models for teams, activities, leaderboard, and workouts if not already defined
# For demonstration, we use Django's ORM directly for test data

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all users
        User.objects.all().delete()

        # Create Marvel and DC teams
        Team = self.get_team_model()
        Team.objects.all().delete()
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (superheroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', first_name='Peter', last_name='Parker', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', first_name='Clark', last_name='Kent', team=dc),
        ]

        # Create activities
        Activity = self.get_activity_model()
        Activity.objects.all().delete()
        Activity.objects.create(user=users[0], type='Run', duration=30, calories=300)
        Activity.objects.create(user=users[1], type='Swim', duration=45, calories=400)
        Activity.objects.create(user=users[2], type='Bike', duration=60, calories=500)
        Activity.objects.create(user=users[3], type='Yoga', duration=50, calories=200)

        # Create workouts
        Workout = self.get_workout_model()
        Workout.objects.all().delete()
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create leaderboard
        Leaderboard = self.get_leaderboard_model()
        Leaderboard.objects.all().delete()
        Leaderboard.objects.create(user=users[0], points=1000)
        Leaderboard.objects.create(user=users[1], points=900)
        Leaderboard.objects.create(user=users[2], points=1100)
        Leaderboard.objects.create(user=users[3], points=950)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))

    def get_team_model(self):
        from octofit_tracker.models import Team
        return Team

    def get_activity_model(self):
        from octofit_tracker.models import Activity
        return Activity

    def get_workout_model(self):
        from octofit_tracker.models import Workout
        return Workout

    def get_leaderboard_model(self):
        from octofit_tracker.models import Leaderboard
        return Leaderboard
