# This imports the REAL FastAPI app (with the /reset and /step endpoints) 
# from your server folder and exposes it to Hugging Face
from server.app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
