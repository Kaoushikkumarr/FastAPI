from typing import List

from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    description: str


class Base(BlogBase):
    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogBase] = []

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    description: str
    creator: ShowUser

    class Config:
        orm_mode = True
