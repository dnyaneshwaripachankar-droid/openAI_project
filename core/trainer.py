import torch
from utils.logger import setup_custom_logger
from utils import validate_config

class OpenEnvTrainer:
    def __init__(self, config):
        self.config = config
        self.logger, self.writer = setup_custom_logger()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.logger.info(f"Training initialized on {self.device}")

    def save_checkpoint(self, state, epoch):
        path = f"data/raw/checkpoint_ep_{epoch}.pth"
        torch.save(state, path)
        self.logger.info(f"Saved checkpoint to {path}")

    def train(self, epochs):
        for epoch in range(epochs):
            # --- Dummy Training Logic ---
            loss = 1.0 / (epoch + 1) # Example metric
            
            # Log to TensorBoard
            self.writer.add_scalar("Loss/train", loss, epoch)
            
            if epoch % 10 == 0:
                self.logger.info(f"Epoch {epoch}: Loss = {loss:.4f}")
                self.save_checkpoint({"epoch": epoch, "loss": loss}, epoch)

if __name__ == "__main__":
    conf = {"lr": 0.001, "batch_size": 32}
    trainer = OpenEnvTrainer(conf)
    trainer.train(100)