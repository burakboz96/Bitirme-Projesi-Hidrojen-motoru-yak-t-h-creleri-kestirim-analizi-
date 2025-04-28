from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Tüm domainlerden gelen istekleri kabul et

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Gelen veriler
    temperature = data.get('temperature', 0)
    humidity = data.get('humidity', 0)
    hydrogen_level = data.get('hydrogen_level', 0)
    vibration = data.get('vibration', 0)

    # Basit tahmin mantığı
    if hydrogen_level < 100:
        prediction = "Sistem stabil"
    elif hydrogen_level < 500:
        prediction = "Dikkat: Hidrojen seviyesi artıyor"
    else:
        prediction = "Tehlikeli seviye: Hidrojen yüksek!"

    # Örnek verimlilik karşılaştırması (örnek değerler)
    verimlilik_analizi = {
        "Yakıt Türü": "Hidrojen (Yenilenebilir)",
        "Termal Verimlilik": "%35-45",
        "CO2 Emisyonu": "Yok",
        "NOx Emisyonu": "Yüksek (azaltılabilir)",
        "Motor Gücü": "Düşük",
        "Enerji Yoğunluğu": "120 MJ/kg",
        "Depolama": "Zor (yüksek basınç)",
        "Güvenlik": "Yüksek riskli",
        "Maliyet": "Yüksek",
        "Gelecek Potansiyeli": "Yüksek (karbon sıfır)"
    }

    return jsonify({
        "prediction": prediction,
        "verimlilik_analizi": verimlilik_analizi,
        "status": "ok"
    })

if __name__ == '__main__':
    app.run(debug=True)
