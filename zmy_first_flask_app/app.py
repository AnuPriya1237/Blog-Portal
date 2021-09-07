from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = {
    0: {
        'post_id': 0,
        'Title': 'Hello World!',
        'Content': 'This is my personal blog'
    }
}

@app.route('/')
def home():
    return render_template("homee.html",posts = posts)

#for static info
"""@app.route('/post/<int:post_id>')  #post_id will be 0 here from dictionary.
def post(post_id):
    post = posts.get(post_id)
    return render_template('post.html')
"""

#for dynamic info
@app.route('/post/<int:post_id>')  #post_id will be 0 here from dictionary.
def post(post_id):
    post = posts.get(post_id)
    if not post: #when post value = None
        return render_template('404.html',message = f' A post with {post_id} not found.')
    return render_template('post.html', post = posts.get(post_id))  #the red in color post represent the post[Title..]/ post['Conte/..in post.html page


"""@app.route('/post/form')
def form():
    return render_template('create.html')
"""
#http://127.0.0.1:5000/post/form?title=my+post&content=hi+there%21
"""@app.route('/post/create')
def create():
    title = request.args.get('title')
    content = request.args.get('content')
    postid = len(posts)
    posts[postid] = {'post_id':postid, 'Title':title, 'Content':content}
    return redirect(url_for('post', post_id = postid))
"""
#for more secure request there is use of payloads, here hidden payload is request.form

#http://127.0.0.1:5000/post/form?title=my+post&content=hi+there%21
""" ?title=my+post&content=hi+there%21 this information should not be visible this is not secure so this can be actaully packed up by form in html
and attach to hidden payloads. So this won't be visble anyamore it will be hidden. So for that GET method does not have that functionality for that we need
to use POST method."""
#Actaully when you want to put everything in function and do not want sacttrred programming then you can do the stuffs of GET
# and POST method in one function only avoid other unnecessary endpoints
#so you can avlid form route and put that to create only see below for the cahnges.
#also remember there will be some change in create.html also.
"""
@app.route('/post/create', methods = ['POST'])
def create():
    title = request.form.get('title')
    content = request.form.get('content')
    postid = len(posts)
    posts[postid] = {'post_id':postid, 'Title':title, 'Content':content}
    return redirect(url_for('post', post_id = postid))

"""

@app.route('/post/create', methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        postid = len(posts)
        posts[postid] = {'post_id':postid, 'Title':title, 'Content':content}
        return redirect(url_for('post', post_id = postid))
    return render_template('create.html')




if __name__ == '__main__':
    app.run(debug = True)

