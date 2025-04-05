from flask import Flask, render_template, request
app = Flask(__name__)
entries = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/entries', methods=["POST"])
def createdEntries():
    if request.method == 'POST':
        entry = {
            'date': request.form['date'],
            'title': request.form['title'],
            'description': request.form['description']
        }

        entries.append(entry)
        return render_template('entries.html', entries=entries)


@app.route('/view_entries')
def viewEntries():
    return render_template('entries.html', entries=entries)
if __name__ == '__main__':
    app.run(debug=True)
