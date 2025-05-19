import os, glob, sys
from pdf2image import convert_from_path
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploaded_pdfs'
OUTPUT_FOLDER = './static/images'
TECH_OUTPUT_FOLDER = './static/tech_images'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def convert_pdf_to_img(pdf_path, output_path):

    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return
    
    os.makedirs(output_path, exist_ok=True)

    try:
        images = convert_from_path(pdf_path)
        for filename in os.listdir(output_path):
            if filename.endswith('.png'):
                try:
                    os.remove(os.path.join(output_path, filename))
                    print(f"Removed {filename}")
                except Exception as e:
                    print(f"Error removing {filename}: {e}")
        for i, image in enumerate(images):
            image_path = os.path.join(output_path, f"{i+1}.png")
            image.save(image_path, 'PNG')
            print(f"Saved {image_path}")

    except Exception as e:
        print(f"Error converting PDF to images: {e}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'pdf_file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['pdf_file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(pdf_path)
            convert_pdf_to_img(pdf_path, OUTPUT_FOLDER)
            os.remove(pdf_path)  # Clean up the uploaded PDF
            return redirect(url_for('slideshow'))
    return render_template('upload.html', type="Standard")

@app.route("/techupload", methods=['GET', 'POST'])
def tech_upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'pdf_file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['pdf_file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(pdf_path)
            convert_pdf_to_img(pdf_path, TECH_OUTPUT_FOLDER)
            os.remove(pdf_path)  # Clean up the uploaded PDF
            return redirect(url_for('slideshow'))
    return render_template('upload.html', type="Tech")

@app.route("/techslideshow")
def tech_slideshow():
    image_folder = os.path.join(app.static_folder, 'tech_images')
    image_files = [
        f"images/{file}"
        for file in os.listdir(image_folder)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]
    image_files.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))
    print(f"Image files: {image_files}")
    return render_template("techslideshow.html", images=image_files)

@app.route("/slideshow")
def slideshow():
    image_folder = os.path.join(app.static_folder, 'images')
    image_files = [
        f"images/{file}"
        for file in os.listdir(image_folder)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]
    image_files.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))
    print(f"Image files: {image_files}")
    return render_template("slideshow.html", images=image_files)

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    os.makedirs(TECH_OUTPUT_FOLDER, exist_ok=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()