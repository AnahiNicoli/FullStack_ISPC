/*import { Component } from '@angular/core';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css']
})
export class PerfilComponent {

}
/*
// Declarar las variables para los elementos del menú y del contenido
const menuItems = document.querySelectorAll('.menu li a');
const contenidoItems = document.querySelectorAll('.contenido-container div');

// Agregar controlador de eventos clic a cada elemento de menú
menuItems.forEach(function(menuItem) {
  menuItem.addEventListener('click', function(e) {
    e.preventDefault();
    // Eliminar la clase "activo" de todos los elementos de menú
    menuItems.forEach(function(item) {
      item.classList.remove('activo');
    });

    // Agregar la clase "activo" al elemento de menú seleccionado
    this.classList.add('activo');

    // Mostrar el contenido correspondiente
    var target = this.getAttribute('href');
    for (var j = 0; j < contenidoItems.length; j++) {
      contenidoItems[j].style.display = 'none';
    }
    document.querySelector(target).style.display = 'block';
  });
});
*/

import { Component, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css']
})
export class PerfilComponent implements AfterViewInit {
  constructor() {}

  ngAfterViewInit() {
    const menuItems: NodeListOf<HTMLAnchorElement> = document.querySelectorAll('.menu li a');
    const contenidoItems: NodeListOf<HTMLDivElement> = document.querySelectorAll('.contenido-container div');

    menuItems.forEach((menuItem: HTMLAnchorElement) => {
      menuItem.addEventListener('click', (e) => {
        e.preventDefault();
        menuItems.forEach((item: HTMLAnchorElement) => {
          item.classList.remove('activo');
        });

        menuItem.classList.add('activo');

        const target = menuItem.getAttribute('href');
        let j: number;
        for (j = 0; j < contenidoItems.length; j++) {
          contenidoItems[j].style.display = 'none';
        }
        const targetElement = target !== null ? (document.querySelector(target) as HTMLElement) : null;
        if (targetElement) {
          targetElement.style.display = 'block';
        }
      });
    });
  }
}




