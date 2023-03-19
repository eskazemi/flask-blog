from blog import (
    app,
    db,
    bcrypt,
)
from flask import (
    render_template,
    redirect,
    url_for,
    request,
)
from blog.forms import (
    RegistrationForm,
    LoginForm,
)
from blog.models import (
    User,
    Post,
)


@app.route("/", methods=["GET"])
def home():
    return render_template('home.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "GET":
        return render_template("register.html", form=form)
    else:
        if form.validate_on_submit():
            p_h = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            user = User(username=form.username.data, email=form.email.data,
                        password=p_h)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for("home"))


@app.route("/login")
def login():
    form = RegistrationForm()
    return render_template("login.html", form=form)
