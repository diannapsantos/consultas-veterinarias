# Sistema Interativo de Consultas Veterinárias

Este projeto foi desenvolvido como parte da avaliação do módulo **Projeto de Programação**, integrado na formação de **Linguagem de Programação em Python**.

---

## Objetivo

Criar uma aplicação interativa em Python para simular o registo e a gestão de consultas veterinárias para animais de estimação, de forma simples e funcional.

---

## Funcionalidades

- Registo de animais  
- Registo de sintomas  
- Recomendações com base nos sintomas  
- Armazenamento local com ficheiros `.csv`  
- Testes com `pytest` 

---

## Como executar

1. **Clonar o repositório:**

```bash
git clone https://github.com/diannapsantos/consultas-veterinarias.git
cd consultas-veterinarias
```

## Requisitos

- Python: 3.13.5
- Bibliotecas: pandas, numpy, matplotlib, openpyxl

## Estrutura do Projeto 

consultas-veterinarias/
- main.py (Ficheiro principal com o menu interativo)
- interface.py (Interface via terminal)
- interface_gui.py (Interface gráfica com tkinter)
- animais.py (Módulo de registo de animais)
- dados.py (Leitura/escrita de dados)
- consultas.py (Lógica das consultas e recomendações)
- test_consultas.py (Testes unitários com pytest)
- requirements.txt (Bibliotecas necessárias)
          
## Autora
Diana Santos

## Licença
Este projeto é apenas para fins académicos e não possui licença comercial.


