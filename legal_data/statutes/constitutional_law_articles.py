"""
constitutional_law_articles - Aggregator Module
Preserves backward compatibility while keeping all underlying files < 250 KB
"""

from .constitutional_law_articles_part01 import STATUTORY_REGISTRY_PART_01
from .constitutional_law_articles_part02 import STATUTORY_REGISTRY_PART_02
from .constitutional_law_articles_part03 import STATUTORY_REGISTRY_PART_03
from .constitutional_law_articles_part04 import STATUTORY_REGISTRY_PART_04
from .constitutional_law_articles_part05 import STATUTORY_REGISTRY_PART_05
from .constitutional_law_articles_part06 import STATUTORY_REGISTRY_PART_06
from .constitutional_law_articles_part07 import STATUTORY_REGISTRY_PART_07
from .constitutional_law_articles_part08 import STATUTORY_REGISTRY_PART_08

STATUTORY_REGISTRY = STATUTORY_REGISTRY_PART_01 + STATUTORY_REGISTRY_PART_02 + STATUTORY_REGISTRY_PART_03 + STATUTORY_REGISTRY_PART_04 + STATUTORY_REGISTRY_PART_05 + STATUTORY_REGISTRY_PART_06 + STATUTORY_REGISTRY_PART_07 + STATUTORY_REGISTRY_PART_08

