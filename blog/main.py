from flask import Flask, render_template, request, redirect, url_for
from db import*

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    sections = get_blog_sections()
    return render_template("index.html", sections=sections)


@app.route("/<section_slug>")
def section_page(section_slug):
    sections = get_blog_sections()
    section = get_section_by_slug(section_slug)

    if not section:
        return "Розділ не знайдено", 404

    posts = get_section_posts(section["id"])

    return render_template("section.html", sections=sections, section=section, posts=posts)

@app.route("/add", methods=["GET", "POST"])
def add_post():
    sections = get_blog_sections()

    if request.method == "POST":
        text = request.form["text"]
        image = request.form["image"]
        section_id = int(request.form["section"])
        create_new_post(text, image, section_id)
        section = get_section_by_id(section_id)
        return redirect(url_for("section_page", sections=sections,
                                section_slug=section["slug"]))

    return render_template("add_post.html", sections=sections)


@app.route("/<section_slug>/<post_id>")
def article(section_slug, post_id):
    sections = get_blog_sections()
    post = post_by_id(post_id)

    if not post:
        return "Статтю не знайдено", 404

    post_section = get_section_by_id(post["section_id"])


    return render_template("post_detail.html", sections=sections, post=post, post_section=post_section)


app.run()
