#ifndef BANCO_H
#define BANCO_H

struct conta_banco {
    int id;
    char nomeDoTitular[255]; 
    double saldo;
};

struct conta_banco criar_conta(int id, char nomeDoTitular[]);

int processar_transacao(struct conta_banco *conta , double valorDaTransacao);

#endif
