# SmartCare 🏠
### Projeto - UniFECAF

Gestão inteligente de manutenção de equipamentos domésticos.

# Sobre o projeto

O SmartCare é um projeto acadêmico desenvolvido com a proposta de tornar a gestão da manutenção de equipamentos domésticos mais simples e organizada, dentro do conceito de Smart Home 2050.

A solução busca ajudar moradores a acompanhar as manutenções preventivas de seus equipamentos, evitando esquecimentos e contribuindo para aumentar sua vida útil.

# Problema identificado

Muitas pessoas esquecem de realizar a manutenção periódica de seus equipamentos domésticos, não possuem um histórico organizado e acabam realizando manutenções somente quando ocorre algum problema.

Essa falta de acompanhamento pode causar gastos inesperados, reduzir a vida útil dos equipamentos e comprometer seu funcionamento.

# Nossa solução

O SmartCare propõe uma plataforma para cadastrar equipamentos domésticos, registrar manutenções e acompanhar automaticamente os prazos recomendados para novas manutenções.

Com o auxílio da programação e da automação, o sistema permite identificar quais equipamentos estão em dia, próximos do vencimento ou com a manutenção atrasada.

## ⚙️ Funcionalidades

- Cadastro de equipamentos domésticos.
- Registro da última manutenção realizada.
- Definição do intervalo entre manutenções.
- Cálculo da próxima manutenção.
- Classificação automática do status:
  | Em dia. |
  | Próxima do vencimento. |
  | Atrasada. |
- Acompanhamento das manutenções.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
|---|---|
| Bubble | Desenvolvimento da plataforma No-Code |
| Python | Desenvolvimento do algoritmo de cálculo de manutenção |
| n8n | Automação e classificação dos equipamentos |
| JavaScript | Cálculos executados dentro do workflow n8n |
| Git e GitHub | Versionamento, armazenamento e documentação do projeto |

## 🐍 Algoritmo em Python

O projeto possui um algoritmo desenvolvido em Python para calcular a próxima manutenção dos equipamentos.

O algoritmo recebe três informações:
- Nome do equipamento.
- Data da última manutenção.
- Intervalo recomendado entre manutenções, em dias.

Com esses dados, calcula a próxima data de manutenção, determina quantos dias faltam e classifica a situação do equipamento.

**Arquivo principal:** `python/manutencao.py`

## 🔄 Automação com n8n

Foi desenvolvido um workflow no n8n para automatizar a análise dos equipamentos.

O fluxo executa as seguintes etapas:

1. Inicia a automação por meio de um Manual Trigger.
2. Busca o arquivo CSV armazenado no GitHub usando HTTP Request.
3. Extrai os dados dos equipamentos com Extract From File.
4. Calcula os dias restantes utilizando JavaScript no nó Code.
5. Classifica os equipamentos por meio de condições IF.
6. Define o status de cada equipamento com Edit Fields.
7. Reúne os resultados em uma única saída utilizando Merge.

A automação utiliza o arquivo `n8n/equipamentos.csv` como fonte de dados e possui seu workflow exportado em `n8n/automacao.json`.

## 📁 Estrutura do projeto

```text
smartcare-project/
│
├── docs/
│
├── n8n/
│   ├── automacao.json
│   └── equipamentos.csv
│
├── python/
│   └── manutencao.py
│
├── screenshots/
│
└── README.md

```markdown
# 👥 Equipe

Projeto acadêmico desenvolvido por uma equipe de dois integrantes da UniFECAF.

Cada integrante contribui para o desenvolvimento da solução, envolvendo planejamento, construção da plataforma, programação e automação.

## 🎓 Contexto acadêmico

O SmartCare foi desenvolvido no contexto do tema Smart Home 2050, aplicando conceitos de:

- Product Management.
- Desenvolvimento No-Code.
- Automação Low-Code.
- Lógica de programação com Python.
- Integração de ferramentas digitais.
- Versionamento com Git e GitHub.
- Organização de atividades utilizando conceitos de metodologias ágeis.

---

**SmartCare — Tecnologia a favor do cuidado com sua casa.**