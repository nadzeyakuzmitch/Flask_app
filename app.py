import Flask, send_from_directory
import qrcode
from flask_wtf.csrf import CSRFProtect

# Setup CSRF protection
csrf = CSRFProtect(app)


app = Flask(__name__)
# Set a secret key for CSRF protection
app.config['SECRET_KEY'] = '12345'  # Change 'your-secret-key' to a real secret key

# Setup CSRF protection
csrf = CSRFProtect(app)

@app.route('/')
def serve_qr():
    img_path = generate_qr_code("https://flask.palletsprojects.com/en/3.0.x/")
    return send_from_directory('static', img_path)

def generate_qr_code(url):
    filename = "repo_qrcode.png"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to the static folder
    img.save("static/" + filename)
    
    return filename

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')