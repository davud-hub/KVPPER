from datetime import datetime, timedelta

from flask import Flask, request, jsonify, render_template, url_for, redirect

import db

app = Flask(__name__)


def genereer_datums():
    dates = []
    for daydelta in range(0, 5):
        date = datetime.now() + timedelta(days=daydelta)
        dates.append(date)
    return dates


def genereer_tijden():
    now = datetime.now()  # vandaag
    starttijd = now.hour if now.hour > 8 else 8  # als het huidige uur later is dan 8, negeer eerdere uren
    output = []
    for hours in range(starttijd, 17):
        for x in (0, 30):  # per halfuur
            output.append(f'{hours:02d}:{x:02d}')  # tijd formatting
    return output


@app.route('/afspraak', methods=['POST'])
def afspraak_invoegen():
    dag = request.form.get('dag')
    tijd = request.form.get('tijd')
    tijdstip = dag + "  " + tijd
    email = 'test' # TODO in frontend
    naam = 'test' # TODO in frontend
    print(dag, tijd)
    db.execute_sql("INSERT INTO afspraak(naam, email, tijdstip) VALUES ('{}','{}','{}')".format(naam,email, tijdstip))
    return redirect(url_for('success'))


app.route('/afspraken', methods=['GET'])
def vraag_afspraken_op():
    dbafspraken = db.execute_sql('SELECT * FROM afspraak ORDER BY tijdstip')

    afspraken = []
    for afspraak in dbafspraken:
        afspraken.append({'naam': afspraak['naam'], 'tijdstip': afspraak['tijdstip']})

    return jsonify(afspraken), 200, {'ContentType': 'application/json'}


@app.route('/success')
def success():
    return 'Afspraak bevestigd!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/maak_afspraak')
def afspraak():
    return render_template('afspraak.html',
                           dagen=genereer_datums(),
                           tijden=genereer_tijden())


if __name__ == '__main__':
    app.run()
