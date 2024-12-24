
from os.path import join
import argparse

from PIL import Image
from torchvision import transforms
import torch

import os


def preprocess(data_dir, split):
    assert split in ["test"]

    images_dir = join(data_dir, "imgs")
    pairs = []

    transform = transforms.ToTensor()

    new_height = 45

    for img_name in os.listdir(images_dir):
        img_path = join(images_dir, img_name)
        img = Image.open(img_path)
        img = img.convert('RGB')

        x, y = img.size

        # resize the image to 32*h'
        if y > new_height:
            new_x = int(x * new_height / y)
            img = img.resize((new_x, new_height), Image.Resampling.LANCZOS)
            # img.show()

        img_tensor = transform(img)

        pairs.append((img_tensor, img_name)) # formula placeholder, otherwise error could happen
    pairs.sort(key=img_size)

    print(len(pairs))

    # print(pairs[-2])

    out_file = join(data_dir, "{}.pkl".format(split))
    torch.save(pairs, out_file)
    print("Save {} dataset to {}".format(split, out_file))


def img_size(pair):
    img, formula = pair
    return tuple(img.size())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Im2Latex Data Preprocess Program")
    parser.add_argument("--data_path", type=str,
                        default="./real/", help="The dataset's dir")
    args = parser.parse_args()

    preprocess(args.data_path, 'test')
