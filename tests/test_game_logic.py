from logic_utils import check_guess, update_score, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    # If secret is 50 and guess is 60, hint should be "Too High"
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    # If secret is 50 and guess is 40, hint should be "Too Low"
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_update_score_wrong_guess():
    new_score = update_score(100, "Too High", 1)
    assert new_score == 95

def test_parse_guess_invalid():
    ok, value, error = parse_guess("abc")
    assert ok == False
    assert error == "That is not a number."
    
