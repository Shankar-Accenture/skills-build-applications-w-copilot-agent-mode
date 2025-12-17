from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_user_create(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Test Team')
        self.assertEqual(user.name, 'Test')
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')
    def test_activity_create(self):
        activity = Activity.objects.create(user='Test', activity='Run', duration=10)
        self.assertEqual(activity.activity, 'Run')
    def test_workout_create(self):
        workout = Workout.objects.create(user='Test', workout='Pushup', reps=20)
        self.assertEqual(workout.reps, 20)
    def test_leaderboard_create(self):
        lb = Leaderboard.objects.create(user='Test', points=123)
        self.assertEqual(lb.points, 123)
