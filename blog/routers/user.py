from fastapi import APIRouter
from fastapi import Depends, status
from ..contoller import schema
from sqlalchemy.orm import Session
from ..repository import user
from blog.dbConnectors.database import get_db

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.post('/', response_model=schema.ShowUser)
def create_user(users: schema.User, db: Session = Depends(get_db)):
    return user.create(users, db)


@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=schema.ShowUser)
def fetch_user(user_id: int, db: Session = Depends(get_db)):
    return user.show_user(user_id, db)
