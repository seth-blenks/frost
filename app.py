
from flask import Flask,url_for


from main.blog_blueprint import blog_print

from main.provider import Article_Notification


#application creation function
def create_application(setup,*blueprint):
    app = Flask(__name__)
    app.config.from_object(setup)
    
    #registering all blueprint to application
    for blues in blueprint:
        app.register_blueprint(blues)
    
    
    return app

app = create_application('config.Development',blog_print)

if __name__ == '__main__':
    
    app.run(port=8081,host='10.42.0.1')