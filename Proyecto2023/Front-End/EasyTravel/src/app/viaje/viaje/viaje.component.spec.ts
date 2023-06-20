import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViajeComponent } from './viaje.component';

describe('ViajeComponent', () => {
  let component: ViajeComponent;
  let fixture: ComponentFixture<ViajeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViajeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ViajeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
