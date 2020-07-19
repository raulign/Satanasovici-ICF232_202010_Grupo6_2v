#Digitalizacion De una Peluqueria

Proyecto Universitario llevado a cabo en django

*Usuario de prueba(Super User):
    *Nombre de Usuario : 'admin'
    *Contraseña: 'luciano123'

##Uso del Programa 

1. Obtener el codigo fuente
```

```

2. Es necesario tener python instalado(idealmente 3.7 en adelante)
 
3. Acceder al entorno virtual y ejecutarlo
```
test/Scripts/activate
```

4. Instalar los requerimientos
```
pip3 install -r requirements.txt
```

5. Acceder a la Carpeta Digitalizacion
```
GrupoN°6_Peluqueria/Digitalizacion
```

6. Instalar los Crispy-form
```
pip3 install django-crispy-forms
```

7. Migrar el servidor
```
python manage.py migrate
```

8. Ejecutar el servidor
```
python manage.py runserver
```

##Casos de Prueba
*Usuario de prueba 1:
    *Nombre de Usuario : 'Brianatana'
    *Contraseña: 'atana123'

*Usuario de prueba 2:
    *Nombre de Usuario : 'javo'
    *Contraseña: 'javito123'

*Usuario de prueba 3:
    *Nombre de Usuario : 'Mortons'
    *Contraseña: 'lopez123'

Este programa permite la creacion de tu propio usuario, de igual manera puedes utilizar cualquiera de los casos de prueba propuestos. Una vez iniciada la sesión tendremos un menu con las diferentes opciones a realizar dentro de nuestra pagina. Para realizar cambios a los datos del usuario(nombre, contraseña, suername, etc..) es necesario dirigirse a la pestaña de configuracion de cuenta, alli podran encontran las siguientes opciones:

-Editar perfil
-Cambiar Contraseña
-Eliminar Cuenta

Cada una de esta opciones cumple con una tarea diferente

Editar perfil: Podras editar los datos principales registrados al inicio, ya sean, Nombre, Apellidos, Correo, Username.

Cambiar contraseña: Al ingresar tendras la opcion de cambiar tu contraseña por una nueva

Eliminar Cuenta: Esta opcion permitira eliminar tu cuenta, de ser asi seras redirigido a la pagina principal.


