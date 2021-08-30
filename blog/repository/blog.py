from .. import models
from ..contoller import schema
from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from blog.models import models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(blog: schema.BlogBase, db: Session):
    new_blog = models.Blog(title=blog.title, description=blog.description, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(blog_id: int, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog Id Not Found')
    blogs.delete(synchronize_session=False)
    db.commit()
    return {'response': 'Deleted'}


def update(blog_id: int, blogs: schema.BlogBase, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog Id Not Found')
    blog.update(
        {
            "title": blogs.title,
            "description": blogs.description,
        }
    )
    db.commit()
    return {'response': 'Blog Updated'}


def show_all_blogs(blog_id: int, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog Id Not Found')
    return blogs
