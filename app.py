from flask import Flask, request, jsonify
from models import db, User, TicketType, Ticket, Message, Employee
from datetime import datetime
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://arz:1234@localhost/bakai2db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


with app.app_context():
    db.create_all()


@app.route('/ticket_types', methods=['GET'])
def get_ticket_types():
    ticket_types = TicketType.query.all()
    return jsonify([tt.to_dict() for tt in ticket_types])


@app.route('/userticket', methods=['GET'])
def get_user_tickets():
    user_ticket = Ticket.query.all()
    return jsonify([tt.to_dict() for tt in user_ticket])


@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.json
    new_ticket = Ticket(text=data['text'], ticket_type_id=data['ticket_type_id'], user_id=data['user_id'], status='delivered')
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify(new_ticket.to_dict()), 201

# @app.route('/messages', methods=['POST'])
# def create_message():
#     data = request.json
#     new_message = Message(
#         text=data['text'],
#         ticket_id=data['ticket_id'],
#         user_id=data['user_id'],
#         manager_id=data['manager_id'],
#         status=data['status']
#     )
#     db.session.add(new_message)

#     ticket = Ticket.query.get(data['ticket_id'])
#     if ticket:
#         ticket.status = 'решен'
#         db.session.add(ticket)

#     db.session.commit()
#     return jsonify(new_message.to_dict()), 201

@app.route('/messages', methods=['POST'])
def create_message():
    data = request.json
    new_message = Message(
        text=data['text'],
        ticket_id=data['ticket_id'],
        user_id=data.get('user_id'),
        manager_id=data.get('manager_id'),
        status=data['status']
    )
    db.session.add(new_message)
    ticket = Ticket.query.get(data['ticket_id'])
    if ticket and data.get('manager_id'):
        ticket.status = 'accepted'
        db.session.add(ticket)

    db.session.commit()
    return jsonify(new_message.to_dict()), 201


@app.route('/tickets/<int:ticket_id>/messages', methods=['GET'])
def get_ticket_messages(ticket_id):
    messages = Message.query.filter_by(ticket_id=ticket_id).all()
    return jsonify([message.to_dict() for message in messages])


@app.route('/employee/tickets', methods=['GET'])
def get_employee_tickets():
    tickets = Ticket.query.all()
    return jsonify([ticket.to_dict() for ticket in tickets])


if __name__ == '__main__':
    app.run(debug=True)

