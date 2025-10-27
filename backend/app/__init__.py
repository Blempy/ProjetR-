"""Backend FastAPI application package.

Ensures the project root is on ``sys.path`` so that shared modules
(ex. ``automation``) can be imported by the API code.
"""

from __future__ import annotations

import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))
