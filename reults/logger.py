import logging
from torch.utils.tensorboard import SummaryWriter
import os

def setup_custom_logger(log_dir="results/logs"):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 1. Standard Terminal Logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(f"{log_dir}/session.log"),
            logging.StreamHandler()
        ]
    )
    
    # 2. TensorBoard Writer
    writer = SummaryWriter(log_dir=log_dir)
    
    return logging.getLogger("OpenEnv"), writer