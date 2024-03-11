package org.example;

import org.example.domain.Complex;

public class Main {
    public static void main(String[] args) {
        if (args.length % 2 == 0) {
            System.out.println("Expresia nu este validă. Număr incorect de operatori.");
            return;
        }

        Complex result = Complex.parseComplex(args[0]);
        String operator = null;

        String lastOperator = null;

        for (int i = 1; i < args.length; i += 2) {
            if (!args[i].matches("[+\\-*/]")) {
                System.out.println("Operatorul '" + args[i] + "' nu este valid.");
                return;
            }
            if (lastOperator == null) {
                lastOperator = args[i];
            } else if (!lastOperator.equals(args[i])) {
                System.out.println("Operatorii între numerele complexe nu sunt consecutivi.");
                return;
            }

            operator = args[i];
            Complex operand = Complex.parseComplex(args[i + 1]);

            switch (operator) {
                case "+":
                    result = Complex.add(result, operand);
                    break;
                case "-":
                    result = Complex.subtract(result, operand);
                    break;
                case "*":
                    result = Complex.multiply(result, operand);
                    break;
                case "/":
                    if (operand.equals(Complex.ZERO)) {
                        System.out.println("Împărțirea la zero nu este permisă.");
                        return;
                    }
                    result = Complex.divide(result, operand);
                    break;
                default:
                    System.out.println("Operatorul '" + operator + "' nu este valid.");
                    return;
            }
        }

        System.out.println("Rezultatul expresiei: " + result);
    }
}


