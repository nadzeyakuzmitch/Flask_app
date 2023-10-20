from flask import Flask, send_from_directory
import qrcode
import os

app = Flask(__name__)

# Ensure the 'static' directory exists
if not os.path.exists("static"):
    os.makedirs("static")

@app.route('/generate_qr', methods=['GET'])
def generate_qr():
    # Create a QR code
    img = qrcode.make('https://flask.palletsprojects.com/en/3.0.x/')
    img.save("static/qr.png")
    
    # Serve the saved QR code image
    return send_from_directory(directory='static', filename='qr.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
