"""
court_forms_registry - Aggregator Module
Preserves backward compatibility while keeping all underlying files < 250 KB
"""

from .court_forms_registry_part01 import COURT_FORMS_REGISTRY_PART_01
from .court_forms_registry_part02 import COURT_FORMS_REGISTRY_PART_02
from .court_forms_registry_part03 import COURT_FORMS_REGISTRY_PART_03
from .court_forms_registry_part04 import COURT_FORMS_REGISTRY_PART_04
from .court_forms_registry_part05 import COURT_FORMS_REGISTRY_PART_05
from .court_forms_registry_part06 import COURT_FORMS_REGISTRY_PART_06
from .court_forms_registry_part07 import COURT_FORMS_REGISTRY_PART_07
from .court_forms_registry_part08 import COURT_FORMS_REGISTRY_PART_08

COURT_FORMS_REGISTRY = COURT_FORMS_REGISTRY_PART_01 + COURT_FORMS_REGISTRY_PART_02 + COURT_FORMS_REGISTRY_PART_03 + COURT_FORMS_REGISTRY_PART_04 + COURT_FORMS_REGISTRY_PART_05 + COURT_FORMS_REGISTRY_PART_06 + COURT_FORMS_REGISTRY_PART_07 + COURT_FORMS_REGISTRY_PART_08

