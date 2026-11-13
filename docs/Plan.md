# Plan: NER (Named Entity Recognition)

## Goal

Train an AI model to perform **Named Entity Recognition** — i.e., automatically detect and label text with entity type and recognize the entities themselves.

## Model Choice

Use **BERT-base-uncased** (`bert-base-uncased` from Hugging Face `transformers`) as the base model for fine-tuning on a labeled corpus.

## Approach

1. Prepare a labeled dataset of sentences annotated for named entities (e.g., PERSON, ORG, LOC, DATE, etc.).
2. Load `bert-base-uncased` via `transformers`.
3. Fine-tune the model on the NER task using a standard tokenizer pipeline.
4. Evaluate on held-out test data; iterate on hyperparameters or data if accuracy is insufficient.

## Goal Requirements

### Core libraries (from `requirements.txt` / `pyproject.toml`)
- `transformers==5.22.2`
- `tokenizers==0.23.3`
- `huggingface_hub==2.4.0`
- `safetensors==0.8.0`
- `pydantic==2.14.3`, `pydantic-core==2.50.4`
- `torch` (required by BERT models; install separately)
- `accelerate` (optional but recommended for training speed)
- `anyio`, `fastapi`, `starlette` (if serving the trained model later)
- `click`, `typer`, `rich`, `tqdm`, `regex`, `markdown-it-py`, `mdurl`, `idna`, `PyYAML`, `opentelemetry-api`, `truststore`, `shellingham`, `setuptools`, `wheel`

### Data & utilities
- A corpus of raw text + ground-truth entity annotations (JSONL/CSV).
- Optional: `annotated-doc`, `annotated-types`, `h11`, `hf-xet`, `httpcore2`, `httpx2` for data handling.

### Environment setup
```bash
# CPU
conda create -f environment_cpu.yml   # or uv init && uv sync
# GPU
conda create -f environment_gpu.yml  # or uv init && uv sync
pip install -r requirements.txt
```

## Notes

- This plan focuses on the *training* phase; serving can be added later with FastAPI/FastStarlette.
- The existing `main.py` currently prints "Hello from ner!" — it will be replaced once the model is ready.
