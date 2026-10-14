"""Demo for Oceanography Flashcard Tutor."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import oceanography_tutor

print("Oceanography Flashcard Tutor", "v" + oceanography_tutor.__version__)
print("modules:", [m for m in dir(oceanography_tutor) if not m.startswith('_')])
