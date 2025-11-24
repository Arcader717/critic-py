import pytest

new_line_whitespace = """
a {
    font-size: 5px;
}
"""

good_output = "a{font-size:5px}"

def test_comments(capsys, cli, css_patterns, tmp_path):
    single_line_comment = "a{font-size:5px}/*comment*/"
    d = tmp_path / "static"
    d.mkdir()
    p = d / "test.css"
    css_patterns.overwrite(p.as_posix())

    p.write_text(single_line_comment)
    cli("minify")
    output = capsys.readouterr().out
    assert f"Parsed and minified {p.as_posix()}" in output
    assert p.read_text() == good_output

    multi_line_comment = "a{font-size:5px}/*multi\nline\ncomment\n*/"
    p.write_text(multi_line_comment)
    cli("minify")
    output = capsys.readouterr().out
    assert f"Parsed and minified {p.as_posix()}" in output
    assert p.read_text() == good_output

def test_whitespace(capsys, cli, css_patterns, tmp_path):
    single_line_whitespace = "a {font-size: 5px}"
    d = tmp_path / "static"
    d.mkdir()
    p = d / "test.css"
    css_patterns.overwrite(p.as_posix())

    p.write_text(single_line_whitespace)
    cli("minify")
    output = capsys.readouterr().out
    assert f"Parsed and minified {p.as_posix()}" in output
    assert p.read_text() == good_output

    p.write_text(new_line_whitespace)
    cli("minify")
    output = capsys.readouterr().out
    assert f"Parsed and minified {p.as_posix()}" in output
    assert p.read_text() == good_output

every_test = """
a {
    font-size: 500px;
    background-color: black;

    /* Might edit later */
    &:hover {
        background-color: gray;
    }

    hr {
        content: 'x';
    }
}

/*
 * #id {
 *     background: white;
 * }
 */
"""

every_test_good = "a{font-size:500px;background-color:black}a:hover{background-color:gray}a hr{content:'x'}"

def test_multiple_rules(capsys, cli, css_patterns, tmp_path):
    d = tmp_path / "static"
    d.mkdir()
    p = d / "test.css"
    p.write_text(every_test)
    css_patterns.overwrite(p.as_posix())

    cli("minify")
    output = capsys.readouterr().out
    assert f"Parsed and minified {p.as_posix()}" in output
    assert p.read_text() == every_test_good
