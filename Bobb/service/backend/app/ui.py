from pathlib import Path
from flask import Blueprint, send_from_directory, redirect, Response

MAIN_DIR = Path(__file__).parent.absolute()

ui = Blueprint("ui", __name__)

static_folder = f"{MAIN_DIR}/ui"
assets_folder = f"{static_folder}/assets"

@ui.route("/")
def serve_index() -> Response:
    return send_from_directory(static_folder, "index.html")


@ui.route("/pizza.svg")
def serve_favicon() -> Response:
    return send_from_directory(static_folder, "pizza.svg")

@ui.route("/assets/<path:path>")
def serve_assets(path: str) -> Response:
    return send_from_directory(assets_folder, path)


# Return 'index.html' for everything else
@ui.route("/<path:path>")
def catch_all(path: str) -> Response:
    return send_from_directory(static_folder, "index.html")
