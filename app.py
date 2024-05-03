from flask import Flask ,render_template
app = Flask(__name__)

Jobs = [{
          'id':'1',
          'name':"Data analyst",
          'location':"Remote",
          'salary':'10,000',
          'currency' : '$',
          'requirements':"Bachelor's degree in computer science or related field.\nExcellent communication skills.\nStrong problem-solving and analytical skills.\nExperience with data analysis tools and techniques.1-3 years of experience in python and SQL programming.Basic skills in Ms Excel or Google Sheets.\nExperience with data visualization tools such as Tableau or Power BI.Strong attention to detail and a passion for learning new technologies and techniques.\nAbility to work independently and as part of a team.",
        'responsibilities':"Process data using python,SQL and other tools through the analytics data pipeline.\nIdentify and translate business rules into spcifications and documentation.\nAnalyze and interpret data to uncover insights and make data-driven decisions.Design and implement."
        },
        {
          'id':'2',
          'name':"Data Scientist",
          'location':"Karachi,Pakistan",
          'salary':'18,00,000',
          'currency' : 'Rs.',
          'requirements':"Expert knowledge in Deep learning, NLP, and machine learning.\nExperience with data analysis tools and techniques.\nStrong problem-solving and analytihical skills.\nExperience with data visualization tools such as Tableau or Power BI.Strong attention to detail and a passion.\nProficient in some or all of the following:Python, SQL, R, Tableau, Power BI, Excel,linear and logic regression,Decision trees,Random forest,K-nearest neighbor,Markov Chain,Monte Carlo,Gibbs Sampling,Evolutionary algorithm,Support Vector machine.",
          'responsibilities':"Draft detailed scope for assigned projects.\nDevelop and implement data analysis and machine learning models.\nDevelop and implement data visualization tools such as Tableau or Power Bi.\nExecute on the plan with appropriate data mining,analytical and data science techniques.\nPerform quality assurance and testing of the data analysis and machine learning models.\nManage and maintain the data analysis and machine learning models."
        },
        {
          'id':'3',
          'name':"Frontend Engineer",
          'location':"Lahore,Pakistan",
          'salary':'12,00,000',
          'currency' : 'Rs.',
          'requirements':"Srong knowledge of programming skills in HTML,CSS,Javascript.\nFamiliarity with responsive and adabtabilty design.\nExperience with front-end frameworks such as React,Angular,Vue.js.\nExperince with building website and ability to handle cross browser compatibility issues",
          'responsibilities':"Translate wireframs and designs into high quality JS,HTML and CSS templates.\nDesign ,build and maintain high performance ,reusable and reliable UI components and products.\nEnsure the best possible performance,quality and optimize for maximum speed and scalability.\nWork closely with the design team to ensure the best possible user experience."
        },
        {
          'id':'4',
          'name':"Backend Engineer",
          'location':"Karachi,Pakistan",
          'salary':'15,00,000',
          'currency' : 'Rs.',
          'requirements':"Hands on experience with building a web backend with Java or Golang.\nKnowledge of designing and building Rest APIs.\nProven experience in building a scalable and resilient backend with a focus on performance and security.\nExperience with database design and implementation.Experience with cloud infrastructure and deployment.",
          'responsibilities':"Design and develop a cloud based backend.\nParticipate and produce a scalable cloud based backend system.\nDesign and develop REST based APIs.\nInteract with customers directly with other stakeholders in the organization."
        }
       ]
@app.route('/')
def main():
  return render_template('index.html',jobs = Jobs)

@app.route('/jobs/<int:id>')
def job(id):
  id = id - 1
  if id in range(len(Jobs)):
    return render_template('jobs.html',job = Jobs[id])
  else:
    return "Not Found"
  
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True,port=5001)