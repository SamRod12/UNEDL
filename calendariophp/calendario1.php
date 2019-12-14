<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/estilos.css">
    <title>Document</title>
</head>

<body>
<div id="wrapper">
        <div class="content">
        <table> 
        <thead class="dias">
            <tr>
                <th colspan="7"><h2>Diciembre</h2></th>
            </tr>
        <<tr>
                <th class="diaSem"><h3>Domingo</h3></th>
                <th class="diaSem"><h3>Lunes</h3></th>
                <th class="diaSem"><h3>Martes</h3></th>
                <th class="diaSem"><h3>Miercoles</h3></th>
                <th class="diaSem"><h3>Jueves</h3></th>
                <th class="diaSem"><h3>Viernes</h3></th>
                <th class="diaSem"><h3>Sabado</h3></th>
            </tr>
            </thead>
        <tr><th colspan="7"><h5 id="line">&nbsp;</h5></th></tr>

    
        <?php
        $aux=1;
        $aux2=1;
        $contador=0;
        $banderita=TRUE;
        for ($i=0;$i<5;$i++){ ?>
            <tr>
        <?php
       
            for($x=1;$x<$aux+7;$x++){
                if($banderita==TRUE){
                $contador++;
                $aux2=0;
                if($contador==14){
                    echo "<td id='entrega' title='dia de entrega'><h4>".$contador."</h4></td>";
                }
                else if ($contador==25){
                 echo "<td id='xMas' title='xMas'><h4>".$contador."</h4></td>";
                } else {
                 echo "<td><h4>".$contador. "<h4></td>";
                }
                   
                $aux2=$x%7;
                if($aux2 == 0){
                break;
                }
                if($contador ==31 ){
                $contador=0;
                    $banderita=FALSE;
                }}

                if($banderita==FALSE){
                    $contador++;
                    $aux2=-1;
                    echo "<td class='lighter'><h4>".$contador. "<h4></td>";
             
                    $aux2=($x+1)%7;
                    if($aux2 == 0){
                    break;
                    }
                }
            }
            
            ?>
            </tr>
            <?php
        }
        ?>
    </table>
    </div>
    </div>
    </div>
</body>
</html>

