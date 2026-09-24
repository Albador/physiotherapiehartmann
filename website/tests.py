from django.test import TestCase
from django.urls import reverse


class WebsitePageTests(TestCase):
    def test_root_redirects_to_home(self):
        response = self.client.get('/')
        self.assertRedirects(
            response,
            reverse('website:home'),
            status_code=301,
            fetch_redirect_response=False,
        )

    def test_pages_ok(self):
        pages = ('home', 'impressum', 'leistung', 'praxis', 'team', 'open')
        for name in pages:
            with self.subTest(page=name):
                response = self.client.get(reverse(f'website:{name}'))
                self.assertEqual(response.status_code, 200)

    def test_legacy_urls_redirect_to_trailing_slash(self):
        response = self.client.get('/website/home')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, '/website/home/')

    def test_home_serves_static_assets(self):
        response = self.client.get(reverse('website:home'))
        self.assertContains(response, '/static/website/css/style.css')
        self.assertContains(response, '/static/website/pictures/daniela.jpg')

    def test_team_lists_members(self):
        response = self.client.get(reverse('website:team'))
        for name in ('Daniela Hartmann', 'Ulrike Strobelt', 'Elke Lindworsky'):
            with self.subTest(name=name):
                self.assertContains(response, name)
        self.assertContains(response, 'Manuelle Lymphdrainage')
        self.assertContains(response, 'PNF Neuro')
        self.assertContains(response, 'Touch for Health')
