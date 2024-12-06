from flask import Flask, request, render_template
from StringExtractApp import get_classification, test_predictions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        predictions = get_classification(url)
        result = "Legit URL" if predictions == [0] else "Suspicious URL"
        return render_template('index.html', url=url, result=result)
    return render_template('index.html')

@app.route('/test-results', methods=['GET'])
def test_results():
    results = test_predictions()
    return render_template('test_results.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
