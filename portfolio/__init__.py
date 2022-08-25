from os import abort
from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Glaucoma detection from Retinal Fundus Images",
        "thumb": "img/glaucoma.jpg", # Thumbnail for home
        "categories": ["IEEE", "Research Paper"],
        "prod": "https://ieeexplore.ieee.org/document/9182388"
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/glaucoma.jpg",
        "categories": ["react", "javascript"],
        "prod": "https://youtube.com"
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/glaucoma.jpg",
        "categories": ["writing"],
        "prod": "https://twitter.com"
    }
]

# ALL THE DIMENSIONS OF IMAGE SHOULD BE 1920X1080
certifications = [ 
    {
        "name": "IBM AI Engineering Professional Certificate",
        "thumb": "img/ai-engineer.jpg",
        "prod": "https://www.credly.com/badges/79dfbd63-5141-4e7a-972a-6e45ff53a089/public_url"
    },
    {
        "name": "Algorithmic Toolbox",
        "thumb": "img/algorithm.jpg",
        "prod": "https://www.coursera.org/account/accomplishments/certificate/LWCU3CWG7GRG"
    },
    {
        "name": "TensorFlow Developer Professional Certificate",
        "thumb": "img/tensorflow.jpg",
        "prod": "https://www.coursera.org/account/accomplishments/specialization/certificate/AYXSTXBMNW9J"
    },
]

@app.route('/')
def home():
    return render_template("home.html", projects = projects)

@app.route('/certification')
def certification():
    return render_template("certification.html", certifications = certifications)

@app.route('/contact')
def contact():
    return render_template("contact.html") 

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
