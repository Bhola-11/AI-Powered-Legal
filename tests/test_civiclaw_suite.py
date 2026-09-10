from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.accounts.models import Role
from apps.firms.models import LawFirm
from apps.cases.models import Case, CaseType, CaseStatus
from apps.clients.models import ClientProfile
from apps.courts.models import CourtComplex, Judge
from apps.ai_engine.services import LegalAIService

User = get_user_model()

class CivicLawTestSuite(TestCase):
    def setUp(self):
        self.firm = LawFirm.objects.create(name="CivicLaw Legal Chambers", email="chambers@civiclaw.local", phone="+91-11-23456789")
        self.super_admin = User.objects.create_superuser(username="admin", email="admin@civiclaw.local", password="AdminPassword123!", role=Role.SUPER_ADMIN)
        self.lawyer = User.objects.create_user(username="advocate_sharma", email="sharma@civiclaw.local", password="LawyerPassword123!", role=Role.LAWYER, law_firm=self.firm)
        self.client_user = User.objects.create_user(username="client_corp", email="client@corp.local", password="ClientPassword123!", role=Role.CLIENT)
        self.client_profile = ClientProfile.objects.create(user=self.client_user, display_name="Nexus Technologies Corp", email="contact@nexus.local", phone="+91-9876543210")
        self.court = CourtComplex.objects.create(name="High Court of Delhi", city="New Delhi", state="Delhi", address="Sher Shah Road")
        self.judge = Judge.objects.create(name="Hon. Justice K.R. Rao", court_complex=self.court)
        self.case_type = CaseType.objects.create(code="CS", name="Civil Suit", category="CIVIL")

    def test_user_roles(self):
        self.assertTrue(self.super_admin.is_super_admin())
        self.assertTrue(self.lawyer.is_lawyer())
        self.assertTrue(self.client_user.is_client())

    def test_case_creation_lifecycle(self):
        case = Case.objects.create(
            case_number="CS/2026/001",
            title="Nexus Technologies v. Global Infra",
            case_type=self.case_type,
            court_complex=self.court,
            presiding_judge=self.judge,
            client=self.client_profile,
            law_firm=self.firm,
            description="Suit for Specific Performance and Damages",
            status=CaseStatus.INTAKE
        )
        self.assertEqual(case.status, CaseStatus.INTAKE)
        case.status = CaseStatus.REGISTERED
        case.save()
        self.assertEqual(case.status, CaseStatus.REGISTERED)

    def test_ai_copilot_services(self):
        summary = LegalAIService.generate_case_summary("Contract Breach", "Breach of distribution agreement", "Liquidated damages clause")
        self.assertIn("Executive Summary", summary["summary"])
        self.assertGreater(summary["confidence_score"], 0.90)

        conflict = LegalAIService.check_conflict_of_interest("Nexus Tech", "Global Infra", ["Nexus Tech", "Alpha Corp"], [])
        self.assertFalse(conflict["has_conflict"])
