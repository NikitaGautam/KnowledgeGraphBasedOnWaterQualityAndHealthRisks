
## : Original Datasets are not included due to UMLS license agreement (distribution of datasets not permitted). However, we have included the steps using which you can extract the data from UMLS. 

### Steps for extracting the triples data from UMLS
```
1. Got to [UMLS Webpage](https://uts.nlm.nih.gov/uts/) and Sign Up.

2. Once you successfully login, you will have access to the SemRep/SemMedDB/SKR Resources. 

3. Go to Semantic MEDLINE Database (SemMedDB) option.

4. Go to Download SemMedDB Database.

5. Download the PREDICATION (CSV or MySQL). 

6. Filter the concepts relevant to the domain using the downloaded file and extract triples.

7. Use the scripts in the scripts folder to process the data for preprocessing and dataset creation. 

8. Fine-tune the BERT or RoBERTa models with the dataset for Knowledge Graph Completion Tasks (Triple Classification, Relation Prediction and Link Prediction). 



```


