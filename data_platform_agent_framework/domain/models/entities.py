from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class Environment(Enum):
    DEV = "DEV"
    TEST = "TEST"
    PROD = "PROD"

@dataclass
class Database:
    id: str
    name: str
    server: str
    region: str
    environment: Environment

@dataclass
class Table:
    name: str
    database_id: str
    schema: str = "dbo"

@dataclass
class ReplicationConfig:
    id: str
    source_database_id: str
    target_topic: str
    tables: List[str]
    status: str

class DataLayer(Enum):
    RAW = "RAW"
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"

@dataclass
class PipelineJob:
    id: str
    name: str
    source_topic: str
    target_layer: DataLayer
    status: str

@dataclass
class Incident:
    id: str
    title: str
    description: str
    affected_components: List[str]
    status: str
