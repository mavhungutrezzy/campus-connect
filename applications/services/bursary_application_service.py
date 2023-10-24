from applications.models import BursaryApplication


class BursaryApplicationService:
    """
    Service class for managing Bursary Applications.

    This class provides static methods for creating, updating, retrieving, and deleting Bursary Application instances.

    Methods:
        create_bursary_application(data): Creates a new Bursary Application with the provided data.
        update_bursary_application(bursary_application, data): Updates the fields of a Bursary Application with the provided data.
        get_bursary_application_by_id(bursary_application_id): Retrieves a Bursary Application by its ID.
        delete_bursary_application(bursary_application): Deletes a Bursary Application.

    Args:
        data (dict): A dictionary containing the data for creating or updating a Bursary Application.
        bursary_application (BursaryApplication): The Bursary Application instance to be updated.
        bursary_application_id (int): The ID of the Bursary Application to retrieve.
        bursary_application (BursaryApplication): The Bursary Application instance to be deleted.

    Returns:
        None

    Example:
        ```python
        data = {
            'user': user,
            'bursary': bursary,
            'notes': notes,
            'date_applied': date_applied
        }

        # Creating a new Bursary Application
        BursaryApplicationService.create_bursary_application(data)

        # Updating an existing Bursary Application
        BursaryApplicationService.update_bursary_application(bursary_application, data)

        # Retrieving a Bursary Application by ID
        bursary_application = BursaryApplicationService.get_bursary_application_by_id(bursary_application_id)

        # Deleting a Bursary Application
        BursaryApplicationService.delete_bursary_application(bursary_application)
        ```"""

    @staticmethod
    def get_bursary_applications(user):
        return BursaryApplication.objects.filter(user=user)

    @staticmethod
    def create_bursary_application(data):
        return BursaryApplication.objects.create(**data)

    @staticmethod
    def update_bursary_application(bursary_application, data):
        for key, value in data.items():
            setattr(bursary_application, key, value)
        bursary_application.save()

    @staticmethod
    def get_bursary_application_by_id(bursary_application_id):
        return BursaryApplication.objects.get(pk=bursary_application_id)

    @staticmethod
    def delete_bursary_application(bursary_application):
        bursary_application.delete()
