package bad;

class BadJava {
    public static void main(String[] args) {
        var a1 = 0.2;
        var a2 = 0.1;
        var expected = 0.3;

        var actual = a1 + a2;
        if (expected != actual) {
            System.out.println("Java sucks");
            System.out.println(String.format("Expected %f, got [%.20f]", expected, actual));
        } else {
            System.out.println("Java is awesome");
        }
    }
}