from rest_framework import serializers

from .models import Bursary


class BursarySerializer(serializers.ModelSerializer):
    """
    Serializes the Bursary model for API responses.

    The BursarySerializer class is responsible for converting Bursary model instances into a format that can be easily rendered into JSON or other content types. It specifies the model and fields to include in the serialization.

    Attributes:
        model (Bursary): The Bursary model class.
        fields (str): The fields to include in the serialization. In this case, all fields are included.

    Example:
        ```python
        serializer = BursarySerializer(bursary_instance)
        serialized_data = serializer.data
        ```"""

    class Meta:
        model = Bursary
        fields = "__all__"
