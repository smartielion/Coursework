package cs122;



/**
 * A class representing an asteroid.
 *
 * The class stores member variables representing the 
 * properties we might expect an asteroid to have.
 *
 * @author wallaces
 *
 */
public class Asteroid {
	/* Store the x & y position */
	private double x, y;

	/* Store the x & y velocities */
	private double vx, vy;
	
	/* Create a new Asteroid at a given location with a
	 * specified velocity
	 */
	public Asteroid(int x, int y, double vx, double vy) {
		this.x = x;
		this.y = y;
		this.vx = vx;
		this.vy = vy;
	}

	/**
	 * @return the asteroid's x position
	 */
	public double getX() { return x; }

	/**
	 * @return the asteroid's y position
	 */
	public double getY() { return y; }
	
	/**
	 * Set the asteroid's x and y velocities
	 */
	public void setVelocity( double vx, double vy) {
		this.vx = vx;
		this.vy = vy;
	}
	
	/**
	 * @return the asteroid's x-velocity
	 */
	public double getVX() {
		return vx;
	}

	/**
	 * @return the asteroid's y-velocity
	 */
	public double getVY() {
		return vy;
	}

	/**
	 * Change the asteroid's position based on the 
	 * elapsed time (delta)
	 */
	public void update(double delta) {
		
		x += delta*vx; 
		y += delta*vy; 
		
		// warp the image if necessary.
		// here, we assume the image is ~ 90x110
		// and that the screen is ~ 800x600
		if (x < -45) x = 845;
		else if (x > 845) x = -45;
		if (y < -55) y = 655;
		else if (y > 655) y = -55;	
	}
}
