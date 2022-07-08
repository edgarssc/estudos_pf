import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-rating',
  templateUrl: './rating.component.html',
  styleUrls: ['./rating.component.css']
})
export class RatingComponent  {

  @Input() rating: number = 0;
  @Output() ratingChange = new EventEmitter<number>();

  onClick(i: number) {
    this.ratingChange.emit(i);
  }

}
