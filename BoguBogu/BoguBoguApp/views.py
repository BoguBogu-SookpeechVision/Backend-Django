from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render
from .vowel_recognition import PredictLip
import os
import csv


def vowel_recognition(request):
    global result

    if request.method == "POST":

        # get key and read image from POST request
        get_key = list(request.FILES.items())
        key = get_key[0][0]

        file = request.FILES[key]
        f_name = request.FILES[key].name

        img_path = default_storage.save('tmp/' + f_name, ContentFile(file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, img_path)

        # model path
        model_url = '/path/to/model/'
        predictor_url = '/path/to/predictor/'

        try:
            # Predict the lip shape in the image using the pre-trained predictor and model
            result = PredictLip(tmp_file, predictor_url, model_url).predict()[0]

        except:
            result = "error"

        # make csv file with key and result --> to track accuracy
        csv_file = open('path/to/file.csv', 'a', newline='')
        wr = csv.writer(csv_file)
        wr.writerow([key, result])

        return render(request, "BoguBoguApp/result_view.html", {'result': result})

    else:
        # if request != POST, then return "error"
        return render(request, "BoguBoguApp/result_view.html", {'result': "error"})


def result_view(request):
    return render(request, "BoguBoguApp/result_view.html", {'result': result})
