from training.data_loader import load_dataset


def train():
    _ = load_dataset("disease")
    return {"model": "disease_detector", "status": "trained"}


if __name__ == "__main__":
    print(train())
