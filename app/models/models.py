from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from app import db, bcrypt


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = User.hashed_password(password)
    
    @staticmethod
    def create_user(payload):
        user = User(
            email=payload["email"],
            password=payload["password"],
            first_name=payload["first_name"],
            last_name=payload["last_name"],
        )

        try:
            db.session.add(user)
            db.session.commit()
            return True
        except IntegrityError:
            return False

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None


class Task(db.Model):
    class STATUS:
        COMPLETED = 'COMPLETED'
        IN_PROGRESS = 'IN_PROGRESS'

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime())
    task = db.Column(db.String(255))
    user_id = db.Column(db.String(255))
    status = db.Column(db.String(255))
    
    def __init__(self, task, user_id, status):
        self.date = datetime.utcnow().date()
        self.task = task
        self.user_id = user_id
        self.status = status

    @staticmethod
    def add_task(incoming):
        task = Task(
            task=incoming["task"],
            user_id=incoming["user_id"],
            status=incoming["status"]
        )
        db.session.add(task)
        db.session.commit()
    
    @staticmethod
    def get_latest_tasks():
        user_to_task = {}

        result = db.engine.execute(
            """SELECT date, task, t.user_id, status, u.first_name, u.last_name
                from task t 
                INNER JOIN (SELECT user_id, max(date) as MaxDate from task group by user_id) tm 
                    on t.user_id = tm.user_id and t.date = tm.MaxDate 
                INNER JOIN "user" u 
                    on t.user_id = u.email""") # join with users table
                    
        for t in result:
            if t.user_id in user_to_task:
                user_to_task.get(t.user_id).append(dict(t))
            else:
                user_to_task[t.user_id] = [dict(t)]
       
        return user_to_task

    @staticmethod
    def get_tasks_for_user(user_id):
        return Task.query.filter_by(user_id=user_id)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'date'       : self.date.strftime("%Y-%m-%d"),
           'task'       : self.task,
           'user_id'    : self.user_id,
           'status'     : self.status,
       }
