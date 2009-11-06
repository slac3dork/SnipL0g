/**
  _________      .__       .____   _______
 /   _____/ ____ |__|_____ |    |  \   _  \    ____
 \_____  \ /    \|  \____ \|    |  /  /_\  \  / ___\
 /        \   |  \  |  |_> >    |__\  \_/   \/ /_/  >
/_______  /___|  /__|   __/|_______ \_____  /\___  /
        \/     \/   |__|           \/     \//_____/
http://snippet.c0de.me
slac3dork@gmail.com
*/

/*
 * Array.java
 *
 * Created on September 23, 2007, 23.45 PM
 * Purpose: a simple java program to process array
 *
 */

/**
 * @version 1.0
 * @author slac3dork
 */

public class Array {

	private int panjang;
	private int elements[];

	public Array() {
		panjang = 25;
	}

	public void setCreate() {
		elements = new int[panjang];
		for(int i=0; i<panjang ; i++) {
			elements[i] = 0;
		}
	}

	public void setAdd(int bil) {
		for (int i=0; i<panjang; i++) {
			if (elements[panjang-1]!=0){
				System.out.println("Array is full");
				break;
			} else {
				if (elements[i]==0) {
					elements[i] = bil;
					break;
				}
			}
		}
	}

	public void setDelete() {
		for (int i=panjang-1; i>=0 ; i--) {
			if (elements[0]==0) {
				System.out.println("Array is empty, could not delete element");
				break;
			} else {
				if (elements[i]==0) {
					elements[i] = 0;
					break;
				}
			}
		}
	}

	public void Display() {
		for (int i=0; i<panjang; i++) {
			System.out.println(elements[i]);
		}
	}

	public void setSort() {
		int temp;
		int isi = 0;

		for (int i=0; i<(panjang-2); i++) {
			if (elements[i]!=0)
				isi = isi + 1;
			else
				break;
		}

		for (int i=0; i<(isi-2); i++) {
			for (int j=isi-1; j>=(i+1); j--) {
				if ((elements[j] < elements[j-1]) && (elements[j]!=0 || elements[j-1]!=0)) {
					temp = elements[j];
					elements[j] = elements[j-1];
					elements[j-1] = temp;
				}
			}
		}
	}

	public void getSearch(int bil) {
		boolean cek = false;
		for (int i=0; i<panjang-1; i++) {
			if (elements[i]==bil) {
				System.out.println("Value " + bil +" has index number" + i);
				cek = true;
				break;
			}
		}

		if (!cek)
			System.out.println("Not Found");
	}

	public int getMax() {
		int max = -999; 

		for (int i=0; i<panjang ; i++) {
			if (elements[i]>max) {
				max = elements[i];
			}
		}
		return max;
	}

	public int getMin() {
		int min = 999; 

		for (int i=0; i<panjang ; i++) {
			if ((elements[i]<min) && (elements[i]!=0)) {
				min = elements[i];
			}
		}
		return min;
	}

	public static void main(String args[]) {
		Array objek = new Array();

		System.out.println("Creating Object");
		objek.setCreate();
		System.out.println("Add element");
		objek.setAdd(5);
		objek.setAdd(2);
		objek.setAdd(3);
		objek.setAdd(7);
		objek.setAdd(10);
		System.out.println("Deleting...");
		objek.setDelete();
		System.out.println("Show array");
		objek.Display();
		System.out.println("sorting...\n");
		objek.setSort();
		System.out.println("Show sorted array");
		objek.Display();
		System.out.println("Search...");
		objek.getSearch(3);
		objek.getSearch(15);
		System.out.println("Maximum array value = " + objek.getMax());
		System.out.println("Minimum array value = " + objek.getMin());
	}
}

