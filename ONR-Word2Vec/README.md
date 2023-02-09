
## Usage:
```
Using cbow:

python train.py --model-name=word2vec --data-path=./data --save-path=./output --window=4 --min-word-frequency=50 --train-batch-size=256 --val-batch-size=256 --lr=0.025 --epochs=50 --arch=cbow

Using skipgram:

python train.py --model-name=word2vec --data-path=./data --save-path=./output --window=4 --min-word-frequency=50 --train-batch-size=256 --val-batch-size=256 --lr=0.025 --epochs=50 --arch=skip


```
### Notebooks:
 ```data_utils.ipynb``` and ```train.ipynb``` are test scripts and can be disregarded
 ```inference.ipynb``` contains the script to render 3D scatter plot of some keywords extracted from ontology

