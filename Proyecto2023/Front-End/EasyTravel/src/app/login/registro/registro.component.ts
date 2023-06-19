import { Component, OnInit } from '@angular/core';
import { UsuarioService, Usuario } from 'src/app/services/auth/usuario.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth/auth.service';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})

export class RegistroComponent implements OnInit {

  form:FormGroup;
  usuario: Usuario = new Usuario();

  constructor(private authService:AuthService, private formBuilder: FormBuilder, 
    private usuarioService: UsuarioService, private router:Router) { 

      this.form= this.formBuilder.group(
        {
            nombre:['', [Validators.required]],
            apellido:['', [Validators.required]],
            dni:['', [Validators.required]],
            fechaNac:['', [Validators.required]],
            celular:['', [Validators.required]],
            mail:['', [Validators.required]],
            password:['', [Validators.required]]
        }
      )
  
  }

  ngOnInit(): void {
      
  }


 onEnviar (event:Event, usuario:Usuario): void {
    event.preventDefault;
    if (this.form.valid)
    {
      console.log("enviando al servidor");
      console.log(usuario);
      this.usuarioService.onCrearUsuario(usuario).subscribe(
        data => {
          console.log(data.id);
          if (data.id>0)
          {
            alert("El registro ha sido creado satisfactoriamente, A continuación inicie sesión");
            this.router.navigate(['/login'])
          }
        })
    }
    else 
    {this.form.markAllAsTouched();
    }
 };

 get Password1()
 {
  return this.form.get("password1");
 }

 get Password2() {
  return this.form.get("password2");
 }

 get Mail()
 {
  return this.form.get("mail");
 }

 get Nombre()
 {
  return this.form.get("nombre");
 }

 get Apellido()
 {
  return this.form.get("apellido");
 }

 get FechaNac()
 {
  return this.form.get("fechaNac");
 }

 get DNI()
 {
  return this.form.get("DNI");
 }

 get MailValid()
 {
  return this.Mail?.touched && !this.Mail?.valid;
 } 

 get NombreValid()
 {
  return this.Nombre?.touched && !this.Nombre?.valid;
 } 

 get ApellidoValid()
 {
  return this.Apellido?.touched && !this.Apellido?.valid;
 } 

 get Password1Valid()
 {
  return this.Password1?.touched && !this.Password1?.valid;
 } 

 get Password2Valid()
 {
  return this.Password2?.touched && !this.Password2?.valid;
 } 

 get FechaNacValid()
 {
  return this.FechaNac?.touched && !this.FechaNac?.valid;
 } 

 get DNIValid()
 {
  return this.DNI?.touched && !this.DNI?.valid;
 } 



}
