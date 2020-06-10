imagenet-A is the folder having imagenet-A classes which contains pertubed images
https://drive.google.com/file/d/12G7NxzcHP2CMCmWvSyvjK17LvOojQ3I3/view?usp=sharing

In configuration folder we have config.py which contains our configuration settings.
Other python scripts in this folder will make use of this config.py file.

Using our build_dataset.py script, we will organize and output the contents of the
IN_and_INA_RESNET/ directory to the dataset folder.

From there, the extract_features.py script will use transfer learning via feature extraction to compute feature vectors for each image.
These features will be output to a CSV file.

From there we use train.py, we will use incremental learning to train a simple neural network on the extracted features.

Order for running the python scripts
config.py ==> build_dataset.py ==> extract_features.py ==> train.py