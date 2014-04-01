package cs122;

import java.awt.Graphics;
import javax.swing.JFrame;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;
import java.awt.image.BufferedImage;
import java.io.BufferedInputStream;
import java.io.IOException;
import java.net.URL;

import javax.imageio.ImageIO;


/**
 * A graphical user interface element based on a framed window.
 * 
 * The GameFrame provides the foundation for creating
 * simple animations or games.
 * 
 * Once the GameFrame is constructed, the run() method should
 * be called. This will begin a loop in which the render() and 
 * update() methods are sequentally called until the animation
 * is exited.
 * 
 * @author wallaces
 *
 */
@SuppressWarnings("serial")
public class GameFrame extends JFrame {
	private long lastUpdateTime;
	private double deltaSeconds;

	/**
	 * Create a new GameFrame.
	 * @param w the width of the frame
	 * @param h the height of the frame
	 */
	public GameFrame(int w, int h) {
		super();
		setUndecorated(true);
		setSize(w, h);
		lastUpdateTime = 0;
		deltaSeconds = 0;
	}

	/**
	 * Update the animation. The provided code simply records
	 * how much time has elapsed since the last update. This
	 * value can be retrieved using getDeltaTime() and can be
	 * used to determine how far an object should move or to
	 * display the frame rate.
	 * 
	 * Subclasses of GameFrame will probably want to override 
	 * this method with their own behavior.
	 */
	public void update() {
		// get the current time
		long time = System.nanoTime();

		// calculate how much time has passed,
		// convert from nano seconds into seconds
		if (lastUpdateTime > 0)
			deltaSeconds = (time - lastUpdateTime) / 1000000000.0;

		// update the lastRenderTime
		lastUpdateTime = time;

	}

	/**
	 * Render the animation.
	 * 
	 * Subclasses of GameFrame will probably want to override this 
	 * method with their own behavior.
	 *  
	 * @param g the graphics context (you can and should treat this as a black box)
	 */
	public void render(Graphics g) {
		if (deltaSeconds > 0) {
			// calculate the frames per second (as an integer)
			int fps = (int) (1.0 / deltaSeconds);
			// draw the fps in the lower left corner
			g.drawString(Integer.toString(fps), 10, getHeight() - 20);
		}
	}

	/**
	 * 
	 * @return the number of seconds since the last update
	 */
	public double getDeltaTime() {
		return deltaSeconds;
	}

	/**
	 * You should NOT call this method, and
	 * you should NOT override this method.
	 */
	public void paint(Graphics g) {
		super.paint(g);
		update();
		render(g);
	}

	/**
	 * Run the animation
	 */
	public void run() {
		if (!isVisible()) setVisible(true);
		
		while (true) {
			repaint();

			try {
				Thread.sleep(10);
			} catch (InterruptedException ie) {
			}
		}
	}

	/**
	 * Loads an image (typically from disk).  Getting the image
	 * url can be a tricky business in Java, so I will typically 
	 * set this up for you...
	 *  
	 * @param url the location of the image to load
	 * @return a BufferedImage that can and SHOULD be treated as a black box
	 */
	public static BufferedImage loadImage(String url) {
		try {
			URL u = ClassLoader.getSystemResource(url);
			BufferedImage bi = ImageIO.read(new BufferedInputStream(u.openStream()));
			return bi;
		} catch (IOException e) {
			System.err.println("Error: " + e);
			System.exit(1);
			return null;
		}
	}

	public static void drawImageAt(Graphics2D g, BufferedImage i, double x,
			double y, double theta) {
		AffineTransform at = AffineTransform.getTranslateInstance(x, y);
		at.rotate(theta);
		at.translate(-i.getWidth() / 2.0, -i.getHeight() / 2.0);
		g.drawImage(i, at, null);
	}
}
