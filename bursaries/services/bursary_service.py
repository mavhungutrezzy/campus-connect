from bursaries.models import Bursary


class BursaryService:
    """
    Provides operations for managing Bursary objects.

    Attributes:
        None
    """

    @staticmethod
    def create_bursary(data):
        """
        Creates a new Bursary object.

        Args:
            data (dict): The data to create the Bursary object.

        Returns:
            Bursary: The created Bursary object.
        """
        return Bursary.objects.create(**data)

    @staticmethod
    def update_bursary(bursary, data):
        """
        Updates a Bursary object with new data.

        Args:
            bursary (Bursary): The Bursary object to update.
            data (dict): The new data to update the Bursary object.

        Returns:
            None
        """
        for key, value in data.items():
            setattr(bursary, key, value)
        bursary.save()

    @staticmethod
    def get_bursary_by_id(bursary_id):
        """
        Retrieves a Bursary object by its ID.

        Args:
            bursary_id (int): The ID of the Bursary object.

        Returns:
            Bursary: The retrieved Bursary object.

        Raises:
            Bursary.DoesNotExist: If the Bursary object does not exist.
        """
        return Bursary.objects.get(pk=bursary_id)

    @staticmethod
    def delete_bursary(bursary):
        """
        Deletes a Bursary object.

        Args:
            bursary (Bursary): The Bursary object to delete.

        Returns:
            None
        """
        bursary.delete()
