from flask import url_for
from flask_testing import TestCase

import os
from application import app, db
from application.models import Tasks

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URI'),
            SECRET_KEY=os.getenv('TEST_SECRET'),
            DEBUG=True,
            WTF_CRSF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()

        sample1 = Tasks(description='This is a test task')

        sample2 = Tasks(description='This is a completed task', complete=True)

        db.session.add(sample1)
        db.session.commit()
        db.session.add(sample2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'This is a test task', response.data)

    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Description of task', response.data)

    def test_update_get(self):
        response = self.client.get(url_for('update', number = 1))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Original task', response.data)

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('add'),
            data = dict(description='This should be added'),
            follow_redirects=True
        )
        self.assertIn(b'This should be added',response.data)

class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(
            url_for('delete', number = 2),
            follow_redirects=True
        )
        self.assertNotIn(b'This is a completed task',response.data)

class TestUpdate(TestBase):
    def test_update_post(self):
        response = self.client.post(
            url_for('update', number = 1),
            data = dict(description='This has been updated'),
            follow_redirects=True
        )
        self.assertIn(b'This has been updated',response.data)