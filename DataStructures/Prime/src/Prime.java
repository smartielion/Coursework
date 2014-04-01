
public class Prime {
	/* try dividing p by all numbers between 1 and P
	 */
	public static boolean isPrime(int p){
		if (p < 2) return false;
		if (p==2) return true;
		for (int i = 2; i < p ;i++ ){
			if (p%i == 0){
				return false;
			}
		}
		return true;
	}

	public static void primesBelow(int p){
		int primeCount = 0;
		for(int i = 2;i<=p;i++){
			if (Prime.isPrime(i)){
				primeCount += 1;
				System.out.println(i + " is Prime!");
			}
		}
		System.out.printLn("");
	}
	public static void main(String [] args){
	System.out.println("All of the primes until 100 are:");
	Prime.primesBelow(100);
	}
}