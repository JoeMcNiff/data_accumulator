import uuid
import base64
import tempfile
import os
from config import supabase


def upload_image(file_name: str, image_data, ext: str):
    storage_filename = f"age_classifier/{file_name}{uuid.uuid4()}.{ext}"

    img_bytes = base64.b64decode(image_data)
    with tempfile.NamedTemporaryFile(suffix=f".{ext}", delete=False) as tmp:
        tmp.write(img_bytes)
        tmp_path = tmp.name

    supabase.storage.from_('images').upload(storage_filename, tmp_path)

    os.remove(tmp_path)
    
    # return the location of th image
    return supabase.storage.from_('images').get_public_url(storage_filename)
            
    
    
