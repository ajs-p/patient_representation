# patient_representation
Based off of this paper:

https://arxiv.org/pdf/1805.02096.pdf

This repo relies on data sources that are not publicly accessible.  

You will need to meet the requirements from the originating providers in order to download them:

* MIMICIII: https://mimic.mit.edu/
* i2b2 obesity challenge: https://www.i2b2.org/NLP/DataSets/Main.php
* UMLS Metathesaurus: https://www.nlm.nih.gov/research/umls/index.html

A few NLP options that can be used in accordance with this repo:
* https://ctakes.apache.org/
* https://www.nlm.nih.gov/research/umls/implementation_resources/metamap.html
* https://www.johnsnowlabs.com/spark-nlp-health/

To run the project, execute these files in order:
* code/notebooks/prepare_for_nlp
* code/colab/spark_nlp
* code/notebooks/prepare_for_nn
* code/colab/mlp
* code/notebooks/prepare_for_svm
* code/colab/svm

Also of interest:
* code/notebooks/eda

Directory structure:
* code
*    ...
* data
* --clinical_vocab - UMLS metathesaurus
* --consumed - output of code
* --ctakes_in - for use with cTAKES
* --ctakes_in_complete - for use with cTAKES
* --ctakes_out - for use with cTAKES
* --ctakes_out_complete - for use with cTAKES
* --i2b2 - data for SVMs
* --nlp_jsl - Spark NLP output
* --nlp_raw - MetaMap output
* profiling - data profiling output
