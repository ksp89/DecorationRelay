import RPi.GPIO as GPIO
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pin_list_dictionary = [2, 3, 4, 17,
                       27, 22, 10, 9,
                       11, 5, 6, 13,
                       19, 26, 21, 20]

relay_dictionary = {
    'R1': [2, True], 'R2': [3, True], 'R3': [4, True], 'R4': [17, True],
    'R5': [27, True], 'R6': [22, True], 'R7': [10, True], 'R8': [9, True],
    'R9': [11, True], 'R10': [5, True], 'R11': [6, True], 'R12': [13, True],
    'R13': [19, True], 'R14': [26, True], 'R15': [21, True], 'R16': [20, True],
}

GPIO.setmode(GPIO.BCM)
for key in relay_dictionary:
    GPIO.setup(relay_dictionary[key][0], GPIO.OUT, initial=relay_dictionary[key][1])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ManualRelayControl', methods=['GET', 'POST'])
def manualrelaycontrol():
    if request.method == 'POST':

        if request.form.get('Relay'):
            key = request.form.get('Relay')
            if relay_dictionary[key][1]:
                relay_dictionary[key][1] = False
                GPIO.output(relay_dictionary[key][0], relay_dictionary[key][1])
            else:
                relay_dictionary[key][1] = True
                GPIO.output(relay_dictionary[key][0], relay_dictionary[key][1])

        elif request.form.get('All On') == 'ALL ON':
            for key in relay_dictionary:
                relay_dictionary[key][1] = False
                GPIO.output(relay_dictionary[key][0], relay_dictionary[key][1])

        elif request.form.get('All Off') == 'ALL OFF':
            for key in relay_dictionary:
                relay_dictionary[key][1] = True
                GPIO.output(relay_dictionary[key][0], relay_dictionary[key][1])
        else:
            pass

        return redirect(url_for('manualrelaycontrol'))
    else:
        pass
    return render_template('ManualRelayControl.html', stuff=relay_dictionary)


if __name__ == '__main__':
    try:
        app.run(debug=False, host='0.0.0.0')
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()