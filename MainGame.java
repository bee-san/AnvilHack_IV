package game;

public class MainGame {
	public char[] [] board;
	private char currentPlayer;
	
	public MainGame() {
		currentPlayer = 'x';
	
		
		}
	
	public char getCurrentPlayer() {
		return currentPlayer;
	}
	
	public void initialiseBoard() 
	{
		for (int i=0;i<3;i++) {
			for(int j = 0; j<3; j++) {
				board[i][j] = '-';
				
				
			}
			
		}
		
	}
	public boolean checkRows(){
		for(int i=0; i<3; i++	) {
			if(checkRowCol(board[i][0], board[i][1], board[i][2])== true)
			{
				return true;
			}
		}
		return false;
		}	
		private boolean checkColumns() {
			for (int i=0; i<3; i++) {
				if(checkRowCol(board[0][i], board[1][i], 	
					board[2][i]) == true){
						return true;
					}	
			}
			return false;
			
			
		}		
			
	 private boolean checkDiagonals(){
		 return((checkRowCol(board[0][0], board[1][1], board[2][2])==true
		|| (checkRowCol(board[0][2], board[1][1], board[2][0]) == true)));
		 
	 }
		
		
	public void printBoard() {
		System.out.println("---------");
		for(int i=0; i<3; i++) {
			System.out.println("|");{
				for(int j=0; j<3; j++) {
					System.out.print(board[i][j] + "|");
					
				}
				
			}
		}
		
			System.out.println();;
			System.out.println("------");
		}
		
		
		
	
	public boolean placeMark(int row, int col) {
	if ((row >=0)&&(col<3)){
		if(board[row][col]=='-');{	
			board[row][col]= currentPlayer;
			return true;
		}
	
	}
	return false;
}
	private boolean checkRowCol(char c1, char c2, char c3) {
		return((c1 != '-')&&(c1==c2)&&(c2==3));
		
	}
	public void changePlayer() {
		if(currentPlayer=='x') {
			currentPlayer= 'o';
		}
		else {
			currentPlayer = 'x';
		}
		
	}
	public boolean isWinner() {
		return(checkRows() || checkColumns() || checkDiagonals());
		
		
	}

	
}
