from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    # result = None
    if request.method == 'POST':
        number1 = request.form.get('number1', type=float)
        number2 = request.form.get('number2', type=float)
        operation = request.form.get('operation')

        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            if number2 != 0:
                result = number1 / number2
            else:
                result = 'Cannot divide by zero'
        else:
            result = 'Invalid operation'
    # 이제 result는 항상 정의되어 있으므로, 여기서 render_template을 호출할 수 있습니다.
    return render_template('first_template.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

