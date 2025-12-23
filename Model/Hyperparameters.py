from dataclasses import dataclass
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv("Model.env")

@dataclass
class Hyperparameters:
    node_count: int=int(os.getenv("NODE_COUNT",64))
    link_state_dim:int=int(os.getenv("LINK_STATE_DIM",4))
    path_state_dim:int=int(os.getenv("PATH_STATE_DIM",2))
    learning_rate: float= float(os.getenv("LEARNING_RATE",0.01))
    readout_unit: int=int(os.getenv("READOUT_UNITS",8))
    T: int=int(os.getenv("T",3))
    batch_size: int=int(os.getenv("BATCH_SIZE",32))
    dropout_rate: float=float(os.getenv("DROPOUT_RATE",0.5))
    l2: float=float(os.getenv("L2",0.1))
    l2_2: float=float(os.getenv("L2_2",0.01))
    learn_embedding: bool=bool(int(os.getenv("LEARN_EMBEDDING",True)))
    readout_layers: int=int(os.getenv("READOUT_LAYERS",2))

def print_hyperparameters():
    print("Hyperparameters:")
    hparams=Hyperparameters()
    print(f"Learning Rate: {hparams.learning_rate}")
    
if __name__ == "__main__":
    print_hyperparameters()
