from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
MANIFEST_TABLE = os.getenv("MANIFEST_TABLE")

supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

