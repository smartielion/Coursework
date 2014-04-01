package cs122;


import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;


/**
 * A Skeleton class for creating a simple animation
 * 
 * @author wallaces
 *
 */
public class GilrayAsteroid extends GameFrame {

	// At this point, you don't know what a 'BufferedImage' is
	// you could google it, but it will probably make things 
	// more confusing rather than less.  Suffice it to say that
	// a BufferedImage is a Java data type for representing a
	// graphic image and will is pass it to a method that will 
	// draw it on the screen... 
	// otherwise you can (AND SHOULD) treat this as a black box.  
	// That's a big benefit of the OOP paradigm!
	private BufferedImage asteroidImage;
	private BufferedImage ufoImage;
	private UFO ufo;
	private double timePassed;
	private Object [] asteroidArray;
	
	/**
	 * Create a new AsteroidSkeleton class for creating the animation
	 * 
	 * This base implementation loads the images for the asteroid and ufo
	 * and creates a new ufo
	 * 
	 * @param maxAsteroids the maximum number of asteroids to be displayed
	 */
	public GilrayAsteroid(int maxAsteroids) {	
		super(800, 600);
		asteroidImage = loadImage("cs122/small-asteroid.png");
		ufoImage = loadImage("cs122/small-ufo.png");
		
		// make a stationary ufo...
		ufo = new UFO(400,300,0,0);
		for (int i = 0;(i <=maxAsteroids);i++){
			int xPos = (int) ((Math.random()*400)+200);
			int yPos = (int) ((Math.random()*300)+150);
			double xSpeed = ((Math.random()*60)-30);
			double ySpeed = ((Math.random()*60)-30);
			
			asteroidArray[i] = new UFO(xPos,yPos,xSpeed,ySpeed);
		}
	}
	
	/**
	 * This method overrides update() in the GameFrame class
	 */
	public void update() {
		super.update(); // do whatever the base class (GameFrame) would have done...
	
		timePassed += getDeltaTime();
		
		if (timePassed > 5.0 && ufo.getXVelocity() == 0.0 && ufo.getYVelocity() == 0.0) {
			// start moving slowly...
			System.out.println("5 seconds is up!");
			ufo.setVelocity(20, 20);
		}
		
		// call the update method on each asteroid
		// and the ufo here... 
		ufo.update(getDeltaTime());
		
		// any other code to 
		// change the ufo behavior over time, should
		// probably go here...
	}

	/**
	 * This method overrides render() in the GameFrame class
	 */
	public void render(Graphics g) {
		super.render(g);
		
		// draw each image for example:
		drawImageAt((Graphics2D) g, ufoImage, ufo.getX(), ufo.getY(), 0.0); 
	}

	/**
	 * The entry method used when the class is run as an application
	 * 
	 * Here, we create a new AsteroidSkeleton and call it's run method...
	 * 
	 * @param args (not used)
	 */
	public static void main(String [] args) {
		GilrayAsteroid ask = new GilrayAsteroid(1);
		ask.run();
	}
}
