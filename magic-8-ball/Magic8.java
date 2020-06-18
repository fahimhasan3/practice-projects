import java.util.Random;
import java.util.Scanner;

public class Magic8 {
    public static void main(String[] args) {
        System.out.print("Hi, im the magic8 ball. ");

        String wantToContinue = "yes";
        while (wantToContinue.equals("yes")) {
            System.out.println("ask me a question");
            Scanner scanner = new Scanner(System.in);
            String question = scanner.nextLine();

            Random rand = new Random();
            int randomNumber = rand.nextInt(10);
            String message = "";
            switch (randomNumber) {
                case 0:
                    message = "As I see it, yes.";
                    break;
                case 1:
                    message = "Ask again later.";
                    break;
                case 2:
                    message = "Better not tell you now.";
                    break;
                case 3:
                    message = "Cannot predict now.";
                    break;
                case 4:
                    message = "Don’t count on it.";
                    break;
                case 5:
                    message = "Most likely.";
                    break;
                case 6:
                    message = "My sources say no.";
                    break;
                case 7:
                    message = "Yes.";
                    break;
                case 8:
                    message = "You may rely on it.";
                    break;
                case 9:
                    message = "My reply is no.";
                default:
                    message = "Yes";
                    break;
            }
            System.out.println(message);

            System.out.println("do you want to ask another question? (yes) (no)");
            wantToContinue = scanner.nextLine();
            wantToContinue = wantToContinue.toLowerCase();
        }
    }
}