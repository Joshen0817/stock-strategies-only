from stock_strategies.runtime import get_finmind_token, use_finmind_token


def test_request_token_overrides_and_then_restores_server_token(monkeypatch):
    monkeypatch.setenv("FINMIND_TOKEN", "server-token")

    assert get_finmind_token() == "server-token"
    with use_finmind_token("  browser-token  "):
        assert get_finmind_token() == "browser-token"
    assert get_finmind_token() == "server-token"


def test_empty_request_token_falls_back_to_server_token(monkeypatch):
    monkeypatch.setenv("FINMIND_TOKEN", "server-token")

    with use_finmind_token(""):
        assert get_finmind_token() == "server-token"
