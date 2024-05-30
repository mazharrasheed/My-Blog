from django.test import TestCase
# from .models import Blog

# Create your tests here.


from django.urls import reverse

class MyViewTestCase(TestCase):

    def test_detail_view(self):
        # Create an instance of your model (if needed)
        # your_model = YourModel.objects.create(...)

        # Replace 'detail' with the name of your view and provide the 'id' parameter
        url = reverse('detail', kwargs={'id': 2})  # Replace '1' with the desired ID

        # Make a GET request to the detail view with the specified ID
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Optionally, assert that the response contains specific content
        # For example, if your detail view renders a template with specific content
        # you can use self.assertContains to check for that content
        # self.assertContains(response, 'data')