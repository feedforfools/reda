"""pytest configuration: add project root to sys.path."""

import sys
from pathlib import Path

# Ensure the project root (parent of tests/) is on sys.path so all modules resolve.
sys.path.insert(0, str(Path(__file__).parent.parent))
