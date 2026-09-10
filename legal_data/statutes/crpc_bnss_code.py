"""
crpc_bnss_code - Aggregator Module
Preserves backward compatibility while keeping all underlying files < 250 KB
"""

from .crpc_bnss_code_part01 import CRPC_SECTIONS_REGISTRY_PART_01
from .crpc_bnss_code_part02 import CRPC_SECTIONS_REGISTRY_PART_02
from .crpc_bnss_code_part03 import CRPC_SECTIONS_REGISTRY_PART_03
from .crpc_bnss_code_part04 import CRPC_SECTIONS_REGISTRY_PART_04
from .crpc_bnss_code_part05 import CRPC_SECTIONS_REGISTRY_PART_05
from .crpc_bnss_code_part06 import CRPC_SECTIONS_REGISTRY_PART_06
from .crpc_bnss_code_part07 import CRPC_SECTIONS_REGISTRY_PART_07
from .crpc_bnss_code_part08 import CRPC_SECTIONS_REGISTRY_PART_08
from .crpc_bnss_code_part09 import CRPC_SECTIONS_REGISTRY_PART_09
from .crpc_bnss_code_part10 import CRPC_SECTIONS_REGISTRY_PART_10

CRPC_SECTIONS_REGISTRY = CRPC_SECTIONS_REGISTRY_PART_01 + CRPC_SECTIONS_REGISTRY_PART_02 + CRPC_SECTIONS_REGISTRY_PART_03 + CRPC_SECTIONS_REGISTRY_PART_04 + CRPC_SECTIONS_REGISTRY_PART_05 + CRPC_SECTIONS_REGISTRY_PART_06 + CRPC_SECTIONS_REGISTRY_PART_07 + CRPC_SECTIONS_REGISTRY_PART_08 + CRPC_SECTIONS_REGISTRY_PART_09 + CRPC_SECTIONS_REGISTRY_PART_10

