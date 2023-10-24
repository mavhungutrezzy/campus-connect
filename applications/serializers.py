from rest_framework import serializers

from applications.models import BursaryApplication, CourseApplication


class BursaryApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for the BursaryApplication model.

    This serializer is used to convert BursaryApplication model instances into JSON representation and vice versa.

    Args:
        serializers.ModelSerializer: The base serializer class provided by Django REST Framework.

    Returns:
        None

    Example:
        ```python
        serializer = BursaryApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ```"""

    class Meta:
        model = BursaryApplication
        fields = "__all__"


class CourseApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for the BursaryApplication model.

    This serializer is used to convert BursaryApplication model instances into JSON representation and vice versa.

    Args:
        serializers.ModelSerializer: The base serializer class provided by Django REST Framework.

    Returns:
        None

    Example:
        ```python
        serializer = BursaryApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ```"""

    class Meta:
        model = CourseApplication
        fields = "__all__"
