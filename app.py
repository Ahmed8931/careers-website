from flask import Flask ,render_template
app = Flask(__name__)

Jobs = [{
          'name':"Data analyst",
          'location':"Remote",
          'salary':'10,000',
          'currency' : '$'
        },
        {
          'name':"Data Scientist",
          'location':"Karachi,Pakistan",
          'salary':'18,00,000',
          'currency' : 'Rs.'
        },
        {
          'name':"Frontend Engineer",
          'location':"Lahore,Pakistan",
          'salary':'12,00,000',
          'currency' : 'Rs.'
        },
        {
          'name':"Backend Engineer",
          'location':"Karachi,Pakistan",
          'salary':'15,00,000',
          'currency' : 'Rs.'
        }
       ]
@app.route('/')
def main():
  return render_template('index.html',jobs = Jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True,port=5001)