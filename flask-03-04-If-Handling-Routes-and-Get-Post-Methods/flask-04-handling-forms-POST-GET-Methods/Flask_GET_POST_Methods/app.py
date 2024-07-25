# Import Flask modules
from flask import Flask, render_template, request


# Create an object named app
app = Flask(__name__)


# create a function named "lcm" which calculates a least common multiple values of two numbers. 



# Create a function named `index` which uses template file named `index.html` 
# send two numbers as template variable to the app.py and assign route of no path ('/')
@app.route("/")
def index():
    return render_template("index.html")



# calculate sum of them using "lcm" function, then sent the result to the 
# "result.hmtl" file and assign route of path ('/calc'). 
# When the user comes directly "/calc" path, "Since this is a GET request, 
# LCM has not been calculated" string returns to them with "result.html" file
@app.route("/calc", methods=["GET", "POST"])
def calculate():
    # if get request
    #   render index.html with NO LCM specified
    # else (if post request)
    #   render index.html with LCM specified
    if request.method == "GET":
        return render_template("result.html", developer_name="Altaz")
    else: # request.method == "POST"
        my_lcm = 1
        my_result1 = request.form.get("number1")
        my_result2 = request.form.get("number2")
        return render_template("result.html", 
                               lcm=my_lcm, 
                               result1=my_result1, 
                               result2=my_result2,
                               developer_name="Devon")


# Add a statement to run the Flask application which can be debugged.
if __name__ == "__main__":
    app.run(debug=True)