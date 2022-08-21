from os import abort
from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Glaucoma detection from Retinal Fundus Images",
        "thumb": "img/glaucoma.png", # Thumbnail for home
        "categories": ["IEEE", "Research Paper"],
        "prod": "https://ieeexplore.ieee.org/document/9182388"
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/glaucoma.png",
        "categories": ["react", "javascript"],
        "prod": "https://youtube.com"
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/glaucoma.png",
        "categories": ["writing"],
        "prod": "https://twitter.com"
    }
]

@app.route('/')
def home():
    return render_template("home.html", projects = projects)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html") 

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)