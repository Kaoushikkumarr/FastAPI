from fastapi import FastAPI
from blog.models import models
from blog.dbConnectors.database import engine
from .routers import blog, user

app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
