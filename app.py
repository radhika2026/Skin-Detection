import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import time
import utility
import shutil
from subprocess import call

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', ])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/image_upload', methods = ["POST"])
def image_upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        extension = filename.rsplit('.', 1)[1].lower()
        upload_file_name = str(int(time.time())) + "." + extension
        if utility.detect_if_human(upload_file_name):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], upload_file_name))
            skin_tone = utility.isPorcelain(upload_file_name)
            if skin_tone == "Porcelian":
                return render_template('porcelian.html')
            if skin_tone == "sand neutral Range":
                return render_template('sand.html')
            if skin_tone == "warm beige":
                return render_template('warm_beige.html')
            if skin_tone == "ivory_neutral":
                return render_template('natural.html')
            if skin_tone == "warm ivory":
                return render_template('warm_ivory.html')
            # if skin_tone == "Almond Skintone":
            # return render_template('')
            # if skin_tone == "":
            #     return render_template('')
            # if skin_tone == "":
            #     return render_template('')
            # if skin_tone == "":
            #     return render_template('')
            # if skin_tone == "":
            #     return render_template('')
            # if skin_tone == "":
            #     return render_template('')
            # if skin_tone == "":
            #     return render_template('')
        else:
            return ('<h1>Not a human</h1>')

    return render_template('capture.html')

@app.route('/home')
def home():
    # full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Headskin.png').replace("\\","/")
    full_filename = 'Headskin.png'
    print("\n\n\n\n\n", full_filename)
    return render_template("index.html", Headskin = full_filename, Ptr = 'Ptr.png', Ptr2 = "Ptr2.png", Ptr3 = "Ptr3.png")

def clear():
    dir = os.path.join(os.getcwd(), 'static/uploads')
    shutil.rmtree(os.path.join(os.getcwd(), "static/results"))
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename, code=301))
if __name__ == '__main__':
    app.run(debug = True)    