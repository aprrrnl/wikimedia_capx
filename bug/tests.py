from django.test import TestCase
from django.urls import reverse
from django.contrib import messages
from bug.models import Bug

class BugModelTest(TestCase):

    def setUp(self):
        # Create a sample Bug instance for testing
        self.sample_bug = Bug.objects.create(
            description="Sample Bug",
            bug_type="error",
            status="unconfirmed"
        )

    def test_bug_creation(self):
        """Test that a Bug can be created."""
        self.assertEqual(self.sample_bug.description, "Sample Bug")
        self.assertEqual(self.sample_bug.bug_type, "error")
        self.assertEqual(self.sample_bug.status, "unconfirmed")

    def test_bug_status_choices(self):
        """Test that bug status is one of the defined choices."""
        for choice in Bug.STATUS_CHOICES:
            self.sample_bug.status = choice[0]
            self.sample_bug.save()
            self.assertEqual(self.sample_bug.status, choice[0])

    def test_bug_type_choices(self):
        """Test that bug type is one of the defined choices."""
        for choice in Bug.BUG_TYPES:
            self.sample_bug.bug_type = choice[0]
            self.sample_bug.save()
            self.assertEqual(self.sample_bug.bug_type, choice[0])

    def test_bug_str_representation(self):
        """Test the __str__ method of the Bug model."""
        self.assertEqual(str(self.sample_bug), "Sample Bug")

    def test_bug_report_date_auto_now_add(self):
        """Test that the report_date is automatically set to the current date and time."""
        self.assertIsNotNone(self.sample_bug.report_date)

    def tearDown(self):
        # Clean up by deleting the sample bug instance
        self.sample_bug.delete()

class BugViewsTest(TestCase):
    def setUp(self):
        self.test_bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            status="unconfirmed"
        )

    def test_add_bug_view_get(self):
        response = self.client.get(reverse('add_bug'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug/bug-form.html')

    def test_add_bug_view_post_success(self):
        data = {
            'description': 'New Bug',
            'bug_type': 'error',
            'status': 'unconfirmed',
        }
        response = self.client.post(reverse('add_bug'), data)
        self.assertEqual(response.status_code, 302)  # Expect a redirect
        self.assertRedirects(response, reverse('all_bugs'))

        # Check if a bug was added to the database
        self.assertEqual(Bug.objects.filter(description='New Bug').count(), 1)

    def test_add_bug_view_post_failure(self):
        data = {
            'description': 'Invalid Bug',  # Missing required fields
        }
        response = self.client.post(reverse('add_bug'), data)
        self.assertEqual(response.status_code, 200)  # Expect to stay on the same page
        self.assertTemplateUsed(response, 'bug/bug-form.html')

    def test_all_bugs_view(self):
        response = self.client.get(reverse('all_bugs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug/all-bugs.html')
        self.assertInHTML('Test Bug', str(response.content))  # Check if the test bug is displayed

    def test_bug_detail_view(self):
        response = self.client.get(reverse('bug_detail', args=[self.test_bug.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug/bug-detail.html')
        pattern = r'Test Bug'
        self.assertRegex(str(response.content), pattern) # Check if the test bug details are displayed
