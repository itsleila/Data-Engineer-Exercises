# ☕ Cafe Sales Data Cleaning & Validation

## Overview

Este projeto tem como objetivo realizar a limpeza e validação de um **dataset transacional com dados "sujos"** de vendas de um café.

O conjunto de dados contém valores ausentes, inconsistências e erros intencionais, simulando cenários reais enfrentados em projetos de engenharia de dados.

O objetivo foi transformar os dados brutos em um dataset **limpo, consistente e pronto para análise**, aplicando boas práticas de engenharia de dados.

---

## Dataset

- **File:** `dirty_cafe_sales.csv`
- **Rows:** 10,000
- **Columns:**
  - transaction_id
  - item
  - quantity
  - price_per_unit
  - total_spent
  - payment_method
  - location
  - transaction_date

---

Este projeto demonstra a construção de um pipeline completo de limpeza e validação de dados, incluindo:

- Padronização
- Tratamento de valores ausentes
- Imputação baseada em regras de negócio
- Tratamento de ambiguidade e dados irrecuperáveis
- Validação de consistência

_Foram realizados testes de qualidade:_

- ✓ Ausência de valores nulos críticos
- ✓ Consistência: `total_spent = quantity × price_per_unit`
- ✓ Ausência de valores inválidos (≤ 0)
- ✓ Ausência de duplicatas
- ✓ Categorias padronizadas

## Principais Insights

- Identificação de dependência entre `item` e `price_per_unit`
- Uso de imputação baseada em regras ao invés de métodos estatísticos
- Preservação da integridade dos dados evitando suposições indevidas

## Output

- Dataset limpo exportado como: `clean_cafe_sales.csv`
