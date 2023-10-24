import pytest
from django.utils.text import slugify

from bursaries.models import Bursary


@pytest.mark.django_db
class TestBursary:
    @pytest.mark.parametrize(
        "bursary_name, provider, provider_description, bursary_description, eligibility_requirements, "
        "application_deadline, application_method, application_url, bursary_coverage, field_of_study, "
        "contact_email, contact_number, covers_full_tuition, supported_institutions",
        [
            (
                "Bursary 1",
                "Provider 1",
                "Provider 1 description",
                "Bursary 1 description",
                "Eligibility requirements 1",
                "2023-01-01",
                "Application method 1",
                "https://www.example.com",
                {"Coverage 1": "Details 1"},
                ["Field of Study 1", "Field of Study 2"],
                "test@example.com",
                "1234567890",
                True,
                ["Institution 1", "Institution 2"],
            ),
            (
                "Bursary 2",
                "Provider 2",
                "Provider 2 description",
                "Bursary 2 description",
                "Eligibility requirements 2",
                "2000-01-01",
                "Application method 2",
                "https://www.example.com",
                {},
                [],
                "test@example.com",
                "1234567890",
                False,
                [],
            ),
            (
                "Bursary 3",
                "Provider 3",
                "Provider 3 description",
                "Bursary 3 description",
                "Eligibility requirements 3",
                "2023-01-01",
                "Application method 3",
                "invalid-url",
                {"Coverage 3": "Details 3"},
                ["Field of Study 3"],
                "test@example.com",
                "1234567890",
                True,
                ["Institution 3"],
            ),
        ],
        ids=[
            "happy_path_realistic_values",
            "edge_case_minimum_values",
            "error_case_invalid_application_url",
        ],
    )
    def test_save_bursary(
        self,
        bursary_name,
        provider,
        provider_description,
        bursary_description,
        eligibility_requirements,
        application_deadline,
        application_method,
        application_url,
        bursary_coverage,
        field_of_study,
        contact_email,
        contact_number,
        covers_full_tuition,
        supported_institutions,
    ):
        bursary = Bursary(
            bursary_name=bursary_name,
            provider=provider,
            provider_description=provider_description,
            bursary_description=bursary_description,
            eligibility_requirements=eligibility_requirements,
            application_deadline=application_deadline,
            application_method=application_method,
            application_url=application_url,
            bursary_coverage=bursary_coverage,
            field_of_study=field_of_study,
            contact_email=contact_email,
            contact_number=contact_number,
            covers_full_tuition=covers_full_tuition,
            supported_institutions=supported_institutions,
        )

        bursary.save()

        assert bursary.slug == slugify(bursary_name)
