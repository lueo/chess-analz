# -*- encoding: utf-8 -*-

import subprocess, time

class Engine:

    def __init__(self):
        self.cmd = 'stockfish'
        self.engine = subprocess.Popen(
                self.cmd,
                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                universal_newlines=True,
                )

    def put(self, command):
        print('\nyou:\n\t'+command)
        self.engine.stdin.write(command+'\n')

    def get(self):
    # using the 'isready' command (engine has to answer 'readyok')
    # to indicate current last line of stdout
        self.engine.stdin.write('isready\n')
        print('\nengine:')
        while True:
            text = self.engine.stdout.readline().strip()
            if text == 'readyok':
                break
            if text !='':
                print('\t'+text)
        return text

if __name__ == '__main__':
    e = Engine()
    e.put('uci')
    e.get()
    e.put('isready')
    e.get()
    e.put('ucinewgame')
    e.get()
    e.put('setoption name UCI_AnalyseMode value true')
    e.get()
    e.put('setoption name Threads value 4')
    e.get()
    e.put('setoption name Hash value 256')
    e.get()
    e.put('position fen r1b1k1nr/p5pp/5p2/1Bn1p3/5B2/P7/1PP2PPP/2KR2NR b - - 1 14')
    e.get()
    while True:
        e.put('go infinite')
        e.get()
        time.sleep(3)

