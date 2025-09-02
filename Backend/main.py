from flask import Flask, render_template, request, send_file, jsonify
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get('text', '')
    if not data:
        return jsonify({'error': 'No text provided'}), 400

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#003366", back_color="white").convert('RGB')
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    # Serve as base64 for front-end preview
    import base64
    img_b64 = base64.b64encode(img_io.getvalue()).decode()
    return jsonify({'img_data': f'data:image/png;base64,{img_b64}'})

@app.route('/download_qr', methods=['POST'])
def download_qr():
    data = request.json.get('text', '')
    if not data:
        return "No text provided", 400
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#003366", back_color="white").convert('RGB')
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png', download_name='qrcode.png')

if __name__ == '__main__':
    app.run(debug=True)
