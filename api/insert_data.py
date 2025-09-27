from data_accumulator.config import MANIFEST_TABLE, supabase

def insert_data(file_path: str, image_class: str, image_group: str, weight: str):
    manifest_data = {
        "image_path": file_path,
        "image_class": image_class,
        "image_group": image_group,
        "weight": weight
    }
    supabase.table(MANIFEST_TABLE).insert(manifest_data).execute()
        

