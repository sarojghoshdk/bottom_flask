from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/work',methods=['GET','POST'])
def index():
        
        if request.method == 'POST':
            if request.form.get('Encrypt') == 'Encrypt':
                
                do = "[1,2,3,4]"
            elif  request.form.get('Decrypt') == 'Decrypt':
                
                do = "[10,20,30,40]"

        return render_template("result.html" , do = do)




if __name__=="__main__":
    app.run(host="0.0.0.0")
