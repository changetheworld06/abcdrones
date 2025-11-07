from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mentions-legales")
def mentions_legales():
    return render_template("mentions_legales.html")

@app.route("/politique-confidentialite")
def politique_confidentialite():
    return render_template("politique_confidentialite.html")

@app.route("/cgv")
def cgv():
    return render_template("cgv.html")

@app.route("/robots.txt")
def robots_txt():
    return send_from_directory("static", "robots.txt", mimetype="text/plain")

@app.route("/sitemap.xml")
def sitemap_xml():
    return send_from_directory("static", "sitemap.xml", mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True, port=5173)