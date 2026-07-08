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

def add_images_to_item(
    item_id: str,
    organization_id: str,
    access_token: str,
    image_bytes: bytes,
    filename: str = "item.png",
    content_type: str = "image/png",
    document_ids: str | None = None,
    remove_all: bool | None = None,
    update_primary_image: bool | None = None,
) -> dict:
    url = f"https://www.zohoapis.com/inventory/v1/items/{item_id}/images"

    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
    }

    params = {
        "organization_id": organization_id,
    }
    if document_ids is not None:
        params["document_ids"] = document_ids
    if remove_all is not None:
        params["remove_all"] = str(remove_all).lower()
    if update_primary_image is not None:
        params["update_primary_image"] = str(update_primary_image).lower()

    files = {
        "image": (filename, image_bytes, content_type),
    }

    response = requests.post(url, headers=headers, params=params, files=files)
    response.raise_for_status()

    data = response.json()
    if data.get("code") != 0:
        raise RuntimeError(f"Zoho upload failed: {data.get('message')} (code {data.get('code')})")

    return data