from flask import Flask, render_template, request
import math

app = Flask(__name__)

def get_number_details(n):
    return {
        'multiplication': [f"{n} x {i} = {n*i}" for i in range(1, 11)],
        'is_prime': n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)),
        'factors': [i for i in range(1, n+1) if n % i == 0],
        'square': n ** 2,
        'cube': n ** 3,
        'even_or_odd': "Even" if n % 2 == 0 else "Odd",
        'square_root': round( math.sqrt(n), 3 ),
        'cube_root': round( n ** (1/3), 3 )
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    number = int(request.form['number'])
    details = get_number_details(number)
    return render_template('result.html', number=number, details=details)

if __name__ == '__main__':
    app.run(debug=True)
