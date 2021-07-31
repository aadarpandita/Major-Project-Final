from flask import Flask,render_template,request
import joblib
app=Flask(__name__)


m=joblib.load('model12.pkl')

@app.route('/')
def Hello():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def Regression():
  if request.method=='POST':
    disease=[]
    disease.extend([request.form['age'], request.form['sex'], request.form['cp'],request.form['chol'],request.form['fbs'],
      request.form['thalach'],request.form['exang'], request.form['oldpeak'],request.form['slope'],request.form['ca'],request.form['thal']])
    target=str(m.predict([disease])[0])
    if(target == "1"):
        target = "Chances of you having Heart Disease is high."
    else:
        target = "Chances of you having Heart Disease is low."
    return render_template('index.html',my_target=target)


if __name__=='__main__':
    app.run(debug=True)


l=[]
