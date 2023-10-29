from applications.models import BursaryApplication


class BursaryApplicationService:
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
