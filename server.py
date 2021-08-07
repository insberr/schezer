from flask import Flask, request, url_for, Response
import os
app = Flask(__name__,static_url_path="/")

@app.route('/')
def indexpage():
    return app.send_static_file('index.html')

#@app.route("/<pagename>")
#def page(pagename):
#    if os.path.exists(os.path.join("static",pagename) + ".html"):
#        return app.send_static_file(pagename+".html")
#    else:
#        return Response(status=404)

if __name__ == "__main__":
    app.run(debug=True) # if we are running from the command line, run in debug mode becuase we are probably testing