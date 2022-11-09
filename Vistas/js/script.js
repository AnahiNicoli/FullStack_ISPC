
/* función de pop-up +info de carrousel de ofertas */
const btnAbrirModal =
document.querySelector("#btn-abrir-modal");
const btnCerrarModa =
document.querySelector("#btn-cerrar-modal");
const modal =
document.querySelector("#modal");

btnAbrirModal.addEventListener("click",()=>{
    modal.showModal();
})

btnCerrarModa.addEventListener("click",()=>{
    modal.close();
})


const btnAbrirModal2 =
document.querySelector("#btn-abrir-modal2");
const btnCerrarModal2 =
document.querySelector("#btn-cerrar-modal2");
const modal2 =
document.querySelector("#modal2");

btnAbrirModal2.addEventListener("click",()=>{
    modal2.showModal();
})

btnCerrarModal2.addEventListener("click",()=>{
    modal2.close();
})

const btnAbrirModal3 =
document.querySelector("#btn-abrir-modal3");
const btnCerrarModal3 =
document.querySelector("#btn-cerrar-modal3");
const modal3 =
document.querySelector("#modal3");

btnAbrirModal3.addEventListener("click",()=>{
    modal3.showModal();
})

btnCerrarModal3.addEventListener("click",()=>{
    modal3.close();
})