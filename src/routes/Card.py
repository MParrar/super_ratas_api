from flask import Blueprint, jsonify, request
from models.entities.Buyer import Buyer

# Entities
from models.entities.Card import Card
# Models
from models.CardModel import CardModel


main = Blueprint('card_blueprint', __name__)


@main.route('/')
def get_cards():
    try:
        cards = CardModel.get_cards()
        return jsonify(cards)
    except Exception as ex:
        return jsonify({'msj': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_card():
    try:
        price = request.json['price']
        observation = request.json['observation']
        points = request.json['points']
        user_id = request.json['user_id']
        category_id = request.json['category_id']
        status_id = request.json['status_id']
        created_date = request.json['created_date']
        print(user_id)
        card = Card(None, price, observation, points, user_id, category_id,
                    status_id, created_date,)
        affected_rows = CardModel.add_card(card)
        if affected_rows == 1:
            return jsonify({"status": True})
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/change-status/<id>', methods=['PUT'])
def change_status_card(id):
    try:
        status_id = request.json['status_id']
        updated_date = request.json['updated_date']
        card = Card(id, None, None, None, None, None,
                    status_id, None, updated_date)
        affected_rows = CardModel.change_status_card(card)

        if affected_rows == 1:
            return jsonify(card.id)
        else:
            return jsonify({'message': "No Card deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_category(id):
    try:
        price = request.json['price']
        observation = request.json['observation']
        points = request.json['points']
        user_id = request.json['user_id']
        category_id = request.json['category_id']
        status_id = request.json['status_id']
        card = Card(id, price, observation, points, user_id, category_id,
                    status_id)
        affected_rows = CardModel.update_card(card)

        if affected_rows == 1:
            return jsonify(card.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/buy', methods=['POST'])
def add_status():
    try:
        user_id = request.json['user_id']
        card_id = request.json['card_id']
        print(user_id)
        print(card_id)
        buyer = Buyer(None, user_id, card_id)
        affected_rows = CardModel.add_buyer(buyer)
        if affected_rows == 1:
            return jsonify({"status": True})
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/filter-category/<category>')
def get_cards_by_category(category):
    try:
        cards = CardModel.get_cards_by_category(category)
        return jsonify(cards)
    except Exception as ex:
        return jsonify({'msj': str(ex)}), 500


@main.route('/buyer', methods=['POST'])
def get_buyers():
    try:
        card_id = request.json['card_id']
        buyer = Buyer(None, None, card_id)

        buyers = CardModel.get_buyer(buyer)
        return jsonify(buyers)
    except Exception as ex:
        return jsonify({'msj': str(ex)}), 500


@main.route('/filter-status/<status>')
def get_cards_by_status(status):
    try:
        cards = CardModel.get_cards_by_status(status)
        return jsonify(cards)
    except Exception as ex:
        return jsonify({'msj': str(ex)}), 500
