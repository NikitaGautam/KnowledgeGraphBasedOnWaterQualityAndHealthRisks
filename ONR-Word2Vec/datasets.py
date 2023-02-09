from torch.utils.data import Dataset
import os
from unidecode import unidecode
from utils import build_vocab
import torch
class PDFDataset(Dataset):
    """PDF dataset."""

    def __init__(self, root_dir):
        """
        Args:
            root_dir (string): Directory with all the coverted text files.
            
        """
        self.root_dir = root_dir
        self.filenames = list(filter(
                                lambda file: not file.startswith("._"), #macos adds some meta files, this removes them
                                os.listdir(root_dir)
                                ))

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):
        filename = os.path.join(self.root_dir,self.filenames[idx])
        with open(filename,"r") as f:
            sample = unidecode(" ".join([x.strip() for x in f.readlines()]))
        return sample
    
class CBOWDataset(Dataset):
    """
    CBOW dataset.
        This dataset uses the PDFDataset and creates context-token pairs
    """

    def __init__(self, root_dir,tokenizer,vocab=None,window: int =4,min_word_frequency: int = 50):
        """
        Args:
            root_dir (string): Directory with all the coverted text files.
            
        """
        self.window = window
        self.pdf_dataset = PDFDataset(root_dir)
        if vocab:
            self.vocab = vocab
        else:
            self.vocab = build_vocab(self.pdf_dataset,tokenizer, min_word_frequency)
        self.text_pipeline = lambda x: self.vocab(tokenizer(x))
        self.data=[]
        self.prepare_data()
        
    def prepare_data(self):
        for text in self.pdf_dataset:
            text_tokens_ids = self.text_pipeline(text)

            if len(text_tokens_ids) < self.window * 2 + 1:
                continue

            for idx in range(len(text_tokens_ids) - self.window * 2):
                token_id_sequence = text_tokens_ids[idx : (idx + self.window * 2 + 1)]
                output = token_id_sequence.pop(self.window)
                input_ = token_id_sequence
                self.data.append([input_,output])

class SkipGramDataset(Dataset):
    """
    SkipGramDataset dataset.
        This dataset uses the PDFDataset and creates context-token pairs
    """

    def __init__(self, root_dir,tokenizer,vocab=None,window: int =4,min_word_frequency: int = 50):
        """
        Args:
            root_dir (string): Directory with all the coverted text files.
            
        """
        self.window = window
        self.pdf_dataset = PDFDataset(root_dir)
        if vocab:
            self.vocab = vocab
        else:
            self.vocab = build_vocab(self.pdf_dataset,tokenizer, min_word_frequency)
        self.text_pipeline = lambda x: self.vocab(tokenizer(x))
        self.data=[]
        self.prepare_data()
        
    def prepare_data(self):
        for text in self.pdf_dataset:
            text_tokens_ids = self.text_pipeline(text)

            if len(text_tokens_ids) < self.window * 2 + 1:
                continue

            for idx in range(len(text_tokens_ids) - self.window * 2):
                token_id_sequence = text_tokens_ids[idx : (idx + self.window * 2 + 1)]
                input_ = token_id_sequence.pop(self.window)
                outputs = token_id_sequence

                for output in outputs:
                    self.data.append([input_, output])


    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        context,token = self.data[idx]
        return (torch.tensor(context,dtype=torch.long),token)