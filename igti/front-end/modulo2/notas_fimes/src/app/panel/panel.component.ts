import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'panel',
  templateUrl: './panel.component.html',
  styleUrls: ['./panel.component.css']
})
export class PanelComponent implements OnInit {

  expandend = true;
  @Input() title: string='';
  constructor() { }

  ngOnInit(): void {
  }

  expand() {
    this.expandend = true;
  }

  contract() {
    this.expandend = false;
  }
}
