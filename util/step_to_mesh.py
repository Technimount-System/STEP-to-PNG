import cadquery as cq
import pyvista as pv
import tempfile, os

def step_to_mesh(step_data):
    with tempfile.NamedTemporaryFile(suffix=".step", delete=False) as tmp:
        tmp.write(step_data)
        tmp.flush()
        os.fsync(tmp.fileno())  # optional, extra safety on some filesystems
        tmp_path = tmp.name

    # do the import after the file is closed
    try:
        shape = cq.importers.importStep(tmp_path)
    finally:
        os.remove(tmp_path)  # since delete=False, clean up yourself

        tmp_stl = os.path.join(tempfile.gettempdir(), "model.stl")

        cq.exporters.export(shape, tmp_stl, angularTolerance=0.1)
        mesh = pv.read(tmp_stl)
        mesh = mesh.clean()  # remove duplicate points/faces

        return mesh

import requests

def download_zoho_file(uri: str, access_token: str) -> requests.Response:
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}"
    }

    response = requests.get(uri, headers=headers)
    response.raise_for_status()

    return response