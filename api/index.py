try:
    from app.main import app
except Exception as e:
    import logging
    logging.error(f"Error importing app: {str(e)}")
    
    # Create minimal app for debugging
    from fastapi import FastAPI
    app = FastAPI()
    
    @app.get("/{path:path}")
    async def debug(path: str):
        return {"error": "Application failed to load", "details": str(e)}
