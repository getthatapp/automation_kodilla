from flask import Flask, abort, request, jsonify

from .utilities import tic_tac_toe_winner

app = Flask(__name__)


@app.route('/winner', methods=['GET'])
def winner():
    board = request.args.get('board', '').replace('_', ' ')
    try:
        return jsonify({
            'winner': tic_tac_toe_winner(board)
        })
    except ValueError:
        abort(400)
