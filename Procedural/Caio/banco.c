#include "banco.h"
#include <string.h>

struct conta_banco criar_conta(int id, char nomeDoTitular[]){
    struct conta_banco conta;
    conta.id = id;
    conta.saldo = 0;
    strcpy(conta.nomeDoTitular, nomeDoTitular);

    return conta;
}

int processar_transacao(struct conta_banco *conta, double valorDaTransacao){
    if (valorDaTransacao > 0){
        conta->saldo += valorDaTransacao;
    } else if(conta->saldo < valorDaTransacao*-1) {
        return 0;
    } else {
        conta->saldo += valorDaTransacao;
    };

    return 1;
}