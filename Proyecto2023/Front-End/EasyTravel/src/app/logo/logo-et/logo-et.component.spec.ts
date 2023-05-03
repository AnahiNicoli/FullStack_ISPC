import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LogoETComponent } from './logo-et.component';

describe('LogoETComponent', () => {
  let component: LogoETComponent;
  let fixture: ComponentFixture<LogoETComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LogoETComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LogoETComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
