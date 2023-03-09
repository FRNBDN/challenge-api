from django.contrib.auth.models import User
from .models import Group
from rest_framework import status
from rest_framework.test import APITestCase


class GroupListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='fran', password='123abc')

    def test_can_list_groups(self):
        fran = User.objects.get(username='fran')
        Group.objects.create(owner=fran, title='test group')
        response = self.client.get('/groups/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_group(self):
        self.client.login(username='fran', password='123abc')
        response = self.client.post('/groups/', {'title': 'test group',
                                                 'tags': 'tag'})
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Group.objects.count(), 1)

    def test_not_logged_in_user_cant_create_group(self):
        response = self.client.post('/groups/', {'title': 'test group',
                                                 'tags': 'tag'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GroupDetailViewTests(APITestCase):
    def setUp(self):
        fran = User.objects.create_user(username='fran', password='123abc')
        cesco = User.objects.create_user(username='cesco', password='123abc')
        Group.objects.create(owner=fran, title='test group 1', tags='tag')
        Group.objects.create(owner=cesco, title='test group 2', tags='tag')

    def test_can_retrieve_group_using_valid_id(self):
        response = self.client.get('/groups/1')
        self.assertEqual(response.data['title'], 'test group 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_group_using_invalid_id(self):
        response = self.client.get('/groups/q')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_groups(self):
        self.client.login(username='fran', password='123abc')
        response = self.client.put('/groups/1', {'title': 'happy group',
                                                 'tags': 'work'})
        group = Group.objects.filter(pk=1).first()
        self.assertEqual(group.title, 'happy group')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='fran', password='123abc')
        response = self.client.put('/groups/2', {'title': 'sad group'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)