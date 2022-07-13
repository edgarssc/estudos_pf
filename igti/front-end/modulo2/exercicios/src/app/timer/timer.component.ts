import { Component, Input} from '@angular/core';
import { Exercise } from '../exercise';

@Component({
  selector: 'app-timer',
  templateUrl: './timer.component.html',
  styleUrls: ['./timer.component.css']
})
export class TimerComponent {

  @Input() exercises: Exercise[] = [];
  currentEx: number = 0;
  currentRep: number =0;
  phase: number = 0;
  constructor() { }

  formatPhase(phase: number){
    switch (phase){
      case 0: return 'Preparação';
      case 1: return 'Exercício';
      case 2: return 'Descanso';
    }
  }
}
