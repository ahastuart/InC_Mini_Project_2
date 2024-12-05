from flask import *
from route.user_route import user_page

app = Flask(__name__)
app.secret_key = 'zl934h23i23I23lsc94b'

@app.route('/')
def home():
    return render_template('login.html')

app.register_blueprint(user_page)

if __name__=='__main__':
    app.run(debug=True)
    
route/user_route.py & service/user_service.py & templates/login.html & DBconn.py & meme_start.py