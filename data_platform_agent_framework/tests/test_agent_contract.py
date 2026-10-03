from core.agent_contract import AgentContract, AgentPurpose

def test_contract_validation():
    contract = AgentContract(
        identity="test",
        purpose=AgentPurpose.MONITORING,
        domain="DataPlatform"
    )
    assert contract.validate()

def test_contract_invalid():
    contract = AgentContract(
        identity="",
        purpose=AgentPurpose.MONITORING,
        domain="DataPlatform"
    )
    assert not contract.validate()
