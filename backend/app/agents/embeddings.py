from __future__ import annotations

import os
from functools import lru_cache
from typing import List

from openai import OpenAI

DEFAULT_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")


@lru_cache(maxsize=1)
def _client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set.")
    return OpenAI(api_key=api_key)


def get_embedding(text: str) -> List[float]:
    """Return the embedding vector for the provided text."""
    client = _client()
    response = client.embeddings.create(model=DEFAULT_EMBEDDING_MODEL, input=[text])
    return response.data[0].embedding
