from flask import Flask, send_file
import qrcode

app = Flask(__name__)

@app.route('/generate_qr')
def generate_qr():
    data = "https://flask.palletsprojects.com/en/3.0.x/"
    img = qrcode.make(data)
    img.save("qr.png")
    return send_file("qr.png", mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')