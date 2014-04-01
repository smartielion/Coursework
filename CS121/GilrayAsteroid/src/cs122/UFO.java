package cs122;


public class UFO {
	/* Store the x & y position */
	private double x, y;

	/* Store the x & y velocities */
	private double vx, vy;
	
	/* Create a new UFO at a given location with a
	 * specified velocity
	 */
	public UFO(int x, int y, double vx, double vy) {
		this.x = x;
		this.y = y;
		this.vx = vx;
		this.vy = vy;
	}

	/**
	 * @return the ufo's x position
	 */
	public double getX() { return x; }

	/**
	 * @return the ufo's y position
	 */
	public double getY() { return y; }
	
	/**
	 * Set the ufo's x and y velocities
	 */
	public void setVelocity( double vx, double vy) {
		double magnitude = Math.sqrt(vx*vx + vy*vy);
		if (magnitude > 141.0) {
			// velocity must be less than e.g., (100,100)
			// if we get here, then we need to scale it...
			System.err.println("You specified a velocity that is too fast for this ufo...");
			
			vx = 141.0*vx/magnitude;
			vy = 141.0*vy/magnitude;
		}
		this.vx = vx;
		this.vy = vy;
	}
	
	/**
	 * @return the ufo's x velocity
	 */
	public double getXVelocity() { return vx; }
	
	/**
	 * @return the ufo's y velocity
	 */
	public double getYVelocity() { return vy; }
	
	/**
	 * Change the ufo's position based on the 
	 * elapsed time (delta)
	 */
	public void update(double delta) { x += delta*vx; y += delta*vy; }
}
