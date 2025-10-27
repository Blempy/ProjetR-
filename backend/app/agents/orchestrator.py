from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "docs" / "agents_registry.json"

from .knowledge_base import KnowledgeBase, KBEntry


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
        try:
            self.memory = KnowledgeBase()
        except Exception:
            self.memory = None

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

        memory_action = self._check_memory(message=message, context=context or {})
        if memory_action:
            return {
                "session_id": session_id,
                "next_agent": "memory_guard",
                "actions": [memory_action],
                "notes": "Réponse servie depuis la mémoire locale.",
                "registry_version": len(self.registry),
            }

        self._learn_if_needed(caller=caller, message=message, context=context or {})

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

    def _check_memory(
        self,
        message: Dict[str, Any],
        context: Dict[str, Any],
    ) -> Optional[Dict[str, Any]]:
        if not self.memory:
            return None

        message_type = message.get("type")
        if message_type not in {"user_request", "follow_up"}:
            return None

        question = self._extract_question(message, context)
        if not question:
            return None

        metadata = self._extract_metadata(context)

        entry: Optional[KBEntry] = self.memory.lookup(question, metadata)
        if not entry:
            return None

        payload = {
            "answer": entry.answer,
            "question": entry.question,
            "similarity": entry.similarity,
            "metadata": entry.metadata,
            "usage_count": entry.usage_count,
        }
        return {
            "type": "respond_from_memory",
            "status": "ready",
            "payload": payload,
        }

    def _learn_if_needed(
        self,
        *,
        caller: str,
        message: Dict[str, Any],
        context: Dict[str, Any],
    ) -> None:
        if not self.memory:
            return
        if caller != "summary":
            return
        if message.get("type") != "response":
            return

        question = self._extract_last_user_message(context)
        answer = self._format_answer(message.get("content"))
        if not question or not answer:
            return

        metadata = self._extract_metadata(context)
        self.memory.store(question, answer, metadata)

    def _extract_question(self, message: Dict[str, Any], context: Dict[str, Any]) -> str:
        content = message.get("content")
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            return "\n".join(str(item) for item in content)
        if isinstance(content, dict):
            return json.dumps(content, ensure_ascii=False)
        history_question = self._extract_last_user_message(context)
        return history_question or ""

    def _extract_last_user_message(self, context: Dict[str, Any]) -> str:
        history = context.get("history") or []
        for item in reversed(history):
            if item.get("speaker") == "user":
                content = item.get("content")
                if isinstance(content, str):
                    return content
                if isinstance(content, list):
                    return "\n".join(str(value) for value in content)
                if isinstance(content, dict):
                    return json.dumps(content, ensure_ascii=False)
        return ""

    def _extract_metadata(self, context: Dict[str, Any]) -> Dict[str, Any]:
        user = context.get("user") or {}
        project = user.get("project") or context.get("project")
        phase = user.get("phase") or context.get("phase")
        roles = user.get("roles") or context.get("roles")
        return {
            "project": project,
            "phase": phase,
            "roles": roles,
        }

    def _format_answer(self, content: Any) -> str:
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            return "\n".join(str(item) for item in content)
        if isinstance(content, dict):
            return json.dumps(content, ensure_ascii=False)
        return ""

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
