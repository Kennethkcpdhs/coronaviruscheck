from flask import Flask, render_template,request,redirect,url_for


app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/healthcheck", methods=["GET","POST"])
def healthcheck():
    return render_template("healthcheck.html")

@app.route("/result", methods=["GET","POST"])
def result():
    if request.method == "POST":

        usertemp = float(request.form.get('usertemp'))
        userper = usertemp
        conditions = ['sneeze','cough','fatigue','breath','friend','crowded','large','overseas']
        for condition in conditions:
            val = request.form.get('cough')
            if val is not None:
                userper *= float(val)
        userper = int(round(userper))
        if float(usertemp) > 37.5:
            return render_template("failresult.html", percentage=userper)
        else:
            return render_template("result.html", percentage=userper)


if __name__ == "__main__":
    app.run(debug=True)
