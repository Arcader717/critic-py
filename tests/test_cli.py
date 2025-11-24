"""Test basic functions, and if all exist"""
import pytest

def test_main_no_args(capsys, cli):
    cli()
    cap = capsys.readouterr()
    assert "usage: critic" in cap.out

def test_main_help(capsys, cli):
    cli("-h")
    cap = capsys.readouterr()
    assert "usage: critic" in cap.out

def test_version(capsys, cli):
    cli("--version")
    cap = capsys.readouterr()
    assert "critic-py v0.1.0\n" == cap.out

def test_quiet_verbose_exclusive(capsys, cli):
    cli("-q", "-v")
    cap = capsys.readouterr()
    assert "critic: error" in cap.err

def test_base_membership(capsys, cli):
    cli("--preview")
    output = capsys.readouterr().out
    members = ["version", "verbose", "quiet", "preview", "command"]
    for member in members:
        assert member in output

def test_minify_membership(capsys, cli):
    cli("--preview", "minify")
    output = capsys.readouterr().out
    members = [
        "version", "verbose", "quiet", "preview", "command='minify'", "type", "demo",
        "list_patterns", "p"
    ]
    for member in members:
        assert member in output
