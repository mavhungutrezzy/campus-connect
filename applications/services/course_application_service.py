from applications.models import CourseApplication


class CourseApplicationService:
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
