from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.wsgi import WSGIMiddleware

app = FastAPI()
# wsgi_app = WSGIMiddleware(app)


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Définir une route POST avec des paramètres
@app.post("/users/{user_id}")
async def create_user(user_id: int, name: str):
    # Logique pour créer l'utilisateur avec l'ID et le nom fournis
    
    return {"message": f"Utilisateur créé avec l'ID {user_id} et le nom {name}"}

# Exécutez l'application avec uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="172.19.120.188", port=8000)