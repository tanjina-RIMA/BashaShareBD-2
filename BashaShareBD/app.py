from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SECRET_KEY"] = "bashashare_secret_key"

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bashashare.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# USER MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    phone = db.Column(db.String(20), nullable=False)

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(
        db.String(20),
        default="user"
    )

    trust_score = db.Column(
        db.Integer,
        default=50
    )


# ACCOMMODATION MODEL
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    rent = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    status = db.Column(
        db.String(20),
        default="pending"
    )

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )
    
    
# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# REGISTER PAGE
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")

        # Check empty fields
        if not name or not email or not phone or not password:
            flash("All fields are required.", "danger")
            return redirect(url_for("register"))

        # Check duplicate email
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("This email is already registered.", "danger")
            return redirect(url_for("register"))

        # Password validation
        if len(password) < 6:
            flash("Password must be at least 6 characters.", "danger")
            return redirect(url_for("register"))

        # Hash password
        hashed_password = generate_password_hash(password)

        # Create user
        new_user = User(
            name=name,
            email=email,
            phone=phone,
            password=hashed_password
        )

        # Save user
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")

        return redirect(url_for("login"))

    return render_template("register.html")



# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        # Find user by email
        user = User.query.filter_by(email=email).first()

        # Check email and password
        if user and check_password_hash(user.password, password):
            # Save user information in session
            session["user_id"] = user.id
            session["user_name"] = user.name
            session["user_role"] = user.role
            
            flash("Login successful!", "success")

            return redirect(url_for("dashboard"))

        else:
            flash("Invalid email or password.", "danger")

            return redirect(url_for("login"))

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():
    
    # Check if user is logged in
    if "user_id" not in session:
        flash("Please login first.", "danger")
        return redirect(url_for("login"))

    return render_template("dashboard.html")

# ADD LISTING
@app.route("/add-listing", methods=["GET", "POST"])
def add_listing():

    # Check login
    if "user_id" not in session:
        flash("Please login first.", "danger")
        return redirect(url_for("login"))

    if request.method == "POST":

        print("========== ADD LISTING POST ==========")
        print("USER ID:", session.get("user_id"))
        print("FORM DATA:", request.form)

        title = request.form.get("title", "").strip()
        location = request.form.get("location", "").strip()
        rent = request.form.get("rent", "").strip()
        description = request.form.get("description", "").strip()

        print("TITLE:", title)
        print("LOCATION:", location)
        print("RENT:", rent)
        print("DESCRIPTION:", description)

        # Validate fields
        if not title or not location or not rent or not description:
            print("ERROR: Missing form field")
            flash("All fields are required.", "danger")
            return redirect(url_for("add_listing"))

        # Convert rent to integer
        try:
            rent = int(rent)
        except ValueError:
            print("ERROR: Rent is not a number")
            flash("Rent must be a valid number.", "danger")
            return redirect(url_for("add_listing"))

        # Create listing
        new_listing = Listing(
            title=title,
            location=location,
            rent=rent,
            description=description,
            owner_id=session["user_id"],
            status="approved"
        )

        print("CREATING LISTING...")
        print("OWNER ID:", session["user_id"])

        db.session.add(new_listing)

        # Commit to database
        db.session.commit()

        print("DATABASE COMMIT SUCCESSFUL")
        print("LISTING ID:", new_listing.id)

        flash("Listing submitted successfully.", "success")

        print("REDIRECTING TO /listings")

        return redirect(url_for("listings"))

    return render_template("add_listing.html")

 # VIEW LISTINGS
@app.route("/listings")
def listings():

    if "user_id" not in session:
        flash("Please login first.", "danger")
        return redirect(url_for("login"))

    search = request.args.get("search", "")

    if search:
        listing_data = Listing.query.filter(
            Listing.location.contains(search),
            Listing.status == "approved"
        ).all()
    else:
        listing_data = Listing.query.filter_by(
            status="approved"
        ).all()

    return render_template(
        "listings.html",
        listings=listing_data,
        search=search
    )
    
    
   

# APPROVE LISTING
@app.route("/admin/approve/<int:listing_id>")
def approve_listing(listing_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    if session.get("user_role") != "admin":
        flash("Access denied.", "danger")
        return redirect(url_for("dashboard"))

    listing = Listing.query.get_or_404(listing_id)

    listing.status = "approved"

    db.session.commit()

    flash("Listing approved successfully.", "success")

    return redirect(url_for("admin"))


# REJECT LISTING
@app.route("/admin/reject/<int:listing_id>")
def reject_listing(listing_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    if session.get("user_role") != "admin":
        flash("Access denied.", "danger")
        return redirect(url_for("dashboard"))

    listing = Listing.query.get_or_404(listing_id)

    listing.status = "rejected"

    db.session.commit()

    flash("Listing rejected.", "success")

    return redirect(url_for("admin"))

    
# LOGOUT
@app.route("/logout")
def logout():

    # Remove all session information
    session.clear()

    flash("You have been logged out.", "success")

    return redirect(url_for("login"))

 # ADMIN PANEL
@app.route("/admin")
def admin():

    # Must be logged in
    if "user_id" not in session:
        flash("Please login first.", "danger")
        return redirect(url_for("login"))

    # Only admin can access
    if session.get("user_role") != "admin":
        flash("Access denied. Admins only.", "danger")
        return redirect(url_for("dashboard"))

    pending_listings = Listing.query.filter_by(
        status="pending"
    ).all()

    return render_template(
        "admin.html",
        listings=pending_listings
    )


# CREATE DATABASE
with app.app_context():
    db.create_all()

 
 # RUN APPLICATION   
if __name__ == "__main__":
    app.run(debug=True)
    
    