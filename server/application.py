from flask import Flask, request, jsonify
import base64
import cv2
import tensorflow as tf
import os
import numpy as np
import keras
from keras.preprocessing import image
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image

app = Flask(__name__, static_folder='../react-app/build', static_url_path='/')

@app.route('/')
def index():
   return app.send_static_file('index.html')

@app.route('/uploader', methods=['POST', 'GET'])
def make_file():
   if request.method == "POST":
        file = request.data
        f = open("uploads/upload.png", "wb")
        f.write(file)
        f.close()
        print("file created")
        return jsonify(
            name = get_pred_allergy(),
            cancer = get_pred_cancer()
        )

def get_pred_allergy():
    path= './uploads/upload.png'
    model = tf.keras.models.load_model('models/skin_allergy.model')

    labels=['Acne and Rosacea Photos', 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions', 'Atopic Dermatitis Photos', 'Bullous Disease Photos', 'Cellulitis Impetigo and other Bacterial Infections', 'Eczema Photos', 'Exanthems and Drug Eruptions', 'Hair Loss Photos Alopecia and other Hair Diseases', 'Herpes HPV and other STDs Photos', 'Light Diseases and Disorders of Pigmentation', 'Lupus and other Connective Tissue diseases', 'Melanoma Skin Cancer Nevi and Moles', 'Nail Fungus and other Nail Disease', 'Poison Ivy Photos and other Contact Dermatitis', 'Psoriasis pictures Lichen Planus and related diseases', 'Scabies Lyme Disease and other Infestations and Bites', 'Seborrheic Keratoses and other Benign Tumors', 'Systemic Disease', 'Tinea Ringworm Candidiasis and other Fungal Infections', 'Urticaria Hives', 'Vascular Tumors', 'Vasculitis Photos', 'Warts Molluscum and other Viral Infections', 'Acne and Rosacea Photos', 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions', 'Atopic Dermatitis Photos', 'Bullous Disease Photos', 'Cellulitis Impetigo and other Bacterial Infections', 'Eczema Photos', 'Exanthems and Drug Eruptions', 'Hair Loss Photos Alopecia and other Hair Diseases', 'Herpes HPV and other STDs Photos', 'Light Diseases and Disorders of Pigmentation', 'Lupus and other Connective Tissue diseases', 'Melanoma Skin Cancer Nevi and Moles', 'Nail Fungus and other Nail Disease', 'Poison Ivy Photos and other Contact Dermatitis', 'Psoriasis pictures Lichen Planus and related diseases', 'Scabies Lyme Disease and other Infestations and Bites', 'Seborrheic Keratoses and other Benign Tumors', 'Systemic Disease', 'Tinea Ringworm Candidiasis and other Fungal Infections', 'Urticaria Hives', 'Vascular Tumors', 'Vasculitis Photos', 'Warts Molluscum and other Viral Infections']
    pred_image=image.load_img(path) 
    gray_pred=cv2.resize(np.float32(pred_image),(80, 80))
    gray = cv2.cvtColor(gray_pred, cv2.COLOR_BGR2GRAY)
    pred_img_array=image.img_to_array(gray_pred)
    pred_img_array=np.array(pred_img_array)/255
    x_pred=pred_img_array.reshape((-1,80,80,1))

    predicted_category=labels[np.argmax(model.predict([x_pred]))]
    print(predicted_category)
    return predicted_category

def get_pred_cancer():
    model = tf.keras.models.load_model('models/skin_cancer.model')
    labels = ['Benign', 'Malignant']
    read = lambda imname: np.asarray(Image.open(imname).convert("RGB"))
    pred = labels[np.argmax(read)]
    print(pred)
    return pred

if __name__ == '__main__':
    app.run()