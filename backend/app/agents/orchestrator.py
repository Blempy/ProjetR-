from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "docs" / "agents_registry.json"


@lru_cache(maxsize=1)
def load_agents_registry() -> List[Dict[str, Any]]:
    if not REGISTRY_PATH.exists():
        return []
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        return []
    return data


class Orchestrator:
    """Very first stub of the multi-agent orchestrator."""

    def __init__(self) -> None:
        self.registry = load_agents_registry()

    def route(
        self,
        *,
        session_id: str,
        caller: str,
        message: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Return the next agent to trigger along with optional actions."""
        message_type = message.get("type", "")
        next_agent = self._choose_next_agent(caller=caller, message_type=message_type)
        actions: List[Dict[str, Any]] = []

        if next_agent.startswith("specialist:") and context:
            # Example: attach registry entry for the selected specialist
            slug = next_agent.split(":", 1)[1]
            brief = next((item for item in self.registry if item.get("slug") == slug), None)
            if brief:
                actions.append(
                    {
                        "type": "load_brief",
                        "payload": {"slug": slug, "source": brief.get("source")},
                        "status": "pending",
                    }
                )

        return {
            "session_id": session_id,
            "next_agent": next_agent,
            "actions": actions,
            "notes": "Orchestrateur en version brouillon – logique à affiner.",
            "registry_version": len(self.registry),
        }

    @staticmethod
    def _choose_next_agent(*, caller: str, message_type: str) -> str:
        if caller == "welcome":
            return "clarification"
        if message_type == "user_request":
            return "clarification"
        if message_type == "follow_up":
            return "clarification"
        if message_type == "context":
            return "dispatch"
        if message_type == "action_plan":
            return "summary"
        if caller.startswith("specialist"):
            return "summary"
        return "summary"
