/*
escribir un programa que ingrese una frase y que las letras a,e,i,o,g,s se cambien por sus respectivos numeros

a=4 e=3 i=1 o=0 g=9 s=5 

y viceversa
si el text field en el html esta vacio mandar un mensaje de error por consola
*/
function escribir(){
    
var entrada = document.getElementById("frase").value;

if (entrada == ""){
    console.error("necesitas ingresar un texto en el campo frase");
    alert("error impreso en consola");
   
    resultado(entrada);
}
else{
    entrada = Array.from(entrada);
    for(x in entrada){
        switch(entrada[x]){
            case "a": entrada[x]=4;
                break;
            case "e": entrada[x]=3;
                break;
            case "i": entrada[x]=1;
                break;
            case "o": entrada[x]=0;
                break;
            case "g": entrada[x]=9;
                break;
            case "s": entrada[x]=5;
                break;
            case "4": entrada[x]='a';
                break;
            case "3": entrada[x]='e';
                break;
            case "1": entrada[x]='i';
                break;
            case "0": entrada[x]='o';
                break;
            case "9": entrada[x]='g';
                break;
            case "5": entrada[x]='s';
                break;
        }
    }
   
    entrada = entrada.join("");
    
    resultado(entrada);
}

    function resultado(texto){
        res.innerHTML = texto
    }

      
      
};

