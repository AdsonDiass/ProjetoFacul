public class gerenciamentoBanco {
    private String nome;
    private String sobrenome;
    private String cpf;
    private double saldo;

    // Construtor
    public gerenciamentoBanco(String nome, String sobrenome, String cpf) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.cpf = cpf;
        this.saldo = 0.0; // Saldo inicial zero
    }

    // Método para consultar saldo
    public double consultarSaldo() {
        return saldo;
    }

    // Método para realizar um depósito
    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
            System.out.println("Depósito de R$" + valor + " realizado com sucesso.");
        } else {
            System.out.println("Valor inválido para depósito.");
        }
    }

    // Método para realizar um saque
    public void sacar(double valor) {
        if (valor > 0 && saldo >= valor) {
            saldo -= valor;
            System.out.println("Saque de R$" + valor + " realizado com sucesso.");
        } else {
            System.out.println("Saldo insuficiente ou valor inválido para saque.");
        }
    }
}