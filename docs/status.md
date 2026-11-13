# Status

## Project: NER (Named Entity Recognition)

**Type:** Live document — this file is a live record of the project's state and is updated every time its content changes.

### Current State
- **Goal:** Train an AI model to perform Named Entity Recognition (NER) using `bert-base-uncased`.
- **Model chosen:** `bert-base-uncased` from Hugging Face `transformers`.
- **Plan:** `docs/Plan.md` outlines the training approach, data requirements, and environment setup.
- **Config:** `src/config.py` defines directory paths (`models`, `data`, `logs`, `cache`).
- **Requirements:** `requirements.txt` / `pyproject.toml` list dependencies; `tokenizers==0.23.3`, `transformers==5.22.2`, etc.
- **Environment:** CPU/GPU via `environment_cpu.yml` or `environment_gpu.yml`; install with `pip install -r requirements.txt`.

### What This Document Is
A live status/log document that tracks the current project state and is updated on every change so it always reflects the latest situation.
