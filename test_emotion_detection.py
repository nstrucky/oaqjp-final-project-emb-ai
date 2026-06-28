""" This tests the emotion_detector capabilities in EmotionDetection """
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """ Class to test emotion_detector """

    def test1(self):
        """ Contains test cases for all five emotions in emotion_detector """

        self.assertEqual("joy",
            emotion_detector("I am glad this happened")["dominant_emotion"])
        self.assertEqual("anger",
            emotion_detector("I am really mad about this")["dominant_emotion"])
        self.assertEqual("disgust",
            emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"])
        self.assertEqual("sadness",
            emotion_detector("I am so sad about this")["dominant_emotion"])
        self.assertEqual("fear",
            emotion_detector("I am afraid that this will happen")["dominant_emotion"])

unittest.main()
