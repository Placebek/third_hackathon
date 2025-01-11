from sqlalchemy.exc import IntegrityError
from db_config import DatabaseManager
from db_pars import *


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
                    subtitle=story_data['subtitle'],
                    text=story_data['text'],
                    initial_picture=story_data['initial_picture'],
                    story_reads=story_data['story_reads'],
                    age_category_id=int(self.insert_age_categories(story_data)),
                    author_id=int(self.insert_author(story_data)),


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
    

    def update_story_berries(self, story_data):
        try:
            story_berries = self.session.query(StoryBerries).where(
                StoryBerries.title == story_data['title']
            ).one_or_none()
            
            if story_berries and story_berries.text is None:
                story_berries.text = story_data['text']
                self.session.commit()
                return story_berries.id
            elif story_berries:
                return story_berries.id
            else:
                return None
        except IntegrityError:
            self.session.rollback()
            raise


    def insert_author(self, story_data):
        try:
            existing_author = self.session.query(Authors).filter_by(
                name = story_data['author_name']
            ).first()
            if not existing_author:
                new_author = Authors(
                    name=story_data['author_name'],
                    photo=story_data['author_photo'],
                    bio=story_data['author_bio']
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
                name = story_data['category_name']
            ).first()
            if not existing_category:
                new_category = Categories(
                    name = story_data['category_name']
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
   