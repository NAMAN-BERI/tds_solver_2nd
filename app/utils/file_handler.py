import os
import shutil
import tempfile
from fastapi import UploadFile

async def save_upload_file_temporarily(upload_file: UploadFile) -> str:
    """
    Save an upload file temporarily and return the path to the saved file.
    Modified for Vercel serverless compatibility.
    """
    # Always use /tmp directory for Vercel
    temp_dir = "/tmp"
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        # Create a path to save the file
        file_path = os.path.join(temp_dir, upload_file.filename)
        
        # Save the file
        with open(file_path, "wb") as f:
            contents = await upload_file.read()
            f.write(contents)
        
        # Return the path to the saved file
        return file_path
    except Exception as e:
        # Log the error but we don't need to clean up /tmp
        print(f"Error saving file: {str(e)}")
        raise e