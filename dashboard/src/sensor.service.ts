// dashboard/src/app/sensor.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SensorService {
  private apiUrl = 'http://localhost:8002/api/sensor-data';  // Update with your actual backend API endpoint

  constructor(private http: HttpClient) {}

  getSensorData(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
}
