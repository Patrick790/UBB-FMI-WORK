package org.example.domain;

public class Complex {

    private final int real;
    private final int imag;

    public Complex(int real, int imag) {
        this.real = real;
        this.imag = imag;
    }

    public static Complex parseComplex(String complexStr) {
        // Divizez șirul în parte reală și parte imaginară folosind semnul "+" sau "-" ca separator
        String[] parts = complexStr.split("[+]");

        if (parts.length != 2) {
            parts = complexStr.split("-");
        }

        int realPart = Integer.parseInt(parts[0]);

        // Verifică dacă șirul conține "+" sau "-" pentru a determina partea imaginară
        if (complexStr.contains("+")) {
            int imagPart = Integer.parseInt(parts[1].replace("i", ""));
            return new Complex(realPart, imagPart);
        } else if (complexStr.contains("-")) {
            int imagPart = -Integer.parseInt(parts[1].replace("i", ""));
            return new Complex(realPart, imagPart);
        } else {
            return new Complex(realPart, 0);
        }
    }


    public static Complex add(Complex a, Complex b) {
        int realResult = a.real + b.real;
        int imagResult = a.imag + b.imag;
        return new Complex(realResult, imagResult);
    }

    public static Complex subtract(Complex a, Complex b) {
        int realResult = a.real - b.real;
        int imagResult = a.imag - b.imag;
        return new Complex(realResult, imagResult);
    }

    public static Complex multiply(Complex a, Complex b) {
        int realResult = a.real * b.real - a.imag * b.imag;
        int imagResult = a.real * b.imag + a.imag * b.real;
        return new Complex(realResult, imagResult);
    }

    public static Complex divide(Complex a, Complex b) {
        int denominator = b.real * b.real + b.imag * b.imag;
        int realResult = (a.real * b.real + a.imag * b.imag) / denominator;
        int imagResult = (a.imag * b.real - a.real * b.imag) / denominator;
        return new Complex(realResult, imagResult);
    }

    @Override
    public String toString() {
        if (imag >= 0) {
            return real + "+" + imag + "i";
        } else {
            return real + "" + imag + "i";
        }

    }

    public static final Complex ZERO = new Complex(0, 0);
}

