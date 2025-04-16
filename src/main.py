from fastapi import FastAPI
from src.routers import notes
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",  # for local frontend (if you have it on a different port)
    "http://localhost:3000",  # React's default port
    "*",  # Allows all origins (use carefully in production)
]

# Adding CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(notes.router)
