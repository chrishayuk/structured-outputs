# Introduction
This is a small test harness that is used to demonstrate how to use structured outputs with openai and Ollama.

In this case, we ask the model to verify if a sudoku puzzle is a valid grid.

## Ollama
For Ollama (default provider), using default model ("phi4"):

```bash
uv run sudoku.py
```

For Ollama specifying model explicitly:

```bash
uv run sudoku.py --model-provider=ollama --model=phi4
```

## OpenAI
For OpenAI with default model ("gpt-4o-mini"):

```bash
uv run sudoku.py --model-provider=openai
```

For OpenAI specifying a different model (e.g. "gpt-4o"):
python sudoku.py 

```bash
uv run sudoku.py --model-provider=openai --model=gpt-4o
```