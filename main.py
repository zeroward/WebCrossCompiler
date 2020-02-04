import os
# import magic
import urllib.request
from app import app
import ccomp
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['cs', 'c+', 'c'])


def allowed_file(filename):
    #return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    return True

@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            compiler = request.values['compiler']
            arch = request.values['architecture']
            outfile = request.values['output']
            if not outfile.isalpha():
                flash('HACKING DETECTED!!!!')
                return redirect('/')
            ccomp.comphandle(filename, compiler, arch, outfile)
            return redirect('/')
        else:
            flash('Source Code Only Allowed!')
            return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')