# Introdução a Programação 1 (LC/UFRPE)
## Projeto 2 VA

O trabalho pode ser feito individualmente ou em dupla.

### Equipe
* Claudia ...
* Antonio Raul

### Descrição
Neste projeto, o seu objetivo consiste em construir um pequeno sistema em Python. Marque com um `[ X ]` a opção de projeto que será realizado pela sua equipe na seção abaixo.

* `[ ]` Sistema de buscas em arquivos de texto
* `[X]` Sistema de cadastros de monitoria
* `[ ]` Outro projeto (incluir descrição na seção abaixo)

### Projetos

### Projeto 1: Sistema de buscas em arquivos de texto
Fluxo de uso:
1. O usuário disponibiliza uma interface (linha de comando ou GUI), na qual o usuário indica uma pasta do seu computador para ser indexada pelo sistema de buscas.
2. O sistema realiza o mapeamento das palavras presentes em cada arquivo txt da pasta (indexação)
3. O sistema mantém um 'prompt' disponível de consulta para o usuário digitar os termos a serem buscados.
4. Após a busca, listar os arquivos em que os termos foram encontrados.

### Projeto 2: Sistema de cadastros de monitoria
Fluxo de uso:
1. Disponibilizar uma interface (linha de comando ou GUI) com uma listagem de escolha para a funcionalidade escolhia:  cadastro de professores, disciplinas e alunos.
2. A depender da opção escolhida, receber os campos específicos de cada tipo de entidade.
3. O sistema deve manter os dados informados em arquivos.
4. Ao abrir novamente o sistema, ele deve verificar se os arquivos ('banco de dados') já existe, e caso seja encontrado, deve carregar os mesmos na memória.


### Submissão
A submissão deve ser feita através do Github Classroom através do link divulgado no google classroom.

Tente seguir a seguinte estrutura:
```
.
├── src
│   ├── main.py
│   ├── modulo1.py
│   └── <outros arquivos>
├── app.py <arquivo principal do projeto, ex.: python app.py>
├── <outros arquivos>
└── README.md
```

Ao concluir, faça o commit+push com a sua resposta, no repositório criado pelo github classroom.

### Avaliação
* 2,0 Pontos: Organização do repositório, facilidade de uso e execução do projeto
* 5,0 Pontos: Implementação das funcionalidades
* 3,0 Pontos: Vídeo de demonstração do projeto
