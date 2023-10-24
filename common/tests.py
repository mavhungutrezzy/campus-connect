import unittest
from unittest.mock import Mock

from common.permissions import IsOwnerOrReadOnly


class IsOwnerOrReadOnlyTests(unittest.TestCase):
    def setUp(self):
        self.permission = IsOwnerOrReadOnly()

    def test_has_permission_authenticated_user(self):
        request = Mock()
        request.user = Mock()
        request.user.is_authenticated = True
        view = Mock()

        has_permission = self.permission.has_permission(request, view)

        self.assertTrue(has_permission)

    def test_has_permission_unauthenticated_user(self):
        request = Mock()
        request.user = Mock()
        request.user.is_authenticated = False
        view = Mock()

        has_permission = self.permission.has_permission(request, view)

        self.assertFalse(has_permission)

    def test_has_object_permission_safe_methods(self):
        request = Mock()
        request.method = "GET"
        view = Mock()
        obj = Mock()
        obj.user = Mock()
        request.user = obj.user

        has_object_permission = self.permission.has_object_permission(request, view, obj)

        self.assertTrue(has_object_permission)

    def test_has_object_permission_unsafe_methods(self):
        request = Mock()
        request.method = "POST"  # An unsafe method
        view = Mock()
        obj = Mock()
        obj.user = Mock()
        request.user = obj.user

        has_object_permission = self.permission.has_object_permission(request, view, obj)

        self.assertTrue(has_object_permission)

        request.user = Mock()

        has_object_permission = self.permission.has_object_permission(request, view, obj)

        self.assertFalse(has_object_permission)
