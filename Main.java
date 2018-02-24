package game;
import java.util.Scanner;
public class Main {
	private static  int moveR;
	private static int moveC;
	private static MainGame game;
	private static final int row;
	private static final int col;		

	game = new MainGame();		

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		do {
			System.out.println("Current layout:");
			game.printBoard();
			System.out.println("Enter row");
			moveR  =  scan.nextInt();
			System.out.println("Enter column");
			moveC = scan.nextInt();
			game.placeMark(moveR, moveC);
		
			do {
				System.out.println("Player"+ game.getCurrentPlayer()
				+ "eneter an empty row and column");
				
			} while(game.board[row][col] < 3);
		
		
		}
		 while (game.isWinner() != true);
		scan.close();
	}

	

	//constructor
	public Main() {

		static Scanner scan = new Scanner(System.in);
		row = 3;
		col = 3;
	}

	}