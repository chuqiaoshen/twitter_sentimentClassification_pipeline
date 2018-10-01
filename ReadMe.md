### TextProcessing Sentiment + Classification
* CatherineS 20180831with model self trained from twitter140 datasets
* Reconstruct version with processes reconstructed
* this version can be used to modify the rest of the info and run 4 kernels or any given number simultaneously


### what you need to edit
1. edit the inputParameters.py about the input folder you want

### Run in the terminal
1. open the terminal and cd to the directory of this folder
2. source activate python3 environment
3. pip install spacy
4. python -m spacy download en
5. pip install -r requirements.txt
6. run the runme.py file by: python runme.py

##### attention:
* for spacy, if not successfully install, please use this in terminal: pip install -U spacy

* if you want to split the processing,please run the findRemain.py first to get the remains, and then run runme_01 ....seperately on different kernels
