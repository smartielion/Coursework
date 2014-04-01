package linkedlist;

import jig.misc.linkedlist.LinkedListNode;
import jig.misc.linkedlist.SinglyLinkedList;

/**
 * This is your implementation of the SinglyLinkedList interface. If you implement it correctly,
 * you should be able to play the linked list game.
 * 
 * @author You
 */
public class StudentLinkedList implements SinglyLinkedList {
	
	private LinkedListNode sentinal;
	

	public StudentLinkedList(){
		sentinal = new LinkedListNode(null);
	}

	public LinkedListNode findPredecessor(LinkedListNode from, Object search) {
		// Returns the node preceeding the node with the specified data
		LinkedListNode x = from;
		while (x.getNext() != null){
			if (search.equals((x.getNext()).getData())){
				return x;
			}
			x = x.getNext();
		}
		return null;
	}
	
	

	public LinkedListNode getHead() {
		// returns the sentinal node
		return sentinal;
	}

	public LinkedListNode getLast() {
		//Returns the last node in the list
		LinkedListNode x = sentinal;
		while(x.getNext() != null ){
			x=x.getNext();
		}
		return x;
	}

	public void insertAfter(LinkedListNode predecessor,
			LinkedListNode nodeOrHeadToInsert) {
		// Splices nodeorheadtoinstert after predecessor
		LinkedListNode x = nodeOrHeadToInsert;
		while (x.getNext() != null){
			x=x.getNext();
		}
		x.setNext(predecessor.getNext());
		predecessor.setNext(nodeOrHeadToInsert);
		
	}

	public LinkedListNode removeNext(LinkedListNode node) {
		// Removes the node immidiatly following the given node
		LinkedListNode y = null;

		y = node.getNext();
		node.setNext(y.getNext());
		y.setNext(null); 
		return y;
		}

	public LinkedListNode removeRemaining(LinkedListNode node) {
		// Removes all follwing the removed node
		LinkedListNode y = null;
		y = node.getNext();
		node.setNext(null);
		return y;
		}
}

