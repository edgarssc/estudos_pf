import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'testes';
  exibir: boolean = true;
  toggleShow() {
    this.exibir = !this.exibir;
  }
}
