# test_consultas.py
import builtins
import pytest
from consultas import realizar_consulta

def test_realizar_consulta(monkeypatch):
    inputs = iter(["Luna", "febre e tosse"])  # simula o input do utilizador
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    resultados = []

    def fake_print(mensagem):
        resultados.append(mensagem)

    monkeypatch.setattr(builtins, "print", fake_print)

    realizar_consulta()

    assert any("Levar ao veterinário" in r for r in resultados)
