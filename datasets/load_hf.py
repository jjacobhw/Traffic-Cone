"""Download a Hugging Face dataset into datasets/cache/ and datasets/<name>/.

Usage:
    python datasets/load_hf.py <hf_dataset_id> [config_name] [--split SPLIT]

Example:
    python datasets/load_hf.py tau/commonsense_qa
    python datasets/load_hf.py piqa --split train
"""

import argparse
from pathlib import Path

from datasets import load_dataset

DATASETS_DIR = Path(__file__).parent
CACHE_DIR = DATASETS_DIR / "cache"


def load_hf_dataset(dataset_id: str, config_name: str | None = None, split: str | None = None):
    """Load a dataset from the Hugging Face Hub and save it locally as Arrow files."""
    dataset = load_dataset(dataset_id, config_name, split=split, cache_dir=str(CACHE_DIR))

    local_name = dataset_id.replace("/", "__")
    out_dir = DATASETS_DIR / local_name
    if config_name:
        out_dir = out_dir / config_name
    out_dir.mkdir(parents=True, exist_ok=True)

    dataset.save_to_disk(str(out_dir))
    print(f"Saved '{dataset_id}' to {out_dir}")
    return dataset


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_id", help="HF dataset id, e.g. tau/commonsense_qa")
    parser.add_argument("config_name", nargs="?", default=None, help="Optional dataset config/subset name")
    parser.add_argument("--split", default=None, help="Optional split, e.g. train/validation/test")
    args = parser.parse_args()

    load_hf_dataset(args.dataset_id, args.config_name, args.split)
