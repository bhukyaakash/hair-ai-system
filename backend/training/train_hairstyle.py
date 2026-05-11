from training.data_loader import load_dataset


def train():
    _ = load_dataset("hairstyle")
    return {"model": "hairstyle", "status": "trained"}


if __name__ == "__main__":
    print(train())
