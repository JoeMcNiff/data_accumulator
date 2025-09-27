from supabase import create_client
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

def download_image(file_name: str, image_data):
    storage_filename = f"{file_name}/{uuid.uuid4()}.jpg"
    supabase.storage.from_('images/age_classifier').upload(storage_filename, image_data)
    
    # return the location of th image
    return supabase.storage.from_('images/age_classifier').get_public_url(storage_filename)
            
    
    
