# Leveraging Existing Literature on the Web and Deep Neural Models to Build a Knowledge Graph Focused on Water Quality and Health Risks

The repository contains these scripts:

1. A set of URLs included in the domain-specific corpus and web crawler scripts to extract data from the Web Of Science.

2. Scripts to create knowledge graph completion (KGC) tasks based on triples data from SemMedDB and SemRep, which requires [UMLS Metathesaurus License Agreement](https://lhncbc.nlm.nih.gov/ii/tools/SemRep_SemMedDB_SKR.html). 
 
3.  Modified scripts from [KG-BERT](https://github.com/yao8839836/kg-bert#readme) for fine-tuning BERT and RoBERTa models on KGC tasks.

4. Modified scripts from [OPEN-KE](https://github.com/thunlp/OpenKE) to run the baseline models on our dataset.

All scripts are tested on Python 3.5+.
