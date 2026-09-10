"""
notices_agreements_forms - Aggregator Module
Preserves backward compatibility while keeping all underlying files < 250 KB
"""

from .notices_agreements_forms_part01 import PLEADING_TEMPLATES_REGISTRY_PART_01
from .notices_agreements_forms_part02 import PLEADING_TEMPLATES_REGISTRY_PART_02

PLEADING_TEMPLATES_REGISTRY = PLEADING_TEMPLATES_REGISTRY_PART_01 + PLEADING_TEMPLATES_REGISTRY_PART_02

