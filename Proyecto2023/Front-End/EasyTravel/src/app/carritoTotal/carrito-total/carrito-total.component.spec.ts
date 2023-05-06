import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarritoTotalComponent } from './carrito-total.component';

describe('CarritoTotalComponent', () => {
  let component: CarritoTotalComponent;
  let fixture: ComponentFixture<CarritoTotalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CarritoTotalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CarritoTotalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
