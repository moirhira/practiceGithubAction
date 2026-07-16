from weather import get_weather
import pytest


def test_missing_key(monkeypatch):
    monkeypatch.setattr("weather.API_KEY", None)
    with pytest.raises(RuntimeError):
        get_weather("London")
