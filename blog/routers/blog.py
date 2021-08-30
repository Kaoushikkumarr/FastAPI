from fastapi import APIRouter
from fastapi import Depends, status
from ..contoller import schema
from sqlalchemy.orm import Session
from ..repository import blog

from blog.dbConnectors.database import get_db

router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)


@router.get('/', response_model=schema.ShowBlog)
def all_blogs(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.get('/{blog_id}', status_code=status.HTTP_200_OK, response_model=schema.ShowBlog)
def all_blogs(blog_id: int, db: Session = Depends(get_db)):
    return blog.show_all_blogs(blog_id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(blogs: schema.BlogBase, db: Session = Depends(get_db)):
    return blog.create(blogs, db)


@router.put('/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id: int, blogs: schema.BlogBase, db: Session = Depends(get_db)):
    return blog.update(blog_id, blogs, db)


@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blogs(blog_id: int, db: Session = Depends(get_db)):
    return blog.delete(blog_id, db)
