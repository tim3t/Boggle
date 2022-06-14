from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """Set up before every test"""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Ensuring information is in session and HTML displaying"""

        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Remaining:', response.data)

        def test_valid_word(self):
            """Test the guessed word to see if it is valid"""

            with self.client as client:
                with client.session_transaction() as sess:
                    sess['board'] = [["C", "A", "T", "T", "T"], 
                                    ["C", "A", "T", "T", "T"], 
                                    ["C", "A", "T", "T", "T"], 
                                    ["C", "A", "T", "T", "T"], 
                                    ["C", "A", "T", "T", "T"]]
            response = self.client.get('/check-word?word=cat')
            self.assertEqual(response.json['result'], 'ok')

        def test_invalid_word(self):
            """Test if guessed word is in dictionary"""

            self.client.get('/')
            response = self.client.get('/check-word?word=impossible')
            self.assertEqual(response.json['result'], 'not-on-board')

        def not_word(self):
            """Test if word is a word"""

            self.client.get('/')
            response - self.client.get('/check-word?word=asdfj;alskdfja;lskdj')
            self.assertEqual(response.json['result'], 'not-word')