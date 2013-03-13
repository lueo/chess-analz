TODO list
===

    0. Change subprocess to QProcess.
    1. Using Thread to launch engine in background.
    2. Using Queue to launch many engines.
    3. Show threat in depth 5 by using null-move technique.

    1. Streaming Stockfish UCI protocol to QTextBrowser. Lively.
    2. Parse UCI info lines to get PV and score (may refer to PyGTK, scid)
    3. Send PV and score to local browser via Socket.io (using python-gevent-socketio) 
    4. Load PGN game from browser and show computer analysis. Lively.
    5. Polish client. (Minimize to tray, dashboard, settings, status... etc)
    6. Establish central server to store games.
    7. Server games could be analyzed by different engines and compare scores.
    8. Each move in every game could be analyzed by different engines.
    9. Convert the client as a node to analyze any given position.
    10. Giant chess computer cluster!
