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
    request,
)
from blog.forms import (
    RegistrationForm,
    LoginForm,
    UpdateProfileForm,
)
from blog.models import (
    User,
    Post,
)
from flask_login import (
    login_user,
    current_user,
    logout_user,
    login_required
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


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("you logged in successfully", category="success")
            next_arg = request.args.get("next")
            return redirect(next_arg if next_arg else url_for('home'))
        else:
            flash("Email or Password is Wrong", category="danger")

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("you logged out successfully", category="success")
    return render_template("home.html")


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Update Successfully", category="info")
    form.username.data = current_user.username
    form.email.data = current_user.email
    return render_template('profile.html', form=form)