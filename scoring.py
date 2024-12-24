# load checkpoint and evaluating
from os.path import join
from functools import partial
import argparse

import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

from data import Im2LatexDataset
from build_vocab import Vocab, load_vocab
from utils import collate_fn
from model import LatexProducer, Im2LatexModel
from model.score import score_files


def main():
    score = score_files('./results/result.txt', './results/ref.txt')
    print("beam search result:", score)


if __name__ == "__main__":
    main()
