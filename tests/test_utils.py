from poldracklab.utils import run_shell_cmd


def test_run_shell_cmd():
    cmd = "echo 'Hello, World!'"
    stdout = run_shell_cmd(cmd)
    assert stdout == ["Hello, World!"]
