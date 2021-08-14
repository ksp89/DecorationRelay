
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

relay_dictionary = {
    'R1': False, 'R2': False, 'R3': False, 'R4': False,
    'R5': False, 'R6': False, 'R7': False, 'R8': False,
    'R9': False, 'R10': False, 'R11': False, 'R12': False,
    'R13': False, 'R14': False, 'R15': False, 'R16': False,
}



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ManualRelayControl', methods=['GET', 'POST'])
def manualrelaycontrol():
    if request.method == 'POST':

        if request.form.get('Relay'):
            key = request.form.get('Relay')
            if relay_dictionary[key]:
                relay_dictionary[key] = False
            else:
                relay_dictionary[key] = True

        elif request.form.get('All On') == 'ALL ON':
            for key in relay_dictionary:
                relay_dictionary[key] = True

        elif request.form.get('All Off') == 'ALL OFF':
            for key in relay_dictionary:
                relay_dictionary[key] = False
        else:
            pass

        return redirect(url_for('manualrelaycontrol'))
    else:
        pass
    return render_template('ManualRelayControl.html', stuff=relay_dictionary)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
