# 📘 Atividade: Testes Automatizados com pytest

## 🎯 Objetivo

Crie uma suíte de testes automatizados para validar funções Python usando pytest. Pratique asserções, parametrização de casos de teste e verificação de exceções sem alterar o módulo que será testado.

## 📝 Tarefas

### 🛠️ Escrever testes básicos

#### Descrição
Instale pytest com `python -m pip install pytest` e, no diretório desta atividade, crie `test_math_utils.py` para testar as funções `add` e `is_even` de `math_utils.py`.

#### Requisitos
O programa concluído deve:

- Conter funções de teste cujos nomes comecem com `test_`.
- Usar `assert` para verificar a soma de dois números positivos e identificar números pares e ímpares.
- Executar os testes com `python -m pytest -v` e obter resultado aprovado.

### 🛠️ Parametrizar diferentes casos

#### Descrição
Amplie a suíte para testar vários valores de `is_even` e `average` usando `pytest.mark.parametrize`.

#### Requisitos
O programa concluído deve:

- Usar `pytest.mark.parametrize` para executar cada função de teste com mais de um conjunto de valores.
- Verificar a média de listas com valores inteiros, valores decimais e um único valor.
- Manter os testes independentes, sem depender da ordem em que são executados.

### 🛠️ Testar erros esperados

#### Descrição
Teste como `average` e `divide` se comportam diante de entradas inválidas, verificando as exceções esperadas com pytest.

#### Requisitos
O programa concluído deve:

- Usar `pytest.raises(ValueError)` para verificar que `average([])` gera um erro.
- Usar `pytest.raises(ValueError)` para verificar que `divide(10, 0)` gera um erro.
- Executar a suíte completa com `python -m pytest -v` e confirmar que todos os testes passam.
