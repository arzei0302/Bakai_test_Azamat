from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow )
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
        
    def __repr__(self):
        return f'<User {self.name}>'
    
    
class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
        
    def __repr__(self):
        return f'<Employee {self.name}>'
    

class TicketType(db.Model):
    __tablename__ = 'ticket_types'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id, 
            'code': self.code,
            'name': self.name,
        }
    
    def __repr__(self):
        return f'<TicketTypes {self.name}>'
    

class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    ticket_type_id = db.Column(db.Integer, db.ForeignKey('ticket_types.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    ticket_type = db.relationship('TicketType')
    user = db.relationship('User')
    
    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'ticket_type_id': self.ticket_type_id,
            'user_id': self.user_id,
            'date_create': self.date_create.isoformat(), 
            'status': self.status
        }

    def __repr__(self):
        return f'<Ticket {self.id}>'
    

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    status = db.Column(db.String(50), nullable=False)
    

    ticket = db.relationship('Ticket')
    user = db.relationship('User', foreign_keys=[user_id])
    manager = db.relationship('Employee', foreign_keys=[manager_id])
    
    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'date_create': self.date_create.isoformat(),
            'ticket_id': self.ticket_id,
            'user_id': self.user_id,
            'user_details': self.user.to_dict() if self.user else None,
            'manager_id': self.manager_id,
            'manager_details': self.manager.to_dict() if self.manager else None,
            'status': self.status
        }


    def __repr__(self):
        return f'<Message {self.id}>'