import sys
from utils import get_english_tokenizer
from datasets import CBOWDataset
from datasets import SkipGramDataset
from torch.utils.data import random_split
import torch
from torch.utils.data import DataLoader
from models import CBOW_Model
from models import SkipGram_Model
from utils import get_lr_scheduler
from torch import nn
from torch.optim import Adam
from trainer import Trainer
from utils import save_vocab
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--model-name', default='word2vec', type=str, help='name of the model')
parser.add_argument('--data-path', default='./data', type=str, help='data path')
parser.add_argument('--save-path', default='./output', type=str, help='save path')
parser.add_argument('--window', default=4, type=int, help='window size for CBOW/SkipGram')
parser.add_argument('--min-word-frequency', default=50, type=int, help='minimum word frequency to build vocab')
parser.add_argument('--val-ratio', default=0.001, type=float, help='ratio of train data to use for validation')
parser.add_argument('--train-batch-size', default=256, type=int, help='training batch size')
parser.add_argument('--val-batch-size', default=256, type=int, help='validation batch size')
parser.add_argument('--epochs', default=50, type=int, help='total epochs to train the model')
parser.add_argument('--lr', default=0.025, type=float, help='learning rate')
parser.add_argument('--arch', default='cbow', type=str, help='Select model architecture - cbow for CBOW and skip for SkipGram') 

def main():
    args = parser.parse_args()  
    
    dataset = CBOWDataset(root_dir = args.data_path,tokenizer = get_english_tokenizer(), window = args.window, min_word_frequency = args.min_word_frequency) if args.arch == "cbow" else SkipGramDataset(root_dir = args.data_path,tokenizer = get_english_tokenizer(), window = args.window, min_word_frequency = args.min_word_frequency)   
    
    vocab_size = len(dataset.vocab.get_stoi())
    print(f"Vocabulary size: {vocab_size}")
    val_size = int(args.val_ratio * len(dataset))
    train_size = len(dataset)-val_size

    train_dataset,val_dataset = random_split(dataset,[train_size,val_size])

    train_loader = DataLoader(
            train_dataset,
            batch_size=args.train_batch_size,
            shuffle=True,
            drop_last = True
        )
    val_loader = DataLoader(
            val_dataset,
            batch_size=args.val_batch_size,
            shuffle=False,
            drop_last = False
        )

    
    model = CBOW_Model(vocab_size=vocab_size) if args.arch == "cbow" else SkipGram_Model(vocab_size=vocab_size)
    criterion = nn.CrossEntropyLoss()

    optimizer = Adam(model.parameters(), lr=args.lr)
    lr_scheduler = get_lr_scheduler(optimizer, args.epochs, verbose=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)


    trainer = Trainer(
        model=model,
        epochs=args.epochs,
        train_dataloader=train_loader,
        train_steps = None,
        val_dataloader=val_loader,
        val_steps = None,
        criterion=criterion,
        optimizer=optimizer,
        checkpoint_frequency = None,
        lr_scheduler=lr_scheduler,
        device=device,
        model_dir=args.save_path,
        model_name=args.model_name,
    )

    trainer.train()
    print("Training finished.")

    trainer.save_model()
    trainer.save_loss()
    save_vocab(dataset.vocab, args.save_path)
    print("Model artifacts saved to folder:", args.save_path)
    

if __name__ == '__main__':
    main()
