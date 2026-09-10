"""
ipc_bns_penal_code - Aggregator Module
Preserves backward compatibility while keeping all underlying files < 250 KB
"""

from .ipc_bns_penal_code_part01 import IPC_OFFENSES_REGISTRY_PART_01
from .ipc_bns_penal_code_part02 import IPC_OFFENSES_REGISTRY_PART_02
from .ipc_bns_penal_code_part03 import IPC_OFFENSES_REGISTRY_PART_03
from .ipc_bns_penal_code_part04 import IPC_OFFENSES_REGISTRY_PART_04
from .ipc_bns_penal_code_part05 import IPC_OFFENSES_REGISTRY_PART_05
from .ipc_bns_penal_code_part06 import IPC_OFFENSES_REGISTRY_PART_06
from .ipc_bns_penal_code_part07 import IPC_OFFENSES_REGISTRY_PART_07
from .ipc_bns_penal_code_part08 import IPC_OFFENSES_REGISTRY_PART_08
from .ipc_bns_penal_code_part09 import IPC_OFFENSES_REGISTRY_PART_09
from .ipc_bns_penal_code_part10 import IPC_OFFENSES_REGISTRY_PART_10
from .ipc_bns_penal_code_part11 import IPC_OFFENSES_REGISTRY_PART_11

IPC_OFFENSES_REGISTRY = IPC_OFFENSES_REGISTRY_PART_01 + IPC_OFFENSES_REGISTRY_PART_02 + IPC_OFFENSES_REGISTRY_PART_03 + IPC_OFFENSES_REGISTRY_PART_04 + IPC_OFFENSES_REGISTRY_PART_05 + IPC_OFFENSES_REGISTRY_PART_06 + IPC_OFFENSES_REGISTRY_PART_07 + IPC_OFFENSES_REGISTRY_PART_08 + IPC_OFFENSES_REGISTRY_PART_09 + IPC_OFFENSES_REGISTRY_PART_10 + IPC_OFFENSES_REGISTRY_PART_11

