from applications.models import CourseApplication


class CourseApplicationService:
    """
        Service class for managing Course Applications.

        This class provides static methods for creating, updating, retrieving, and deleting Course Application instances.

        Methods:
            create_course_application(data): Creates a new Course Application with the provided data.
            update_course_application(course_application, data): Updates the fields of a Course Application with the provided data.
            get_course_application_by_id(course_application_id): Retrieves a Course Application by its ID.
            delete_course_application(course_application): Deletes a Course Application.

        Args:
            data (dict): A dictionary containing the data for creating or updating a Course Application.
            course_application (CourseApplication): The Course Application instance to be updated.
            course_application_id (int): The ID of the Course Application to retrieve.
            course_application (CourseApplication): The Course Application instance to be deleted.

        Returns:
            None

    class CourseApplicationListCreateView(generics.ListCreateAPIView):
        queryset = CourseApplication.objects.all()
        serializer_class = CourseApplicationSerializer
        course_application_service = CourseApplicationService()
        authentication_classes = [SessionAuthentication]
        permission_classes = (IsOwnerOrReadOnly,)

        def get_queryset(self):
            return self.course_application_service.get_course_applications(self.request.user)


        def post(self, request, *args, **kwargs):
            serializer = CourseApplicationSerializer(data=request.data)
            if serializer.is_valid():
                course_data = serializer.validated_data
                course_application = (
                    self.course_application_service.create_course_application(
                        course_data
                    )
                )
                return Response(
                    CourseApplicationSerializer(course_application).data,
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    class CourseApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = CourseApplication.objects.all()
        serializer_class = CourseApplicationSerializer
        course_application_service = CourseApplicationService()
        authentication_classes = [SessionAuthentication]
        permission_classes = (IsOwnerOrReadOnly,)

        def put(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = CourseApplicationSerializer(instance, data=request.data)
            if serializer.is_valid():
                course_data = serializer.validated_data
                self.course_application_service.update_course_application(
                    instance, course_data
                )
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, *args, **kwargs):
            instance = self.get_object()
            self.course_application_service.delete_course_application(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        Example:
            ```python
            data = {
                'user': user,
                'course': course,
                'notes': notes,
                'date_applied': date_applied
            }

            # Creating a new Course Application
            CourseApplicationService.create_course_application(data)

            # Updating an existing Course Application
            CourseApplicationService.update_course_application(course_application, data)

            # Retrieving a Course Application by ID
            course_application = CourseApplicationService.get_course_application_by_id(course_application_id)

            # Deleting a Course Application
            CourseApplicationService.delete_course_application(course_application)
            ```"""

    @staticmethod
    def get_course_applications(user):
        return CourseApplication.objects.filter(user=user)

    @staticmethod
    def create_course_application(data):
        return CourseApplication.objects.create(**data)

    @staticmethod
    def update_course_application(course_application, data):
        for key, value in data.items():
            setattr(course_application, key, value)
        course_application.save()

    @staticmethod
    def get_course_application_by_id(course_application_id):
        return CourseApplication.objects.get(pk=course_application_id)

    @staticmethod
    def delete_course_application(course_application):
        course_application.delete()
