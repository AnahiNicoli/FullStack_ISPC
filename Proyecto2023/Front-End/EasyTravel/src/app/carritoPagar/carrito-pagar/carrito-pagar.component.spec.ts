import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarritoPagarComponent } from './carrito-pagar.component';

describe('CarritoPagarComponent', () => {
  let component: CarritoPagarComponent;
  let fixture: ComponentFixture<CarritoPagarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CarritoPagarComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CarritoPagarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
