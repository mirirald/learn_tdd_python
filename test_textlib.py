import unittest
from textlib import BodyOfText,Paragraph

class TestBodyOfText(unittest.TestCase):
    def test_empty_story(self):
        with self.assertRaises(ValueError):
            BodyOfText('')
    def test_single_paragraph(self):
        single_paragraph_bot = BodyOfText("Hello, Alex")
        self.assertEqual(1, single_paragraph_bot.num_paragraphs())
        self.assertEqual(["Hello, Alex"], single_paragraph_bot.paragraphs())
    def test_several_paragraphs(self):
        several_paragraphs = BodyOfText("""This is a rather short story. It has three paragraphs.

Once upon a time, a brave princess went on a dangerous journey. She
had many adventures, and recruited other heros to her important and
noble cause.

She prevailed, saving the day, and made it home. Yay!""")
        self.assertEqual(3, several_paragraphs.num_paragraphs())
        self.assertEqual(["This is a rather short story. It has three paragraphs.", """Once upon a time, a brave princess went on a dangerous journey. She
had many adventures, and recruited other heros to her important and
noble cause.""", "She prevailed, saving the day, and made it home. Yay!"], several_paragraphs.paragraphs())
    def test_wordcounts(self):
        testitems = [
            {'text': 'This is a sentence.',
             'counts': {'this': 1, 'is': 1, 'a': 1, 'sentence': 1},
             },
            {'text': 'Truth is beauty; beauty, truth.',
             'counts': {'truth': 2, 'beauty': 2, 'is': 1},
             },
            {'text': 'I could finally SEE. But what I could see, remained a mystery.',
             'counts': {'i': 2, 'could': 2, 'finally': 1, 'see': 2,
                        'but': 1, 'what': 1, 'remained': 1, 'a': 1, 'mystery': 1},
             }
        ]
        for testitem in testitems:
            with self.subTest(text=testitem['text'], counts=testitem['counts']):
                body = BodyOfText(testitem['text'])
                self.assertEqual(testitem['counts'], body.wordcounts())

class TestParagraph(unittest.TestCase):
    def test_empty_paragraph(self):
        with self.assertRaises(ValueError):
            Paragraph('')
    def test_single_sentence(self):
        single_sentence_paragraph = Paragraph('Hello, Alex')
        self.assertEqual(1, single_sentence_paragraph.num_sentences())
    def test_several_sentences(self):
        several_sentences_paragraph = Paragraph('''Hello, Alex
        How is life
        Life is ok''')
        self.assertEqual(3, several_sentences_paragraph.num_sentences())


# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
