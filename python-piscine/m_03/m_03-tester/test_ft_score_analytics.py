import sys
import ft_score_analytics as app


def test_get_scores_reads_sys_argv(monkeypatch):
    args = ["10", "20", "30"]
    print(f"Scenario: read scores from sys.argv"
          f" | args: {args}", file=sys.stderr)
    monkeypatch.setattr(
        app.sys, "argv", ["ft_score_analytics.py", *args])

    argv_list = []
    app.get_scores(argv_list)

    assert argv_list == ["10", "20", "30"]


def test_get_total_score():
    scores = [10, 20, 30]
    print(f"Scenario: total score | args: {scores}", file=sys.stderr)
    assert app.get_total_score(scores) == 60


def test_get_avg_score():
    scores = [10, 20, 30]
    print(f"Scenario: average score | args: {scores}", file=sys.stderr)
    assert app.get_avg_score(scores, 3) == 20.0


def test_get_score_range():
    scores = [10, 20, 30]
    print(f"Scenario: score range | args: {scores}", file=sys.stderr)
    assert app.get_score_range(scores) == 20


def test_test_score_analytics_valid_output(monkeypatch, capsys):
    args = ["5", "15", "25"]
    with capsys.disabled():
        print(f"Scenario: CLI valid input | args: {args}", file=sys.stderr)
        monkeypatch.setattr(app.sys, "argv", ["ft_score_analytics.py", *args])

    app.test_score_analytics()

    output = capsys.readouterr().out
    assert "=== Player Score Analytics ===" in output
    assert "Scores processed: [5, 15, 25]" in output
    assert "Total players: 3" in output
    assert "Total score: 45" in output
    assert "Average score: 15.0" in output
    assert "High score: 25" in output
    assert "Low score: 5" in output
    assert "Score range: 20" in output


def test_test_score_analytics_invalid_output(monkeypatch, capsys):
    args = ["ab", "ac"]
    with capsys.disabled():
        print(f"Scenario: CLI invalid input | args: {args}", file=sys.stderr)
        monkeypatch.setattr(app.sys, "argv", ["ft_score_analytics.py", *args])

    app.test_score_analytics()

    output = capsys.readouterr().out
    assert "=== Player Score Analytics ===" in output
    assert "Invalid parameter: ab" in output
    assert "Scores processed:" not in output


def test_test_score_analytics_large_numbers(monkeypatch, capsys):
    args = ["1500", "2300", "1800", "2100", "1950"]
    with capsys.disabled():
        print("Scenario: CLI large valid numbers | "
              f"args: {args}", file=sys.stderr)
        monkeypatch.setattr(app.sys, "argv", ["ft_score_analytics.py", *args])

    app.test_score_analytics()

    output = capsys.readouterr().out
    assert "=== Player Score Analytics ===" in output
    assert "Scores processed: [1500, 2300, 1800, 2100, 1950]" in output
    assert "Total players: 5" in output
    assert "Total score: 9650" in output
    assert "Average score: 1930.0" in output
    assert "High score: 2300" in output
    assert "Low score: 1500" in output
    assert "Score range: 800" in output


def test_test_score_analytics_decimal_avg_1(monkeypatch, capsys):
    args = ["10", "20", "30", "35"]
    with capsys.disabled():
        print("Scenario: CLI decimal average (23.75) "
              f"| args: {args}", file=sys.stderr)
    monkeypatch.setattr(
        app.sys, "argv", ["ft_score_analytics.py", *args])

    app.test_score_analytics()

    output = capsys.readouterr().out
    assert "=== Player Score Analytics ===" in output
    assert "Scores processed: [10, 20, 30, 35]" in output
    assert "Total players: 4" in output
    assert "Total score: 95" in output
    assert "Average score: 23.75" in output
    assert "High score: 35" in output
    assert "Low score: 10" in output
    assert "Score range: 25" in output


def test_test_score_analytics_decimal_avg_2(monkeypatch, capsys):
    args = ["5", "8", "12"]
    with capsys.disabled():
        print(f"Scenario: CLI decimal average (8.333...) |"
              f" args: {args}", file=sys.stderr)
    monkeypatch.setattr(
        app.sys, "argv", ["ft_score_analytics.py", *args])

    app.test_score_analytics()

    output = capsys.readouterr().out
    assert "=== Player Score Analytics ===" in output
    assert "Scores processed: [5, 8, 12]" in output
    assert "Total players: 3" in output
    assert "Total score: 25" in output
    assert "Average score: 8.333" in output
    assert "High score: 12" in output
    assert "Low score: 5" in output
    assert "Score range: 7" in output


def test_test_score_analytics_empty_input(monkeypatch, capsys):
    args = []
    with capsys.disabled():
        print(f"Scenario: CLI empty input | args: {args}", file=sys.stderr)
        monkeypatch.setattr(app.sys, "argv", ["ft_score_analytics.py"])

    app.test_score_analytics()

    output = capsys.readouterr().out
    assert "No scores provided." in output
