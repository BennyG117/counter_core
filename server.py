from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret tunnel song"

@app.route('/')
def view_count():
    if 'count' in session:
        print('key exists!')
        session['count'] += 1
    else:
        print("key 'key_name' does NOT exist")
        session['count'] = 0
    
    return render_template("index.html")

@app.route('/clear')
def clear_button():
    session.clear()
    return redirect('/')

@app.route('/add2')
def add_two():
    session['count'] += 1
    return redirect('/')

if __name__=="__main__":  
    app.run(debug=True, port=5001)




