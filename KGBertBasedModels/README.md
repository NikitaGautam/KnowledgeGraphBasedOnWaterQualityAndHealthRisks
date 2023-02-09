#The following code has been adapted from [KG-BERT](https://github.com/yao8839836/kg-bert)

## Installing required packages

```bash
pip install -r requirements.txt
```

## Data

1. The knowledge graph datasets are present in ./data folder. 

2. ./data/for-rel contains datasets for relation prediction.

3. ./data/for-triple contains datasets for triple classification.

4. ./data/filtered contains datasets for relation prediction but with filtered relations with a certain threshold value.

 5. entity2text.txt contains entity textual sequences relation2text.txt contains relation textual sequences.


### 1. Triple Classification


#### for-triple


BERT 

```shell
python run_bert_triple_classifier.py --task_name kg --do_train --do_eval --do_predict --data_dir ./data/for-triple --bert_model bert-base-uncased --max_seq_length 20 --train_batch_size 32 --learning_rate 5e-5 --num_train_epochs 5.0 --output_dir ./output-triple1/ --gradient_accumulation_steps 1 --eval_batch_size 512
```

Fine-tuned BERT using domain-specific corpus

```shell
python run_bert_triple_classifier.py --task_name kg --do_train --do_eval --do_predict --data_dir ./data/for-triple --bert_model ../Checkpoints/checkpoint-bert --max_seq_length 20 --train_batch_size 32 --learning_rate 5e-5 --num_train_epochs 3.0 --output_dir ./output_triple2/ --gradient_accumulation_steps 1 --eval_batch_size 512
```

RoBERTa

```shell
python run_roberta_triple_classification.py --task_name kg --do_train --do_eval --do_predict --data_dir ./data/for-triple --roberta_model roberta-base --max_seq_length 200 --train_batch_size 32 --learning_rate 5e-5 --num_train_epochs 5.0 --output_dir ./output-triple3/ --gradient_accumulation_steps 1 --eval_batch_size 512
```

Fine-tuned RoBERTa using domain-specific corpus

```shell
python run_roberta_triple_classification.py --task_name kg --do_train --do_eval --do_predict --data_dir ./data/for-triple --roberta_model ../Checkpoints/checkpoint-roberta  --max_seq_length 200 --train_batch_size 32 --learning_rate 5e-5 --num_train_epochs 5.0 --output_dir ./output-triple4/ --gradient_accumulation_steps 1 --eval_batch_size 512
```

### 1. Relation Prediction

#### for-rel / filtered

```shell
python3 run_bert_relation_prediction.py --task_name kg --do_train --do_eval --do_predict --data_dir ./data/filtered --bert_model bert-base-cased --max_seq_length 25 --train_batch_size 32 --learning_rate 5e-5 --num_train_epochs 20.0 --output_dir ./output_rel1/ --gradient_accumulation_steps 1 --eval_batch_size 512
```


Commands for relation prediction using fine-tuned BERT, RoBERTa and fine-tuned RoBERTa are similar to the ones mentioned in the triple classification above. 








