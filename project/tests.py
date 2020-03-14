from django.test import TestCase
from project.models import Project
from django.core.files.base import ContentFile
from django.contrib.auth.models import User

# Create your tests here.

class ProjectTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='john', email='jlennon@beatles.com', password='glass onion')
        Project.objects.create(project_id=1,project_title="designing",project_description="This is designing project",availability_status=True, project_type="designing",user_id=1)
        Project.objects.create(project_id=2,project_title="game development",project_description="This is game development project",availability_status=True, project_type="game development",user_id=1)

    def test_project1(self):
        p1 = Project.objects.get(project_title='designing')
        self.assertEqual(p1.project_title,"designing")

    def test_project2(self):
        p2 = Project.objects.get(project_title='game development')
        self.assertEqual(p2.project_title,"game")

