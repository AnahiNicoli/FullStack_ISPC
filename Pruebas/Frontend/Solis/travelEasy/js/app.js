const imagen1 = document.getElementsByClassName('imagen1');

const cargarImagen = (entradas, observador) => {
    entradas.forEach((entrada) => {
        if(entrada.isIntersecting){
            entrada.target.classList.add('visible');
            console.log('ola')
        }
    });
}


const observador = new IntersectionObserver(cargarImagen, {
    root: null,
    threshold: 1.0
});

observador.observe(imagen1);