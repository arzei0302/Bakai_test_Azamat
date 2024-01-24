#     curl http://localhost:5000/ticket_types
#     curl http://127.0.0.1:5000//userticket
#     curl -X POST http://localhost:5000/tickets \ -H "Content-Type: application/json" \ -d '{"text": "Перевод в МБанк отклонен, но деньги списались с карты", "ticket_type_id": 1, "user_id": 1}'
#     curl -X POST http://localhost:5000/messages -H "Content-Type: application/json" -d '{"text": "Ответили", "ticket_id": 6, "user_id": 1, "manager_id": 1, "status": "accepted"}'
#     curl http://localhost:5000/tickets/6/messages
#     curl http://localhost:5000/employee/tickets

