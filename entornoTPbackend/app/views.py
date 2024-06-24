from flask import jsonify, request
from app.models import Reserva 

def index():
    return jsonify({'message': 'Hello World API Restofinder'})

def create_movie():
    data = request.json
    new_reserva = Reserva(restaurant=data['restaurant'], date=data['date'])
    new_reserva.save()
    return jsonify({'message': 'Reserva creada correctamente'}), 201

def get_all_():
    reservas = Reserva.get_all()
    return jsonify([reserva.serialize() for reserva in reservas])

def get_reserca(reserva_id):
    reserva = Reserva.get_by_id(reserva_id)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404
    return jsonify(reserva.serialize())

def update_reserva(reserva_id):
    reserva = Reserva.get_by_id(reserva_id)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404
    data = request.json
    reserva.restaurant = data['restaurant']
    reserva.date = data['date']
    reserva.save()
    return jsonify({'message': 'Reserva actualizada correctamente'})

def delete_reserva(reserva_id):
    reserva = Reserva.get_by_id(reserva_id)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404
    reserva.delete()
    return jsonify({'message': 'Reserva eliminada correctamennte'})