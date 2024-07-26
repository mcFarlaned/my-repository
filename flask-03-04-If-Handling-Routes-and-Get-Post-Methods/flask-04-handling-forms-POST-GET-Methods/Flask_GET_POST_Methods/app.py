# Import Flask modules
from flask import Flask, render_template

# Create an object named app
app = Flask(__name__)



# create a function named "lcm" which calculates a least common multiple values of two numbers. 
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)



# Create a function named `index` which uses template file named `index.html` 
# send two numbers as template variable to the app.py and assign route of no path ('/') 
@app.route('/')
def index():
    num1 = 10  # Replace with your first number
    num2 = 15  # Replace with your second number
    return render_template('index.html', num1=num1, num2=num2)





# calculate sum of them using "lcm" function, then sent the result to the 
# "result.hmtl" file and assign route of path ('/calc'). 
# When the user comes directly "/calc" path, "Since this is a GET request, LCM has not been calculated" string returns to them with "result.html" file
@app.route('/calc')
def calc():
    num1 = 10  # Replace with your first number
    num2 = 15  # Replace with your second number
    result = lcm(num1, num2)
    return render_template('result.html', result=result)



# Add a statement to run the Flask application which can be debugged.
if __name__ == "__main__":
    app.run(debug=True)