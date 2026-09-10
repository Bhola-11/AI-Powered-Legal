"""
criminal_precedents - Aggregator Module
Preserves backward compatibility while keeping all underlying files < 250 KB
"""

from .criminal_precedents_part01 import PRECEDENTS_DATABASE_PART_01
from .criminal_precedents_part02 import PRECEDENTS_DATABASE_PART_02
from .criminal_precedents_part03 import PRECEDENTS_DATABASE_PART_03
from .criminal_precedents_part04 import PRECEDENTS_DATABASE_PART_04
from .criminal_precedents_part05 import PRECEDENTS_DATABASE_PART_05

PRECEDENTS_DATABASE = PRECEDENTS_DATABASE_PART_01 + PRECEDENTS_DATABASE_PART_02 + PRECEDENTS_DATABASE_PART_03 + PRECEDENTS_DATABASE_PART_04 + PRECEDENTS_DATABASE_PART_05

