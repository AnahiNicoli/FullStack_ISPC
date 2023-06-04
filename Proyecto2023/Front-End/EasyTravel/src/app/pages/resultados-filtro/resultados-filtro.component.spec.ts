import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResultadosFiltroComponent } from './resultados-filtro.component';

describe('ResultadosFiltroComponent', () => {
  let component: ResultadosFiltroComponent;
  let fixture: ComponentFixture<ResultadosFiltroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ResultadosFiltroComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ResultadosFiltroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
