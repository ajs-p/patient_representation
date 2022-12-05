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

To run the project, see these steps:
## NLP
Prepare MIMICIII data for NLP:
* code/notebooks/prepare_for_nlp

Prepare i2b2 data for NLP:
* code/notebooks/prepare_xml_for_modeling

If using MetaMap and AWS Lambda, see:
* code/lambda/get_metamap_response
* code/lambda/send_nlp_files

If using Spark NLP, see:
* code/colab/spark_nlp

Recommended to adapt the above for use in a distributed Spark environment.

If using cTAKES, that will do the work once you provide the input data.

## Train patient representations
Prepare for training:
* code/notebooks/prepare_for_nn

Run MLP to train on MIMICIII data:
* code/colab/mlp


## Use dense patient vectors for classification
Train i2b2 data and extract patient activations from the hidden layer:
* code/colab/mlp

Train classifiers:
* code/notebooks/svm

## Also of interest
* code/notebooks/eda

## Directory structure
* code
*    ...
* data
* --clinical_vocab - UMLS metathesaurus
* --consumed - output of code
* ...
* profiling - data profiling output
