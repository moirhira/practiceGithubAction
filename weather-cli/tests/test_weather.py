from weather import get_weather
import pytest

def test_missing_key(monkeypatch):
	monkeypatch.setattr("weather.API_KEY", None)
	with pytest.raises(RuntimeError):
		get_weather("London")

def test_invalid_api_key(monkeypatch):
	class Response:
		status_code = 401

	monkeypatch.setattr("weather.API_KEY", "test-key")
	monkeypatch.setattr("weather.requests.get", lambda *args, **kwargs: Response())
	with pytest.raises(RuntimeError, match="Invalid API key"):
		get_weather("Rabat")
