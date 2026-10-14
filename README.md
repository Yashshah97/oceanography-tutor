# Oceanography Flashcard Tutor

This oceanography flashcard tutor is designed to help students of marine science master key concepts through interactive repetition and review. With a focus on tide, current, and salinity data, it's the perfect tool for anyone looking to deepen their understanding of these critical aspects of oceanography. Built from the ground up in pure Python, this project prioritizes clarity and maintainability.

## What makes it unique

Combines tide, current, and salinity data with a spaced-repetition trainer with progress tracking — a niche where few ready-made tools exist.

## Features

- **`oceanography_tutor/flashcard.py`** — Flashcard model and operations
- **`oceanography_tutor/tutor.py`** — Spaced repetition trainer logic
- **`oceanography_tutor/tracker.py`** — Progress tracking and storage
- **`oceanography_tutor/data.py`** — Tide, current, and salinity data models and access
- **`oceanography_tutor/cli.py`** — Command-line interface for tutor and tracker
- **`oceanography_tutor/tests.py`** — Unit tests for the entire application

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/oceanography-tutor.git
cd oceanography-tutor

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
oceanography-tutor/
├── oceanography_tutor/
│   ├── flashcard.py
│   ├── tutor.py
│   ├── tracker.py
│   ├── data.py
│   ├── cli.py
│   ├── tests.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **oceanography** · Archetype: **tutor** ·
Built autonomously by JARVIS on 2026-10-13. MIT licensed.
