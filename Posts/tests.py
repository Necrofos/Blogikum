from django.test import TestCase
import unittest
from django.shortcuts import redirect, reverse
import http
# Create your tests here.
class GetPagesTestCase(TestCase):
    def setUp(self):
        pass

    def test_case_1(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_case_2(self):
        path = reverse('about_project')
        response = self.client.get(path)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_case_3(self):
        path = reverse('rules')
        response = self.client.get(path)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def tear_down(self):
        pass
