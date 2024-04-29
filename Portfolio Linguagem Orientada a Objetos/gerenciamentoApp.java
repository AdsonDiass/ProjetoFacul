import java.util.Scanner;

public class gerenciamentoApp {
    public static void main(String [] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bem-vindo ao sistema de gerenciamento bancário!");

        // Pedir dados do usuário
        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();

        System.out.print("Digite seu sobrenome: ");
        String sobrenome = scanner.nextLine();

        System.out.print("Digite seu CPF: ");
        String cpf = scanner.nextLine();

        // Criar a conta bancária
        gerenciamentoBanco conta = new gerenciamentoBanco (nome, sobrenome, cpf);

        // Menu de operações
        int escolha;
        do {
            System.out.println("\nEscolha uma operação:");
            System.out.println("1 - Consultar saldo");
            System.out.println("2 - Realizar depósito");
            System.out.println("3 - Realizar saque");
            System.out.println("4 - Encerrar");

            escolha = scanner.nextInt();

            switch (escolha) {
                case 1:
                    // Consultar saldo
                    System.out.println("Saldo atual: R$" + conta.consultarSaldo());
                    break;
                case 2:
                    // Realizar depósito
                    System.out.print("Digite o valor do depósito: ");
                    double valorDeposito = scanner.nextDouble();
                    conta.depositar(valorDeposito);
                    break;
                case 3:
                    // Realizar saque
                    System.out.print("Digite o valor do saque: ");
                    double valorSaque = scanner.nextDouble();
                    conta.sacar(valorSaque);
                    break;
                case 4:
                    // Encerrar
                    System.out.println("Encerrando o sistema de gerenciamento bancário. Obrigado!");
                    break;
                default:
                    System.out.println("Opção inválida. Escolha novamente.");
            }
        } while (escolha != 4);

        scanner.close();
    }
}