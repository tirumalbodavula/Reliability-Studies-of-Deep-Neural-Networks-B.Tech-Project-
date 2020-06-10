In configuration folder we have config.py is a custom configuration file will help us manage our dataset, class names, and paths.
It is written in Python directly so that we can use os.path  to build OS-specific formatted file paths directly in the script.

build_dataset.py : Using the configuration, this script will  create an organized dataset on disk, making it easy to extract features from.

extract_features.py : This script uses transfer learning technique via feature extraction.
This Python script will compute feature vectors for each image, storing the results in a .csv  file. 
The label encoder .cpickle  file will also be output via this script.

From there we use train.py, where our training script will train a model on top of the previously computed features.
 We will evaluate and save the resulting model as a .cpickle .

Order for running the python scripts
config.py ==> build_dataset.py ==> extract_features.py ==> train.py
