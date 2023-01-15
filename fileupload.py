from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
import uuid
app = Flask(__name__)
app.config['files'] = 'files'
app.secret_key = 'hard guess'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    session['username'] = request.form.get('username')
    if session.get('username') == None:
        return redirect('/')
    else:
        target_father_dir = os.path.join(
            app.config['files'], session['username'])
        if not os.path.exists(target_father_dir):
            os.makedirs(target_father_dir)
        return redirect(url_for('upload'))


@app.route('/list')
def filelist():
    if session.get('username') == None:
        return redirect(url_for('login'))
    else:
        list = []
        path = os.path.dirname(__file__)
        path = os.path.join(path, app.config['files'], session['username'])
        filelist = os.listdir(path)

        for file in filelist:
            #path = os.path.join(os.pardir, app.config['files'])
            t = os.path.join('/download', file)
            list.append([file, t])
        return render_template('list.html', username=session['username'], list=list)

@app.route('/del/<filename>',methods=['GET'])
def delfilename(filename):
    path = os.path.dirname(__file__)
    path = os.path.join(path, app.config['files'], session['username'],filename)
    os.remove(path)
    return redirect(url_for('filelist'))

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    if request.method == 'GET':
        # path=os.path.isfile(os.path.join(app.config['files'],session['username'],filename))
        path = os.path.join(app.config['files'], session['username'])
        if path:
            return send_from_directory(path, filename, as_attachment=True)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(
            basepath, 'files', session['username'], f.filename)
        f.save(upload_path)

        return redirect(url_for('filelist'))


@app.route('/manage')
def manage():
    return 'manage'


if __name__ == '__main__':
    app.run('0.0.0.0', port='8080', debug=False)
