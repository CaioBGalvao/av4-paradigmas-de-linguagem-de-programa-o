/** Classe que define a estrutura de um Personagem, aplicando Encapsulamento. */
public class Personagem {

    // A. Atributos Privados (Encapsulamento)
    private String nome;
    private int pontosVida;
    private int pontosMana;
    private static final int VIDA_MAXIMA = 100; 

    // B. Métodos Públicos (Comportamentos)

    // Construtor
    public Personagem(String nome) {

        this.nome = nome;
        this.pontosVida = VIDA_MAXIMA;
        this.pontosMana = 50;
        
        System.out.println("Personagem " + nome + " foi criado!"); 
    }

    // Métodos de Ação

    /** Subtrai dano dos pontos de vida. Os PVs não podem ser menores que 0.*/
    public void tomarDano(int dano) {
        if (dano > 0) {
            this.pontosVida -= dano;
            // Regra: Pontos de vida não podem ficar abaixo de 0
            if (this.pontosVida < 0) {
                this.pontosVida = 0;
            }
            System.out.println(this.nome + " tomou " + dano + " de dano. PVs atuais: " + this.pontosVida);
        }
    }


    /** Adiciona cura aos pontos de vida. Os PVs não podem ultrapassar 100. */
    public void curar(int cura) {
        if (cura > 0) {
            this.pontosVida += cura;
            // Regra: Pontos de vida não podem ultrapassar o valor máximo
            if (this.pontosVida > VIDA_MAXIMA) {
                this.pontosVida = VIDA_MAXIMA;
            }
            System.out.println(this.nome + " se curou em " + cura + " pontos. PVs atuais: " + this.pontosVida);
        }
        
    }


    /** Tenta usar uma magia, consumindo mana se houver o suficiente. */
    public boolean usarMagia(int custoMana) {
        if (custoMana <= 0) {
             System.out.println(this.nome + " tentou usar magia com custo 0 ou negativo. Operação cancelada.");
             return false;
        }
        
        // Regra: Verifica se há mana suficiente
        if (this.pontosMana >= custoMana) {
            this.pontosMana -= custoMana;
            System.out.println(this.nome + " usou magia com sucesso! Custo: " + custoMana + ". Mana restante: " + this.pontosMana);
            return true;
        } else {
            System.out.println(this.nome + " falhou ao usar magia. Mana insuficiente.");
            return false;
        }
    }


    // Métodos de Consulta (Getters)

    public String getNome() {
        return nome;
    }

    public int getPontosVida() {
        return pontosVida;
    }

    public int getPontosMana() {
        return pontosMana;
    }

    /** Retorna se o personagem está vivo (pontosVida > 0). */
    public boolean estaVivo() {
        return pontosVida > 0;
    }
}