from datetime import datetime
from typing import Optional
from sqlalchemy import Boolean, Column, DateTime, String, Integer, Float, ForeignKey, Date, func, Text
from sqlalchemy.orm import relationship
from database.db import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(150), nullable=False, unique=True)
    hashed_password = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False) 
    created_at = Column(DateTime(timezone=True), default=func.now())

    favorites = relationship("Favorites", back_populates="user")
    


class Authors(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    stories = relationship("StoryBerries", back_populates="author")


class AgeCategories(Base):
    __tablename__ = "age_category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)  

    stories = relationship("StoryBerries", back_populates="age_category")


class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    story_berries_id = Column(Integer, ForeignKey('story_berries.id'), nullable=False)

    user = relationship("Users", back_populates="favorites")
    story_berry = relationship("StoryBerries", back_populates="favorites")



class StoryBerries(Base):
    __tablename__ = "story_berries"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    subtitle = Column(String, nullable=False)
    initial_picture = Column(Text, nullable=True)
    story_reads = Column(Integer, default=0) 
    age_category_id = Column(Integer, ForeignKey('age_category.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())

    # Связи с другими таблицами
    age_category = relationship("AgeCategories", back_populates="stories")
    author = relationship("Authors", back_populates="stories")
    favorites = relationship("Favorites", back_populates="story_berry")
