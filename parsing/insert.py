from sqlalchemy.exc import IntegrityError
from model.model import *

from parsing.db_config import DatabaseManager


class Inserting:
    def __init__(self):
        db_manager = DatabaseManager()
        self.session = db_manager.Session()

    def insert_story_berries(self, story_data):
        try:
            existing_story_berries = self.session.query(StoryBerries).filter_by(
                title=story_data['title'],
            ).first()
            
            if not existing_story_berries:
                new_story_berries = StoryBerries(
                    title=story_data['title'],
                    duration=story_data['duration'],
                    link=story_data['link'],
                    initial_picture=story_data['initial_picture'],
                    story_reads=story_data['story_reads'],
                    age_category_id=int(self.insert_age_categories(story_data)),
                    author_id=int(self.insert_author(story_data)),
                    category_id=int(self.insert_categories(story_data)),


                )
                self.session.add(new_story_berries)
                self.session.commit()

                return new_story_berries.id 
            else:

                return existing_story_berries.id
        except IntegrityError:
            self.session.rollback()
            raise
        finally:
            self.session.close()


    def insert_author(self, story_data):
        try:
            existing_author = self.session.query(Authors).filter_by(
                author_name = story_data['author_name']
            ).first()
            if not existing_author:
                new_author = Authors(
                    author_name=story_data['author_name'],
                    author_logo=story_data['author_logo'],
                    author_bio=story_data['author_bio']
                )
                self.session.add(new_author)
                self.session.commit()

                return new_author.id
            else:

                return existing_author.id
        except IntegrityError:
            self.session.rollback()
            raise
        finally:
            self.session.close()


    def insert_age_categories(self, story_data):
        try:
            existing_age_category = self.session.query(AgeCategories).filter_by(
                name = story_data['age_category'],
            ).first()
            if not existing_age_category:
                new_age_category = AgeCategories(
                    name = story_data['age_category'],
                )
                self.session.add(new_age_category)
                self.session.commit()
                return new_age_category.id
            else:
                return existing_age_category.id
        except IntegrityError:
            self.session.rollback()
            raise
        finally:
            self.session.close()


    def insert_categories(self, story_data):
        try:
            existing_category = self.session.query(Categories).filter_by(
                name_categories = story_data['category']
            ).first()
            if not existing_category:
                new_category = Categories(
                    name_categories = story_data['category']
                )
                self.session.add(new_category)
                self.session.commit()
                return new_category.id
            else:
                return existing_category.id
        except IntegrityError:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    


    def insert_stories_category(self, story_data):
        try:
            existing_stories_category = self.session.query(StoriesCategory).filter_by(
                story_berries_id=int(self.insert_story_berries(story_data)),
                category_id=int(self.insert_categories(story_data)),
            ).first()
            if not existing_stories_category:
                new_stories_category = StoriesCategory(
                    story_berries_id=int(self.insert_story_berries(story_data)),
                    category_id=int(self.insert_categories(story_data)),
                )
                self.session.add(new_stories_category)
                self.session.commit()
                return new_stories_category.id
            else:
                return existing_stories_category.id
        except IntegrityError:
            self.session.rollback()
            raise
        finally:
            self.session.close()
   