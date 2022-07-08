import { Component, OnInit } from '@angular/core';
import { TodoItem } from './todoitem';
@Component({
  selector: 'app-todolist',
  templateUrl: './todolist.component.html',
  styleUrls: ['./todolist.component.css']
})
export class TodolistComponent {
  
  newTask: string = '';

  tasks: TodoItem[] = [
    {description: 'Arrumar a cama', done: true},
    {description: 'Lavar o carro', done: false},
    {description: 'Pagar a conta', done: false}
  ];
 
  addTask() {
    this.tasks.push({
      description: this.newTask,
      done: false
    });
  }

  deleteTask(i: number) {
    this.tasks.splice(i, 1);
  }
}
