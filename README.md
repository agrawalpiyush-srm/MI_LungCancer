# MI_LungCancer
This project aims to characterize the Bidirectional Molecular Signatures Associating Myocardial Infarction and Lung Cancer

We used publically available datasets from the GEO and TCGA for our studies. We used 'limma' package to get the DEGs. Post DEGs charcterization, we perfromed multiple
analysis such as Gene Ontology, KEGG pathway analysis, miRNA-mRNA target analysis.

We also perfromed survival association of the selected DEGs in TCGA-LUAD and TCGA-LUSC datasets. 

Drug repurposing analysis, using FDA-approved drugs was done to find new drugs against the new therapeutic targets.

# Machine Learning Model Development

We also developed 2 different machine learning models, Support Vector Machine (SVM) and Random Forest (RF) using gene expression as features of the selected target genes
to classify MI patients from non-MI patients.

Models are provided in the "ML_model" folder and instructions for usage is given in the README file.

Code usage: python predict.py

# Code Availability

All the codes and input files have been provided in the "codes" folder for the public usage.
