from flask import Flask, request, jsonify, render_template
from modules.models import load_model
from modules.data_processing import transform_image
import torch
from PIL import Image

app = Flask(__name__)

# 모델 불러오기
model = load_model('models/mnist_model.pth') # MnIST 실습 후 만든 저장한 모델 사용

@app.route('/')
def index():
    return render_template('index.html') # templates 폴더에 있는 index.html 반환

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({
            'error': 'No file uploaded'
        }), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({
            'error': 'No selected file'
        })
    
    if file:
        # 이미지를 전처리하고 모델로 예측
        img = Image.open(file)
        processed_img = transform_image(img)

        # 예측
        prediction = model(processed_img)
        result = torch.argmax(prediction, dim=1).item()

        # 결과 반환
        return jsonify({
            'prediction': result
        })
    
    else:
        return jsonify({
            'error': 'Invalid file'
        })
    
if __name__ == '__main__':
    app.run(debug=True)