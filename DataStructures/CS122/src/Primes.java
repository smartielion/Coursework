import java.util.Scanner;


public class Primes {
	public static void main(String [] arrrgs){
		Scanner input = new Scanner(System.in);
		while(true){
		System.out.print("Select Rock/Paper/Scissors : ");
		String yourinput = input.next();
		yourinput = yourinput.toLowerCase();
		System.out.println("You chose " + yourinput);
		if (yourinput.equals("rock")){
			System.out.println("Computer chooses paper.");
			System.out.println("Computer Wins");
		}
		if (yourinput.equals("paper")){
			System.out.println("Computer chooses scissors.");
			System.out.println("Computer Wins");
		}
		if (yourinput.equals("scissors")){
			System.out.println("Computer chooses rock.");
			System.out.println("Computer Wins");
		} 
	}		
}}
