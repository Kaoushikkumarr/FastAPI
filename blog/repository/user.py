from fastapi import status, HTTPException
from .. import models
from ..contoller import schema
from ..hashPassword import hashing
from sqlalchemy.orm import Session
from blog.models import models


def create(user: schema.User, db: Session):
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hashing.HashingPassword.bcrypt(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show_user(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Id Not Found')
    return user
