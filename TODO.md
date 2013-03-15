TODO list
===

- [x] Change subprocess to QProcess.
- [x] <del>Using Thread to launch engine in background.</del> (Don't need anymore since QProcess is sig-slot model)
- [x] <del>Using Queue to launch many engines.</del> (Don't need, as above)
- [ ] Show threat in depth 5 by using null-move technique.
- [ ] Streaming Stockfish UCI protocol to QTextBrowser. Lively.
- [ ] Parse UCI info lines to get PV and score (may refer to PyGTK, scid)
- [ ] Send PV and score to local browser via Socket.io (using python-gevent-socketio)
- [ ] Load PGN game from browser and show computer analysis. Lively.
- [ ] Polish client. (Minimize to tray, dashboard, settings, status... etc)
- [ ] Establish central server to store games.
- [ ] Server games could be analyzed by different engines and compare scores.
- [ ] Each move in every game could be analyzed by different engines.
- [ ] Convert the client as a node to analyze any given position.
- [ ] Giant chess computer cluster!
