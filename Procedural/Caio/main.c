#include <stdio.h>
#include <ctype.h>
#include "banco.h"

int main(){
    char novaTransacao = 'S';
    int id;
    char nomeDoTitular[255];
    struct conta_banco conta;

    printf("Seja bem vindo ao Banco Boente.\n");
    
    printf("Digite o nome do novo titular: ");
    scanf("%[^\n]", nomeDoTitular);
    
    printf("Digite o ID da conta: ");
    scanf("%d", &id);

    conta = criar_conta(id, nomeDoTitular);

    printf("Conta para %s aberta com sucesso.\n", nomeDoTitular);
    printf("Saldo atual e 0\n");

    while(novaTransacao == 'S'){
        
        int valorDaTransacao;

        printf("\n--- Nova Transacao ---\n");
        printf("Saldo atual: %.2f \n", conta.saldo);

        printf("Qual o valor da transacao? [ex.: -50, 35]: ");
        scanf("%d", &valorDaTransacao);

        int resultado = processar_transacao(&conta, valorDaTransacao);
        
        if(resultado == 0){
            printf("Erro: Usuario nao tem saldo suficiente para o saque.\n");
        } else {
            printf("Sucesso: Transacao realizada.\n");
        }

        printf("Voce deseja iniciar uma nova transacao? [S/N]: ");
        scanf(" %c", &novaTransacao);
        novaTransacao = toupper(novaTransacao);
    };

    printf("\nRelatorio da Conta: \n");
    printf("Correntista: %s \n", conta.nomeDoTitular);
    printf("Saldo Final: %.2f \n", conta.saldo);
    printf("Identificador interno: %d \n", conta.id); // %d para int
    
    return 0;
}