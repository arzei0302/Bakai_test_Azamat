# init_db.py
# from app import app, db
# from models import User, Employee

# with app.app_context():
#     user1 = User(name='Bakaibek', email='bakaibek@example.com')
#     user2 = User(name='Bakaigul', email='bakaigul@example.com')
#     employee = Employee(name='Bankman')
#     employee = Employee(name='Bankbek')
    

#     db.session.add(user1)
#     db.session.add(user2)
#     db.session.add(employee)
#     db.session.commit()
    
    
    
# with app.app_context():
#     user_to_update = User.query.filter_by(name='Bakaibek').first()
#     if user_to_update:
#         user_to_update.email = 'new_email@example.com' 
#         db.session.commit()
        
        
# with app.app_context():
#     user_to_delete = User.query.filter_by(name='Bakaigul').first()
#     if user_to_delete:
#         db.session.delete(user_to_delete)
#         db.session.commit()


