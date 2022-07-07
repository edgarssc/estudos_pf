import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-tic-tac-toe',
  templateUrl: './tic-tac-toe.component.html',
  styleUrls: ['./tic-tac-toe.component.css']
})
export class TicTacToeComponent {

  currentPlayer: string = 'O';
  winner: string = '';
  board: string[][] = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
  ];

  processPlay(line: number, col: number){
    //verifica se o jogo ainda não teve vencendor
    if (this.board[line][col] === '' && this.winner === '') {
    this.board[line][col] = this.currentPlayer;    
    }
    //verifica se o jogador ganhou
    if (this.checkWinner(this.currentPlayer)) {
      this.winner = this.currentPlayer;
    }
    //troca jogadores
    if (this.currentPlayer === 'O') {
      this.currentPlayer = 'X';
    }
    else {
      this.currentPlayer = 'O';
    }
  }

  checkWinner(player: string){
    //testa linhas
    for (let i = 0; i < this.board.length; i++) {
      if (this.board[i][0] === player && this.board[i][1] === player && this.board[i][2] === player) {
        return true;
      }
    }
    //testa colunas
    for (let i = 0; i < this.board.length; i++) {
      if (this.board[0][i] === player && this.board[1][i] === player && this.board[2][i] === player) {
        return true;
      }
    }
    //testa diagonais
    if (this.board[0][0] === player && this.board[1][1] === player && this.board[2][2] === player) {
      return true;
    }
    //testa diagonais
    if (this.board[0][2] === player && this.board[1][1] === player && this.board[2][0] === player) {
      return true;
    }
    return false;
  }
  //reinicia a partida
  reset(){
    this.board = [
      ['', '', ''],
      ['', '', ''],
      ['', '', '']
    ];
    this.currentPlayer = 'O';
    this.winner = '';
  }
}