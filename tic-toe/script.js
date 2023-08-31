document.addEventListener("DOMContentLoaded", () => {
    const cells = document.querySelectorAll('[data-cell]');
    const status = document.getElementById('status');
    const restartButton = document.getElementById('restartButton');
  
    let currentPlayer = 'X';
    let gameActive = true;
    let gameState = ['', '', '', '', '', '', '', '', ''];
  
    const winningCombinations = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ];
  
    function handleCellClick(e) {
      const cell = e.target;
      const cellIndex = parseInt(cell.getAttribute('data-cell'));
  
      if (gameState[cellIndex] !== '' || !gameActive) {
        return;
      }
  
      gameState[cellIndex] = currentPlayer;
      cell.textContent = currentPlayer;
      checkWin();
      checkDraw();
      swapPlayer();
    }
  
    function checkWin() {
      for (const combination of winningCombinations) {
        const [a, b, c] = combination;
        if (
          gameState[a] === gameState[b] &&
          gameState[b] === gameState[c] &&
          gameState[a] !== ''
        ) {
          status.textContent = `Player ${currentPlayer} wins!`;
          gameActive = false;
          return;
        }
      }
    }
  
    function checkDraw() {
      if (gameState.every(cell => cell !== '')) {
        status.textContent = "It's a draw!";
        gameActive = false;
      }
    }
  
    function swapPlayer() {
      currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
      status.textContent = `Player ${currentPlayer}'s turn`;
    }
  
    function restartGame() {
      currentPlayer = 'X';
      gameActive = true;
      gameState = ['', '', '', '', '', '', '', '', ''];
      status.textContent = `Player ${currentPlayer}'s turn`;
      cells.forEach(cell => {
        cell.textContent = '';
      });
    }
  
    cells.forEach(cell => {
      cell.addEventListener('click', handleCellClick);
    });
  
    restartButton.addEventListener('click', restartGame);
  });
  