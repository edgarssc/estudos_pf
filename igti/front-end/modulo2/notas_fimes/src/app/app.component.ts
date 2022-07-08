import { Component } from '@angular/core';
//import {Movie} from './movie';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'notas_fimes';
  movies = [
    {title: 'The Shawshank Redemption', rating: 5},
    {title: 'The Godfather', rating: 3},
    {title: 'The Godfather: Part II', rating: 2},
    {title: 'The Dark Knight', rating: 4},
    {title: '12 Angry', rating: 3}
  ];
}
