import requests

def add_img_to_item(
    item_id: str,
    organization_id: str,
    access_token: str,
    image_bytes: bytes,
    filename: str = "item.png",
    content_type: str = "image/png",
) -> dict:
    url = f"https://www.zohoapis.com/inventory/v1/items/{item_id}/image"

    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
    }

    params = {
        "organization_id": organization_id,
    }

    files = {
        "image": (filename, image_bytes, content_type),
    }

    response = requests.post(url, headers=headers, params=params, files=files)
    response.raise_for_status()

    data = response.json()
    if data.get("code") != 0:
        raise RuntimeError(f"Zoho upload failed: {data.get('message')} (code {data.get('code')})")

    return data

def add_back_img_to_item(
    item_id: str,
    organization_id: str,
    access_token: str,
    image_bytes: bytes,
    filename: str = "item.png",
    content_type: str = "image/png",
) -> dict:
    url = f"https://www.zohoapis.com/inventory/v1/items/{item_id}/backimage"

    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
    }

    params = {
        "organization_id": organization_id,
    }

    files = {
        "back_image": (filename, image_bytes, content_type),
    }

    response = requests.post(url, headers=headers, params=params, files=files)
    response.raise_for_status()

    data = response.json()
    if data.get("code") != 0:
        raise RuntimeError(f"Zoho upload failed: {data.get('message')} (code {data.get('code')})")

    return data