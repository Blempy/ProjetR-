# -*- coding: utf-8 -*-
"""Shared helpers for automation tooling."""

from __future__ import annotations

import re


def slugify(value: str, fallback: str = "element") -> str:
    """Return a filesystem-friendly slug."""
    value = value.lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.ASCII)
    value = re.sub(r"[-\s]+", "-", value, flags=re.ASCII).strip("-")
    return value or fallback
