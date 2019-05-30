from mindwave.parser import ThinkGearParser, TimeSeriesRecorder

import unittest

class ParserTests(unittest.TestCase):

    def testParser(self):
        s = open("baseline.bytes", mode='r', encoding="ISO-8859-15").read()
        ts_recorder = TimeSeriesRecorder()
        parser = ThinkGearParser(recorders=[ts_recorder])
        parser.feed(s)
        
        self.assertTrue(len(ts_recorder.attention) == len(ts_recorder.meditation) == len(ts_recorder.blink) == len(ts_recorder.poor_signal))

        

def main():
    unittest.main()

if __name__ == '__main__':
    main()
