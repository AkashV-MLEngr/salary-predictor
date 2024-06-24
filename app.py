from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

file=open('salaryPredictor.pkl','rb')
model=pickle.load(file)
file.close()

@app.route('/',methods=['GET','POST'])
def predictor():
    if request.method=='POST':        
        Education = request.form['Education']
        Experience = request.form['Experience']
        Location = request.form['Location']
        Job_Title = request.form['Job_Title']
        Age = request.form['Age']
        Gender = request.form['Gender']
        inputFeatures=[[Education, Experience, Location, Job_Title, Age, Gender]]
        salary=model.predict(inputFeatures)[0]
        print(salary)
        salaryInfo = f"The Predicted Salary is ₹{salary:,.2f}."        
        return render_template('index.html', salary=salaryInfo)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)