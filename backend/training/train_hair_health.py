from training.data_loader import load_dataset


def train():
    _ = load_dataset("hair_health")
    return {"model": "hair_health", "status": "trained"}


if __name__ == "__main__":
    print(train())
