from flask import Flask, request, redirect, render_template, flash 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build_a_blog:buildablog@localhost:8889/build_a_blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key= '8an@8a$4m3'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    titles = db.Column(db.String(120))
    body = db.Column(db.String(500))
    

    def __init__(self, titles, body):
        self.titles = titles
        self.body= body

    
            

@app.route('/newpost', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        new_entry_title = request.form['titles']
        new_entry_body = request.form['body']
        if new_entry_title != 0:
            new_entry_title=new_entry_title
        elif new_entry_body !=0:
            new_entry_body=new_entry_body
            new_entry = Blog(new_entry_title, new_entry_body)
            db.session.add(new_entry)
            db.session.commit()
            new_blog = '/new?id=' + str(new_entry.id)
            return redirect (new_blog)
        else: 
            return render_template('blog_entry.html')
            

    else:
        return render_template('blog_entry.html', title= 'Add your blog below')        

@app.route('/blog')
def list():
    blog_list= Blog.query.all()
    return render_template('display_blogs.html', blog_list=blog_list)

@app.route('/new')
def single_post():
    entry_id = request.args.get('id')
    if (entry_id):
        entry = Blog.query.get(entry_id)
        return render_template('new_blog.html', title="Blog Entry", entry=entry)

if __name__ == '__main__':
    app.run()