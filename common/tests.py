import unittest
from unittest.mock import Mock


from common.permissions import IsOwnerOrReadOnly


class IsOwnerOrReadOnlyTests(unittest.TestCase):
    def setUp(self):
        self.permission = IsOwnerOrReadOnly()

    def test_has_permission_authenticated_user(self):
        # Create a mock request and view
        request = Mock()
        request.user = Mock()
        request.user.is_authenticated = True
        view = Mock()

        # Check if the permission allows access for authenticated users
        has_permission = self.permission.has_permission(request, view)

        # Assert that the permission returns True
        self.assertTrue(has_permission)

    def test_has_permission_unauthenticated_user(self):
        # Create a mock request and view
        request = Mock()
        request.user = Mock()
        request.user.is_authenticated = False
        view = Mock()

        # Check if the permission denies access for unauthenticated users
        has_permission = self.permission.has_permission(request, view)

        # Assert that the permission returns False
        self.assertFalse(has_permission)

    def test_has_object_permission_safe_methods(self):
        # Create a mock request, view, and object
        request = Mock()
        request.method = "GET"
        view = Mock()
        obj = Mock()
        obj.user = Mock()
        request.user = obj.user

        # Check if the permission allows access for safe methods
        has_object_permission = self.permission.has_object_permission(
            request, view, obj
        )

        # Assert that the permission returns True
        self.assertTrue(has_object_permission)

    def test_has_object_permission_unsafe_methods(self):
        # Create a mock request, view, and object
        request = Mock()
        request.method = "POST"  # An unsafe method
        view = Mock()
        obj = Mock()
        obj.user = Mock()
        request.user = obj.user

        # Check if the permission allows access for unsafe methods when the user is the owner
        has_object_permission = self.permission.has_object_permission(
            request, view, obj
        )

        # Assert that the permission returns True
        self.assertTrue(has_object_permission)

        # Change the user to a different one
        request.user = Mock()

        # Check if the permission denies access for unsafe methods when the user is not the owner
        has_object_permission = self.permission.has_object_permission(
            request, view, obj
        )

        # Assert that the permission returns False
        self.assertFalse(has_object_permission)
