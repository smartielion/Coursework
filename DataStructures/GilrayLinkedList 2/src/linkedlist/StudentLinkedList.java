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
		if (sentinal.getNext() == null){return sentinal;}
		else{
		LinkedListNode x = sentinal.getNext();
		while (x.getNext() != null){
			x.setNext(x.getNext());
		}
		
		return x;
		}
	}

	public void insertAfter(LinkedListNode predecessor,
			LinkedListNode nodeOrHeadToInsert) {
		// Splices nodeorheadtoinstert after predecessor
		LinkedListNode x = sentinal;
		while (x.getNext() != null){
			if (x.equals(predecessor)){
				break;
			}
			x = x.getNext();
		}
		nodeOrHeadToInsert.setNext(x.getNext());
		x.setNext(nodeOrHeadToInsert);
	}

	public LinkedListNode removeNext(LinkedListNode node) {
		// Removes the node immidiatly following the given node
		if (sentinal.getNext() == null){return sentinal;}
		else{
		LinkedListNode x = sentinal.getNext();
		LinkedListNode y = null;
		while (x.getNext() != null){
			if (x.equals(node)){
				y = x.getNext();
				x.setNext(y.getNext());
				break;
			}
			x=x.getNext();
		}
		return y;
		}
	}

	public LinkedListNode removeRemaining(LinkedListNode node) {
		// Removes all follwing the removed node
		if (sentinal.getNext() == null){return sentinal;}
		else{
		LinkedListNode x = sentinal.getNext();
		LinkedListNode y = null;
		while (x.getNext() != null){
			if (x.equals(node)){
				break;
			}
			x=x.getNext();
		}
		y = x.getNext();
		x.setNext(null);
		return y;
	}
	}
}

