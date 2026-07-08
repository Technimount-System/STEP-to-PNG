# STEP → STL → Snapshot → Zoho

A lightweight Flask backend that pulls **STEP** files from **Zoho WorkDrive**, converts them to **STL**, renders a snapshot with **PyVista**, and pushes the resulting images straight back into the corresponding item on **Zoho Inventory**.

Trigger it with a single `POST` request, tunnel it through `ngrok`, and let Zoho do the rest.

---

## Pipeline

```
┌──────────────┐     ┌────────────────┐     ┌───────────────┐     ┌──────────────┐     ┌───────────────────┐
│ POST /steps  │ ──▶ │ Download STEP  │ ──▶ │ CadQuery       │ ──▶ │ PyVista       │ ──▶ │ Zoho Inventory     │
│ (item info,  │     │ from Zoho      │     │ STEP → STL     │     │ render + cam  │     │ upload 2 PNGs      │
│  token, url) │     │ WorkDrive      │     │ conversion     │     │ + screenshot  │     │ to item images     │
└──────────────┘     └────────────────┘     └───────────────┘     └──────────────┘     └───────────────────┘
```

1. **Trigger** — an authenticated `POST` hits `/steps` with the Zoho WorkDrive download URL + access token for the target STEP file.
2. **Fetch** — the STEP file is downloaded from Zoho WorkDrive.
3. **Convert** — `cadquery` imports the STEP geometry and exports it as `.stl`.
4. **Render** — `pyvista` loads the STL into a scene, positions a camera, and captures **two PNG screenshots** (e.g. isometric + front view).
5. **Upload** — the generated images are pushed to the matching part's page via the **Zoho Inventory Images API**.

End result: every part with a STEP file in WorkDrive gets an auto-generated preview image on its Inventory item — no manual screenshotting required.

---

## Tech Stack

| Layer | Tool |
|---|---|
| Web framework | [Flask](https://flask.palletsprojects.com/) |
| CAD conversion | [CadQuery](https://cadquery.readthedocs.io/) |
| 3D rendering | [PyVista](https://pyvista.org/) |
| Tunneling | [ngrok](https://ngrok.com/) |
| Inventory sync | [Zoho Inventory API](https://www.zoho.com/inventory/api/v1/) |
| File source | [Zoho WorkDrive API](https://www.zoho.com/workdrive/api/) |

---

## Getting Started

### 1. Clone & install

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```


### 3. Run the server

```bash
python main.py
```
Then, in another terminal, run
```bash
ngrok http 5000
```

This launches Flask and opens an ngrok tunnel, printing your public URL to the console:



---

## API

### `POST /steps`

Downloads a STEP file, converts + renders it, and uploads the resulting images to a Zoho Inventory item.

**Request body**

```json
{
  "token": "zoho-workdrive-token",
  "uri": "https://download.zoho.com/v1/workdrive/download/Part-Name",
  "item_id": "Part-ID",
  "org_id": "Org-ID",
  "inventory_token": "Inventory-Token"
}
```

**Response**

```json
{
    "status": "ok",
    "front_upload": img1,
    "isometric_upload": img2
}
```
