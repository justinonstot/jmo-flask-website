from app import app

@app.route('/')
@app.route('/index')

def index():
    # return render_template('home.html') 
    return "Hello World!"