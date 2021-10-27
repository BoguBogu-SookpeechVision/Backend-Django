import multiprocessing
import argparse
import dlib

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--training", required=True,
                help="path to input training XML file")
ap.add_argument("-m", "--model", required=True,
                help="path serialized dlib shape predictor model")
args = vars(ap.parse_args())

# grab the default options for dlib's shape predictor
print("[INFO] setting shape predictor options...")
options = dlib.shape_predictor_training_options()

# define the depth of each regression tree
options.tree_depth = 6

# regularization parameter in the range [0, 1]
options.nu = 0.1

# the number of cascades used to train the shape predictor
options.cascade_depth = 15

# number of pixels used to generate features for the random trees at each cascade
options.feature_pool_size = 400

# selects best features at each cascade when training
options.num_test_splits = 55

# controls amount of "jitter" (i.e., data augmentation)
options.oversampling_amount = 5

# amount of translation jitter to apply
options.oversampling_translation_jitter = 0.1

# tell the dlib shape predictor to be verbose and print out status messages our model trains
options.be_verbose = True

# number of threads/CPU cores to be used when training
options.num_threads = multiprocessing.cpu_count()

# log our training options to the terminal
print("[INFO] shape predictor options")
print(options)

# train the shape predictor
print("[INFO] training shape predictor...")
dlib.train_shape_predictor(args["training"], args["model"], options)
