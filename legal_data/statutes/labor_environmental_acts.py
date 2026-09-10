"""
labor_environmental_acts - Aggregator Module
Preserves backward compatibility while keeping all underlying files < 250 KB
"""

from .labor_environmental_acts_part01 import LABOR_ENV_SECTIONS_PART_01
from .labor_environmental_acts_part02 import LABOR_ENV_SECTIONS_PART_02
from .labor_environmental_acts_part03 import LABOR_ENV_SECTIONS_PART_03
from .labor_environmental_acts_part04 import LABOR_ENV_SECTIONS_PART_04
from .labor_environmental_acts_part05 import LABOR_ENV_SECTIONS_PART_05
from .labor_environmental_acts_part06 import LABOR_ENV_SECTIONS_PART_06
from .labor_environmental_acts_part07 import LABOR_ENV_SECTIONS_PART_07
from .labor_environmental_acts_part08 import LABOR_ENV_SECTIONS_PART_08
from .labor_environmental_acts_part09 import LABOR_ENV_SECTIONS_PART_09
from .labor_environmental_acts_part10 import LABOR_ENV_SECTIONS_PART_10
from .labor_environmental_acts_part11 import LABOR_ENV_SECTIONS_PART_11
from .labor_environmental_acts_part12 import LABOR_ENV_SECTIONS_PART_12

LABOR_ENV_SECTIONS = LABOR_ENV_SECTIONS_PART_01 + LABOR_ENV_SECTIONS_PART_02 + LABOR_ENV_SECTIONS_PART_03 + LABOR_ENV_SECTIONS_PART_04 + LABOR_ENV_SECTIONS_PART_05 + LABOR_ENV_SECTIONS_PART_06 + LABOR_ENV_SECTIONS_PART_07 + LABOR_ENV_SECTIONS_PART_08 + LABOR_ENV_SECTIONS_PART_09 + LABOR_ENV_SECTIONS_PART_10 + LABOR_ENV_SECTIONS_PART_11 + LABOR_ENV_SECTIONS_PART_12

