from core.skill import Skill

def get_replication_investigation_skill() -> Skill:
    return Skill(
        identity="replication_investigation",
        description="Knowledge on how to investigate replication failures.",
        knowledge="Replication pulls data from on-prem DBs to Kafka/Databricks.",
        procedures="If replication is STOPPED, you must check the downstream Bronze pipeline status.",
        heuristics="A FAILED downstream pipeline is the most common cause of STOPPED upstream replication."
    )
