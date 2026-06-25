import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router

app = FastAPI(
    title="Aeromind AI Service",
    description=("Ai powered flight search",
                 "Using groq api key for nlp task"
                 ),
                 version="0.1.0",
                 docs_url="/docs",
                 redoc_url="/redoc"

)



app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials = True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

app.include_router(router)

@app.get("/healthy")
def health_check():
    return {"status": "ok"}






if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)
