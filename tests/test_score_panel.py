from game.score_panel import ScorePanel

def test_score_update():
    sp = ScorePanel()
    sp.handle_score_update("Player1:B1:100")

    assert sp.scores["Player1"] == 100
    assert sp.highscore == 100
    assert sp.highscore_player == "Player1"

def test_multiple_players():
    sp = ScorePanel()
    sp.handle_score_update("Player1:B1:100")
    sp.handle_score_update("Player2:B2:150")

    assert sp.scores["Player1"] == 100
    assert sp.scores["Player2"] == 150
    assert sp.highscore == 150
    assert sp.highscore_player == "Player2"

def test_invalid_message():
    sp = ScorePanel()
    sp.handle_score_update("invalidmessage")  # should not crash

    assert sp.scores == {}
    assert sp.highscore == 0