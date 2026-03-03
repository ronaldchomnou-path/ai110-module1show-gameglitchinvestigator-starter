# ---------------------------------------------------------------
# Pure-logic helpers (copied from app.py so no Streamlit needed)
# ---------------------------------------------------------------

def check_guess(guess, secret):
    if guess == secret:
        return "Win", "Correct!"
    if guess > secret:
        return "Too High", "Go LOWER!"
    else:
        return "Too Low", "Go HIGHER!"


def reset_game(state):
    """Simulates what the New Game button should do."""
    state["attempts"] = 0
    state["status"] = "playing"
    state["secret"] = 61  # fixed for testing
    return state


# ---------------------------------------------------------------
# Bug 1: Hints were wrong for secret=61 with guesses 100->50->25->12->6->3->1
# ---------------------------------------------------------------

def test_hint_sequence_secret_61():
    secret = 61
    guesses_and_expected = [
        (100, "Too High"),
        (50,  "Too Low"),
        (25,  "Too Low"),
        (12,  "Too Low"),
        (6,   "Too Low"),
        (3,   "Too Low"),
        (1,   "Too Low"),
    ]
    for guess, expected_outcome in guesses_and_expected:
        outcome, _ = check_guess(guess, secret)
        assert outcome == expected_outcome, (
            f"guess={guess}, secret={secret}: expected '{expected_outcome}', got '{outcome}'"
        )


# ---------------------------------------------------------------
# Bug 2: New Game button did not reset status, so the game stayed
#         stuck on "won" or "lost" after the game ended.
# ---------------------------------------------------------------

def test_new_game_resets_status_after_win():
    state = {"attempts": 7, "status": "won", "secret": 61}
    state = reset_game(state)
    assert state["status"] == "playing", (
        f"Expected status='playing' after new game, got '{state['status']}'"
    )
    assert state["attempts"] == 0

def test_new_game_resets_status_after_loss():
    state = {"attempts": 7, "status": "lost", "secret": 61}
    state = reset_game(state)
    assert state["status"] == "playing", (
        f"Expected status='playing' after new game, got '{state['status']}'"
    )
    assert state["attempts"] == 0


# for running tests use (in the main directory) : pytest test/test_game_logic.py -v