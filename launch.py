import os

import uvicorn
import threading
from webui import app

def run_fastapi():
    # FastAPI
    os.environ["TTS_FP16"] = "0"
    os.environ["TTS_DEVICE"] = "cuda"

    # Run the server
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8060,
        reload=False,
        log_level="info"
    )

def main():
    # Start FastAPI in a new thread
    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.start()

    # WebUI
    app.queue(20)
    app.launch(server_name="0.0.0.0", server_port=8066)


if __name__ == "__main__":
    main()