from flask import *
#importing all the methods, classes, functions from flask


app = Flask(__name__)


#This is the first page that comes when you type localhost:5000... it will have a a tag that redirects to a page
@app.route("/")
def  HomePage(index.html):
    return "<a href='/runscript'>EXECUTE SCRIPT </a>"

#Once it redirects here (to localhost:5000/runscript) it will run the code before the return statement
@app.route("/runscript")
def ScriptPage():
    #Type what you want to do when the user clicks on the link
    # once it is done with doing that code... it will redirect back to the homepage
    return redirect(url_for("HomePage"))

#Running it only if we are running it directly from the file... not by importing
if __name__ == "__main__":
    app.run(debug=True)