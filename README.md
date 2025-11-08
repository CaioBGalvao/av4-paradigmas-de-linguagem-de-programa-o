# Paradigmas de Linguagem de Programação

## AV4

### Descrição da Prova

Escreva 2 algorítimos em 4 arquivos.

- Dois arquivos (C e Python) para Paradigma Estruturado (Procedural)
- Dois arquivos (Java e Python) para Parafigma Orientado a Objeto

Os algorítimos podem ser escolhido pelos alunos.

## Estruturada (Procedural)

- Yohan: Linguagem C
- Wallace Falque: Linguagem Python

### Algorítimo:


## Orientada a Objeto

- Java: Wallace Calisto
- Python: Caio Galvão

### Algorítimo

**Objetivo:**
Desenvolver um programa simples em console que simule o gerenciamento de personagens de um jogo, aplicando os conceitos fundamentais de Programação Orientada a Objetos (Classes, Atributos, Métodos, Encapsulamento e Instanciação).

**Enunciado do Problema:**
Você foi contratado para projetar o sistema de gerenciamento de personagens de um novo jogo de RPG. Nesta primeira fase, você deve criar a classe principal que define o que é um personagem e como ele interage com o mundo.

---

### **Requisitos do Sistema**

#### 1. A Classe `Personagem`

Você deve implementar uma classe chamada `Personagem`. Esta classe deve conter:

**A. Atributos (Privados):**
A classe deve proteger seus dados internos. Os seguintes atributos devem ser declarados como `private`:
* `nome` (tipo String): O nome do personagem.
* `pontosVida` (tipo int): A quantidade de "HP" (Health Points) do personagem.
* `pontosMana` (tipo int): A quantidade de "MP" (Mana Points) do personagem.

**B. Métodos (Públicos):**
A classe deve expor as seguintes ações e informações através de métodos `public`:

* **Construtor:**
    * Um método construtor que é chamado ao criar um novo objeto (`new Personagem(...)`).
    * Ele deve receber o `nome` do personagem como parâmetro.
    * Ele deve inicializar (definir valores padrão) `pontosVida` como **100** e `pontosMana` como **50**.

* **Métodos de Ação:**
    * `tomarDano(int dano)`: Este método recebe uma quantidade de dano. Ele deve subtrair esse valor dos `pontosVida`.
        * **Regra:** Os pontos de vida não podem ficar abaixo de 0.
    * `curar(int cura)`: Este método recebe uma quantidade de cura. Ele deve adicionar esse valor aos `pontosVida`.
        * **Regra:** Os pontos de vida não podem ultrapassar o valor máximo de 100.
    * `usarMagia(int custoMana)`: Este método recebe um custo de mana para uma magia.
        * **Regra:** Ele deve verificar se os `pontosMana` atuais são suficientes (maiores ou iguais ao `custoMana`).
        * Se houver mana suficiente, ele subtrai o custo dos `pontosMana` e retorna `true` (verdadeiro).
        * Se não houver mana suficiente, a operação falha e o método retorna `false` (falso).

* **Métodos de Consulta (Getters):**
    * `getNome()`: Retorna o `nome` do personagem.
    * `getPontosVida()`: Retorna o valor atual de `pontosVida`.
    * `getPontosMana()`: Retorna o valor atual de `pontosMana`.
    * `estaVivo()`: Retorna um valor booleano (`true` se `pontosVida > 0`, e `false` caso contrário).

---

#### 2. O Programa Principal (Simulação)

No seu arquivo/classe principal (onde fica o método `main`, por exemplo), você deve **instanciar** (criar objetos) da sua classe `Personagem` e simular um cenário de uso:

1.  Crie dois (2) objetos da classe `Personagem`:
    * Um personagem chamado "Herói".
    * Um personagem chamado "Vilão".
2.  Simule uma batalha e interações:
    * Faça o "Vilão" atacar o "Herói" (ex: `heroi.tomarDano(30)`).
    * Faça o "Herói" tentar usar uma magia muito cara (ex: `heroi.usarMagia(60)`), que deve falhar.
    * Faça o "Herói" se curar (ex: `heroi.curar(20)`).
    * Faça o "Herói" usar uma magia mais fraca (ex: `heroi.usarMagia(15)`), que deve funcionar.
    * Faça o "Herói" atacar o "Vilão" com força total (ex: `vilao.tomarDano(110)`), o que deve fazer com que os pontos de vida do vilão fiquem em 0, e não em -10.
3.  Ao final da simulação, imprima no console o status final de ambos os personagens, mostrando seus nomes, pontos de vida, pontos de mana e se estão vivos ou não.
