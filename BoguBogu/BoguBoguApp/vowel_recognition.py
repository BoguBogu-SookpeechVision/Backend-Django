from imutils import face_utils
import imutils
import dlib
import cv2
import joblib
import pandas as pd


class GetLandmarks:

    # initialize dlib's frontal_face_detector and shape_predictor with the pre-trained dat file
    def __init__(self, image_path, face_predictor):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(face_predictor)
        self.image_path = image_path

    def get_landmarks(self):
        # load the image, resize it, and convert it to grayscale
        image = cv2.imread(self.image_path)
        image = imutils.resize(image, width=1000)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # detect faces in the grayscale image
        rects = self.detector(gray, 1)

        dots = list(range(68))
        landmarks = {}
        # loop over the face detections
        for (i, rect) in enumerate(rects):
            # determine the facial landmarks for the face region,
            # then convert the facial landmark (x, y)-coordinates to a NumPy
            shape = self.predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # loop over the (x, y) coordinates for facial landmarks and append them to landmarks(dict)
            for (x, y) in shape:
                landmarks[dots[i]] = [x, y]

                i += 1

        return landmarks


class Calculate:

    def __init__(self, image_path, face_predictor):
        self.cal_result = {'m_width': {}, 'm_height': {}, 'upper_lip': {}, 'lower_lip': {},
                           'cheek_chin': {}, 'cheek_cheek': {}}

        self.landmark_coords = GetLandmarks(image_path, face_predictor).get_landmarks()

    # calculate distances between certain landmarks
    def calculate(self):
        # width and height of lips
        m_width = self.landmark_coords[54][0] - self.landmark_coords[48][0]
        m_height = self.landmark_coords[57][1] - self.landmark_coords[51][1]

        # thickness of upper and lower lip
        upper_lip = self.landmark_coords[62][1] - self.landmark_coords[51][1]
        lower_lip = self.landmark_coords[57][1] - self.landmark_coords[66][1]

        # distance between the cheek and chin
        cheek_chin = self.landmark_coords[8][1] - self.landmark_coords[2][1]

        # distance between right and left cheek
        cheek_cheek = self.landmark_coords[14][0] - self.landmark_coords[2][0]

        self.cal_result['m_width'][0] = m_width
        self.cal_result['m_height'][0] = m_height
        self.cal_result['upper_lip'][0] = upper_lip
        self.cal_result['lower_lip'][0] = lower_lip
        self.cal_result['cheek_chin'][0] = cheek_chin
        self.cal_result['cheek_cheek'][0] = cheek_cheek

        return self.cal_result


class PredictLip:
    def __init__(self, image_path, face_predictor, model_path):

        calc_results = Calculate(image_path, face_predictor).calculate()
        self.model_path = model_path

        # convert calculated results into a Pandas DataFrame
        self.df = pd.DataFrame(calc_results)
        self._X_data = self.df.iloc[:, :]
        self._prediction = None

    def predict(self):
        # predict lip shape using the pre-trained pickle model
        model = joblib.load(self.model_path)
        self._prediction = model.predict(self._X_data)

        return self._prediction


