from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from models import db, Post, Comment
from forms import PostForm, CommentForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash("Post created!", "success")
        return redirect(url_for('index'))
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', form=form, posts=posts)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, post=post)
        db.session.add(comment)
        db.session.commit()
        flash("Comment added!", "info")
        return redirect(url_for('post_detail', post_id=post.id))
    return render_template('post_detail.html', post=post, form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
