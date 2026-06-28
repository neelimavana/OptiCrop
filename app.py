from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model/model.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))
encoder = pickle.load(open('model/label_encoder.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/find-your-crop', methods=['GET', 'POST'])
def find_your_crop():
    if request.method == 'GET':
        return render_template('find_your_crop.html')

    try:
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        input_scaled = scaler.transform(input_data)
        pred_encoded = model.predict(input_scaled)[0]
        prediction = encoder.inverse_transform([pred_encoded])[0].capitalize()

        return render_template('find_your_crop.html', prediction=prediction)
    except Exception as e:
        return render_template('find_your_crop.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)