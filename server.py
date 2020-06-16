from flask import Flask, make_response, render_template, redirect
import logging
from  datetime import datetime as dt

import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='templates',
            template_folder='templates'
)

logging.basicConfig(
    filename='access.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

logging.getLogger().addFilter(lambda record: "/ " in record)


@app.route("/")
def home():
    return render_template("pages/auth-normal-sign-in.htm")

@app.route("/404")
def not_found():
    return render_template("errors/404.html")



@app.route("/<template>")
def page(template):
    path = os.path.join("templates", "pages", template)
    if not os.path.isfile(path):
        path = os.path.join("templates", "theme", template)
        if not os.path.isfile(path):
            print("THEME Not Found:", template)
            return redirect("/404")
        else: return render_template("theme/"+template)
    return render_template("pages/"+template)


if __name__ == "__main__":
    app.run(debug=True, port=80)
