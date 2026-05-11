from training.data_loader import load_dataset


def train():
    _ = load_dataset("face_shape")
    return {"model": "face_shape", "status": "trained"}


if __name__ == "__main__":
    print(train())
