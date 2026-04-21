from flask import Flask, request, render_template
from src.Heart.pipeline.Prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

# Define the home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Validate and convert form data to CustomData object
            age = request.form.get("age", 54)
            sex = request.form.get("sex", 1)
            cp = request.form.get("cp", 3)
            trestbps = request.form.get("trestbps", 130)
            chol = request.form.get("chol", 240)
            fbs = request.form.get("fbs", 0)
            restecg = request.form.get("restecg", 0)
            thalach = request.form.get("thalach", 150)
            exang = request.form.get("exang", 0)
            oldpeak = request.form.get("oldpeak", 1.4)
            slope = request.form.get("slope", 1)
            ca = request.form.get("ca", 0)
            thal = request.form.get("thal", 2)

            data = CustomData(
                age=age,
                sex=sex,
                cp=cp,
                trestbps=trestbps,
                chol=chol,
                fbs=fbs,
                restecg=restecg,
                thalach=thalach,
                exang=exang,
                oldpeak=oldpeak,
                slope=slope,
                ca=ca,
                thal=thal
            )

            final_data = data.get_data_as_dataframe()
            # Make prediction
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_data)
            result = round(pred[0], 2)

            patient = {
                "age": age,
                "sex": sex,
                "cp": cp,
                "trestbps": trestbps,
                "chol": chol,
                "fbs": fbs,
                "restecg": restecg,
                "thalach": thalach,
                "exang": exang,
                "oldpeak": oldpeak,
                "slope": slope,
                "ca": ca,
                "thal": thal
            }
            return render_template("result.html", final_result=result, patient=patient)

        except Exception as e:
            # Handle exceptions gracefully
            error_message = f"Error during prediction: {str(e)}"
            return render_template("error.html", error_message=error_message)

    else:
        # Render the initial page
        return render_template("index.html")

@app.route("/referral")
def referral():
    return render_template("referral.html")

# Execution begins
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
