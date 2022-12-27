# Maquina elemental Abacus
Este pequeno programa es un interprete de la Maquina Elemental Abacus usada en la materia "Organizacion del Computador" de la Catedra de Benitez. Especificada aqui: https://drive.google.com/file/d/1rz3_wATokWx7XaGZR4H13a8Iq0fjcuaz/view

Pull Request mas que  bienvenidos! (Particularmente sobre los TODO's)

![Demostracion](demo.gif)

## Que hace?
1. Te permite escribir y ejecutar un codigo Abacus (Con comentario)
2. Ver el contenido del acumulador
3. Ver linea a linea lo que la maquina interpreta

**Advertencia sobre archivos excel**: El programa soporta el uso de archivos xlsx con codigo abacus. Sin embargo, se necesita la libreria "openpyxl", la cual se puede descargar con pip o con el instalador de paquetes nativos. **Si no se usan archivos excel, no es necesario descargar dicha libreria**, el interprete puede funcionar correctamente sin la libreria mientras que se le pasen archivos .abs. Siempre existe la posibilidad de copiar y pegar el excel en un archivo .abs y configurarlo a mano. 

Si se usa un archivo xlsx, el programa va a devolver un archivo .abs con el codigo abacus extraido del xlsx (este nuevo archivo puede ser editado y ejecutado en corridas posteriores).

## TODO (en orden de prioridad):
- [ ] Hacer que el programa soporte argumentos de terminal
- [X] Importar un excel con codigo Abacus y ejecutarlo
	- [ ] Incluir soporte para notacion RodoFabri
- [ ] Tener funciones que permitan crear estructuras ya pre-hechas (como un creador de lista que te permita crear una lista de x elementos con valores de ejemplo)
- [X] Que escriba el resultado en otro archivo
- [ ] Tener errores propios y mas lindos (en vez de Keyerror)
- [ ] Crear un lsp (Ultimo)
