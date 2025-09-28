This is the code for a small api server which will take json requests containing images (as base64), data labels (classes), and a file name and inserts them into your supabase database.

Few things to note:

Start Command for this app (when deploying on remote server): 
'''gunicorn api.webhook:app'''

You must set the following Enviroment Variables:
1) SUPABASE_URL (The url of your supabase project)
2) SUPABASE_SERVICE_KEY (The service key of supabase project)
3) MANIFEST_TABLE (The name of the table you want to track the manifest data in)

Important customization notes:
1) If you want to change the fields in your manifest table to be different fromt he ones this server is inserting into, you must manually do it in insert_data.py
2) If you care about what the images are named either make sure you send the right name or modify this code to give it the porper naming conventions
3) For the data_classes you can send whatever to this server and it will save whatever class you sent in your manifest table