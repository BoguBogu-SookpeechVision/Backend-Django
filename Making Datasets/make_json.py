# import the necessary packages
import os

from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import json
import time


# get dlib's frontal_face_detector and initialize shape_predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('full_face_predictor.dat')

# get file names from directory
all_files = os.listdir('./path/to/image/files')

for j in range(len(all_files)):
	# load the input image, resize it, and convert it to grayscale
	image = cv2.imread(f'./path/to/image/files{all_files[j]}')
	image = imutils.resize(image, width=1000)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# detect faces in the grayscale image
	rects = detector(gray, 1)

	dots = list(range(0, 68))
	landmarks = {}
	# loop over the face detections
	for (i, rect) in enumerate(rects):
		# determine the facial landmarks for the face region,
		# then convert the facial landmark (x, y)-coordinates to a NumPy
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		# loop over the (x, y) coordinates for facial landmarks and append them to landmarks(dict)
		for (x, y) in shape:
			landmarks[dots[i]] = [x, y]

			i += 1

	# encoder for json since json does not recognize NumPy data types
	# source: https://stackoverflow.com/a/57915246
	class NpEncoder(json.JSONEncoder):
		def default(self, obj):
			if isinstance(obj, np.integer):
				return int(obj)
			elif isinstance(obj, np.floating):
				return float(obj)
			elif isinstance(obj, np.ndarray):
				return obj.tolist()
			else:
				return super(NpEncoder, self).default(obj)

	# dump coordinates into a json file
	with open(f'/path/to/file/file.json', 'w') as f:
		json.dump(landmarks, f, ensure_ascii=False, indent="\t", cls=NpEncoder)
