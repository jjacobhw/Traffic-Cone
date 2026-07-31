# Traffic Cone: An Inference-Time Compute Benchmark for LLM Reasoning and Planning With Guardrails and Permissions

## Motivation:
Prior research suggests that large language models (LLMs) cannot reliably evaluate the correctness of their own intermediate reasoning steps. This limitation may become increasingly consequential as inference-time search grows deeper. Typically seen in common-sense reasoning tasks, extended reasoning can improve performance on difficult problems by allowing a model to generate, compare, and refine multiple candidate solutions, but it can also cause the context window to accumulate redundant and irrelevant information, including abandoned branches, incorrect hypotheses, superseded intermediate results, and other forms of garbage data.

This can create context pollution that dilutes attention to task-relevant information and degrades the model’s ability to reason effectively at critical stages, which also impairs its ability to self-verify. As the context window becomes increasingly cluttered, the model becomes more likely to introduce errors and become less capable of identifying and correcting them. Undetected errors can then propagate into subsequent steps, further contaminating the reasoning process and potentially producing a compounding decline in reliability as search depth increases, which can have nasty side effects for users in critical systems.

Despite the growing use of extended inference and search-based reasoning, it remains unclear when accumulated reasoning clutter begins to harm performance, which types of contextual information are most disruptive, and how these effects interfere with self-evaluation. Setting guardrails for these testbenches can help identify when these errors occur and assess the clutter to minimize fallout. 

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

   This unzips `LLMs_Planning.zip`, sets the `VAL`/`PR2` environment variables for the planner tools, and creates/activates the `sys2bench` Conda environment from `sys2bench.yaml`.
