from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.accounts.models import Role, UserProfile
from apps.firms.models import LawFirm, BranchOffice, PracticeArea, FirmSetting
from apps.clients.models import ClientProfile, ClientType
from apps.courts.models import CourtComplex, CourtRoom, Judge, CourtLevel
from apps.cases.models import Case, CaseType, CaseStatus, CasePriority
from apps.hearings.models import Hearing, HearingType
from apps.billing.models import Invoice, InvoiceStatus
from django.utils import timezone
import datetime

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds initial enterprise legal data for CivicLaw platform'

    def handle(self, *args, **options):
        self.stdout.write("Seeding CivicLaw enterprise records...")
        
        # Law Firm
        firm, _ = LawFirm.objects.get_or_create(
            name="CivicLaw Premier Legal LLP",
            defaults={'email': 'contact@civiclaw.local', 'phone': '+91-11-23000000', 'primary_office_address': 'Connaught Place, New Delhi'}
        )
        FirmSetting.objects.get_or_create(firm=firm)

        # Users
        admin_user, _ = User.objects.get_or_create(
            username="admin",
            defaults={'email': 'admin@civiclaw.local', 'role': Role.SUPER_ADMIN, 'is_staff': True, 'is_superuser': True}
        )
        admin_user.set_password("Admin@12345")
        admin_user.save()

        lawyer, _ = User.objects.get_or_create(
            username="advocate_kapoor",
            defaults={'email': 'kapoor@civiclaw.local', 'role': Role.LAWYER, 'first_name': 'Vikram', 'last_name': 'Kapoor', 'law_firm': firm}
        )
        lawyer.set_password("Lawyer@12345")
        lawyer.save()

        # Courts & Judges
        hc, _ = CourtComplex.objects.get_or_create(
            name="High Court of Delhi",
            defaults={'level': CourtLevel.HIGH_COURT, 'city': 'New Delhi', 'state': 'Delhi', 'address': 'Sher Shah Road'}
        )
        room, _ = CourtRoom.objects.get_or_create(court_complex=hc, room_number="Courtroom 04")
        judge, _ = Judge.objects.get_or_create(name="Justice Sanjay Kishan", defaults={'court_complex': hc, 'assigned_courtroom': room})

        # Clients & Cases
        client, _ = ClientProfile.objects.get_or_create(
            display_name="Bharat Heavy Infrastructure Ltd",
            defaults={'client_type': ClientType.CORPORATE, 'email': 'legal@bharat-infra.local', 'phone': '+91-9811122233', 'billing_address': 'Barakhamba Road, New Delhi'}
        )
        ctype, _ = CaseType.objects.get_or_create(code="ARB", defaults={'name': 'Arbitration Petition', 'category': 'ARBITRATION'})
        
        case, _ = Case.objects.get_or_create(
            case_number="ARB/2026/108",
            defaults={
                'title': 'Bharat Heavy Infra v. Metrorail Corporation',
                'case_type': ctype,
                'court_complex': hc,
                'courtroom': room,
                'presiding_judge': judge,
                'client': client,
                'law_firm': firm,
                'status': CaseStatus.HEARING_SCHEDULED,
                'priority': CasePriority.HIGH,
                'filing_date': timezone.now().date(),
                'next_hearing_date': timezone.now().date() + datetime.timedelta(days=7),
                'description': 'Section 9 Arbitration Petition for urgent interim measures restraining bank guarantee invocation.',
            }
        )

        Hearing.objects.get_or_create(
            case=case,
            hearing_date=timezone.now().date() + datetime.timedelta(days=7),
            defaults={'start_time': '10:30:00', 'courtroom': room, 'judge': judge, 'hearing_type': HearingType.INTERIM_RELIEF, 'purpose': 'Hearing on Interim Injunction'}
        )

        self.stdout.write(self.style.SUCCESS("CivicLaw enterprise seed data initialized successfully."))
