import os
import glob
import numpy as np
import torch

def process_raw_data(raw_dir='data/raw', processed_dir='data/processed'):
    """
    Combines raw rollout .npy or .pth files into a single processed buffer.
    """
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    files = glob.glob(os.path.join(raw_dir, "*.pth"))
    all_data = []

    for f in files:
        checkpoint = torch.load(f)
        # Extract transitions (state, action, reward)
        all_data.append(checkpoint)

    if all_data:
        processed_path = os.path.join(processed_dir, "buffer_latest.pth")
        torch.save(all_data, processed_path)
        print(f"✅ Processed {len(all_data)} rollouts into {processed_path}")
    else:
        print("⚠️ No raw data found to process.")

if __name__ == "__main__":
    process_raw_data()