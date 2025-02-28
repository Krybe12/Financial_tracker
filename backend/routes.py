from flask import Blueprint, request, jsonify

bp = Blueprint("api", __name__)


@bp.route("/", methods=["GET"])
def main():
    return "hello"