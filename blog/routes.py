from blog import (
    app,
    db,
    bcrypt,
)
from flask import (
    render_template,
    redirect,
    url_for,
    flash,
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
    if form.validate_on_submit():
        p_h = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data,
                    password=p_h)
        db.session.add(user)
        db.session.commit()
        flash("you registered successfully", 'success')
        return redirect(url_for("home"))
    return render_template("register.html", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    return render_template("home.html")