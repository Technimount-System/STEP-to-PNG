from flask import Blueprint, request, jsonify
from util.step_to_mesh import step_to_mesh, download_zoho_file
from util.render import render_mesh_twice
from util.zoho_tools import add_img_to_item, add_images_to_item
from PIL import Image

steps_bp = Blueprint("steps", __name__)

import io

@steps_bp.route("", methods=["POST"])
def step_to_img():
    data = request.get_json(force=True, silent=True)

    if not data:
        return jsonify({"error": "Expected a JSON body"}), 400

    required_fields = ["uri", "token", "item_id", "org_id", "inventory_token"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    step_bytes = download_zoho_file(data["uri"], data["token"]).content

    mesh = step_to_mesh(step_bytes)
    render_mesh_twice(mesh)

    img1 = Image.open("view_front.png")
    img2 = Image.open("view_isometric.png")

    def image_to_bytes(img: Image.Image, fmt: str = "PNG") -> bytes:
        buf = io.BytesIO()
        img.save(buf, format=fmt)
        return buf.getvalue()

    img1_bytes = image_to_bytes(img1)
    img2_bytes = image_to_bytes(img2)


    result2 = add_img_to_item(
        data["item_id"], data["org_id"], data["inventory_token"],
        img2_bytes, filename="isometric.png", content_type="image/png",
    )

    result1 = add_images_to_item(
        data["item_id"], data["org_id"], data["inventory_token"],
        img1_bytes, filename="front.png", content_type="image/png",
    )

    return jsonify({
        "status": "ok",
        "front_upload": result1,
        "isometric_upload": result2,
    }), 200