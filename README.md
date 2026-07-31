# Traffic Cone
Inference-Time Compute for LLM Reasoning and Planning: Guardrails and Permissions for Benchmark and Insights

## Setup

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Downloading Hugging Face datasets

Datasets are downloaded on demand with [datasets/load_hf.py](datasets/load_hf.py). Downloaded data is saved under `datasets/` and is git-ignored, so each device needs to fetch it independently.

```bash
python datasets/load_hf.py <hf_dataset_id> [config_name] [--split SPLIT]
```

Examples:

```bash
python datasets/load_hf.py tau/commonsense_qa
python datasets/load_hf.py piqa --split train
```

This saves the dataset to `datasets/<hf_dataset_id with "/" replaced by "__">/` (e.g. `datasets/tau__commonsense_qa/`) and caches raw downloads under `datasets/cache/`.

Optional: set an `HF_TOKEN` environment variable to avoid unauthenticated Hub rate limits:

```bash
export HF_TOKEN=<your_huggingface_token>
```

## Retrieving the Sys2Bench dataset

[Sys2Bench](https://github.com/divelab/Sys2Bench) lives under `datasets/Sys2Bench` as its own git clone (it is git-ignored in this repo, so it isn't fetched automatically when you clone Traffic-Cone).

1. Clone it into `datasets/`:

   ```bash
   git clone git@github.com:divelab/Sys2Bench.git datasets/Sys2Bench
   ```

   This pulls in `datasets/Sys2Bench/data/`, which already contains the benchmark data (game24, strategyqa, cube, binpacking, hotpotQA, aqua, tripplan, calendarplan, blocksworld, prontoqa).

2. (Optional) If you need the full Sys2Bench toolchain — planning tools and its Conda environment — run its setup script from inside that directory:

   ```bash
   cd datasets/Sys2Bench
   ./setup.sh
   ```

   This unzips `LLMs_Planning.zip`, sets the `VAL`/`PR2` environment variables for the planner tools, and creates/activates the `sys2bench` Conda environment from `sys2bench.yaml`. See [datasets/Sys2Bench/README.md](datasets/Sys2Bench/README.md) for details.
