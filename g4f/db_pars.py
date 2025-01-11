from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, String, Integer, Float, ForeignKey, func, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model.model import *


Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    hashed_password = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    favorites = relationship("Favorites", back_populates="user")


class Authors(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(500), nullable=False)
    photo = Column(Text)
    bio = Column(Text)

    stories = relationship("StoryBerries", back_populates="author")


class AgeCategories(Base):
    __tablename__ = "age_category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)

    stories = relationship("StoryBerries", back_populates="age_category")


class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)

    stories_categories = relationship("StoriesCategory", back_populates="categories")


class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    story_berries_id = Column(Integer, ForeignKey('story_berries.id'), nullable=False)

    user = relationship("Users", back_populates="favorites")
    story_berry = relationship("StoryBerries", back_populates="favorites")


class StoriesCategory(Base):
    __tablename__ = "stories_category"
    id = Column(Integer, primary_key=True, index=True)
    story_berries_id = Column(Integer, ForeignKey('story_berries.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    categories = relationship("Categories", back_populates="stories_categories")
    stories = relationship("StoryBerries", back_populates="stories_categories")


class StoryBerries(Base):
    __tablename__ = "story_berries"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(526), nullable=False)
    title_kz = Column(String(526), nullable=True)
    prologue_kz = Column(Text, nullable=True)
    subtitle = Column(Text, nullable=False)
    subtitle_kz = Column(Text, nullable=True)
    initial_picture = Column(Text)
    story_reads = Column(String(20))
    text = Column(Text, nullable=False)
    text_kz = Column(Text, nullable=True)
    age_category_id = Column(Integer, ForeignKey('age_category.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())

    age_category = relationship("AgeCategories", back_populates="stories")
    author = relationship("Authors", back_populates="stories")
    favorites = relationship("Favorites", back_populates="story_berry")
    stories_categories = relationship("StoriesCategory", back_populates="stories")
