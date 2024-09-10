import pytest
from eidolon_ai_client.client import Agent


@pytest.fixture
def agent():
    return Agent.get("repo-expert")


@pytest.mark.vcr()
async def test_agent(agent: Agent):
    process = await agent.create_process()
    response = await process.action("converse", "Why should I use Eidolon?")
    assert "eidolon is an open-source agent service sdk" in response.data.lower()