from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

list_of_exoplanets = ['Kepler 16-b', '55 Cancrie', 'Trappist-1e', 'PSO J318.522', '51 Pegasib']
exoplanet_distances = {
    'Kepler 16-b': 245,
    '55 Cancrie': 40,
    'Trappist-1e': 39,
    'PSO J318.522': 80,
    '51 Pegasib': 50
}

@app.route('/')
def index():
    return render_template('index.html', exoplanets=list_of_exoplanets)

@app.route('/result', methods=['POST'])
def result():
    try:
        exoplanet = request.form['exoplanet']
        if exoplanet in exoplanet_distances:
            distance = exoplanet_distances[exoplanet]
            return render_template('result.html', exoplanet=exoplanet, distance=distance)
        else:
            return render_template('error.html', message="Invalid exoplanet selection. Please try again.")
    except KeyError:
        return render_template('error.html', message="Please select a valid exoplanet.")

if __name__ == '__main__':
    app.run(debug=True)