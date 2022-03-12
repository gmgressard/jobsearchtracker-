from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """user info"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))

    def __repr__(self):
        """show user info"""
        return f'<Username:{self.username} email: {self.email}>'


class Job(db.Model):
    """job posting info"""

    __tablename__ = 'jobs'

    job_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    company_name = db.Column(db.String(30))
    job_title = db.Column(db.String(30))
    date_applied = db.Column(db.DateTime)
    company_website = db.Column(db.String(100), nullable=True)
    job_description = db.Column(db.String(300), nullable=True)
    notes = db.Column(db.String(300), nullable=True)
    active = db.Column(db.Boolean)

    def __repr__(self):
        """show job info"""
        return f'<Company{self.company_name} job: {self.job_title}>'


class Archive(db.Model):
    """archived jobs"""

    ___tablename__ = 'archives'

    archive_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'))

    def __repr__(self):
        """show archived job info"""
        return f'<job id:{self.job_id}>'


class Quotes(db.Model):
    """motivational quotes"""

    ___tablename__ = 'quotes'

    quote_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    quote = db.Column(db.String(50))

    def __repr__(self):
        """show archived job info"""
        return f'<quote id:{self.quote_id}>'








def connect_to_db(app, db_uri="postgresql:///hikes"):
    """Connect to database"""

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)