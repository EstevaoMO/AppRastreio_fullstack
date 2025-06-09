from fastapi import FastAPI
from routes import pedido_router, usuario_router, possui_router

app = FastAPI()

# Rotas
app.include_router(pedido_router.router, prefix="/pedidos", tags=["Pedidos"])
app.include_router(usuario_router.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(possui_router.router, prefix="/associacoes", tags=["Associacoes"])