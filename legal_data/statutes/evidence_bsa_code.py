"""
evidence_bsa_code - Aggregator Module
Preserves backward compatibility while keeping all underlying files < 250 KB
"""

from .evidence_bsa_code_part01 import EVIDENCE_SECTIONS_REGISTRY_PART_01
from .evidence_bsa_code_part02 import EVIDENCE_SECTIONS_REGISTRY_PART_02
from .evidence_bsa_code_part03 import EVIDENCE_SECTIONS_REGISTRY_PART_03
from .evidence_bsa_code_part04 import EVIDENCE_SECTIONS_REGISTRY_PART_04

EVIDENCE_SECTIONS_REGISTRY = EVIDENCE_SECTIONS_REGISTRY_PART_01 + EVIDENCE_SECTIONS_REGISTRY_PART_02 + EVIDENCE_SECTIONS_REGISTRY_PART_03 + EVIDENCE_SECTIONS_REGISTRY_PART_04

