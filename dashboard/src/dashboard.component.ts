// dashboard/src/app/dashboard.component.ts

import { Component, OnInit } from '@angular/core';
import { SensorService } from './sensor.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css'],
})
export class DashboardComponent implements OnInit {
  sensorData: any;

  constructor(private sensorService: SensorService) {}

  ngOnInit(): void {
    // For demonstration purposes, you can hardcode sample data or fetch real data here
    this.sensorData = {
      temperature: 25,
      motion: 15,
      humidity: 50,
    };
  }
}

