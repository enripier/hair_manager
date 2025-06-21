import pytest
from hair_manager_app import data_manager as data
from hair_manager_app import constantes as c

def test_isvalid_input_valid(monkeypatch):
    inputs = iter(["user@example.com"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = data.isvalid_input("email", c.REGEX_EMAIL)
    assert result == "user@example.com"

def test_isvalid_input_invalid_then_valid(monkeypatch):
    # Simule 3 appels à input dans l'ordre où le code va les faire :
    # 1. "bademail" (premier essai invalide)
    # 2. "y" (réponse au retry: oui on retry)
    # 3. "user@example.com" (2e essai valide)
    inputs = iter(["bademail", "y", "user@example.com"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = data.isvalid_input("email", c.REGEX_EMAIL)
    assert result == "user@example.com"