<?php
    $carros = array("Gol", "Uno", "Fiesta", "honda", "jeep");
    print_r($carros);
    echo "<hr>";

    $clientes = ["Edgar", "João", "Maria", "Pedro", "José"];
    print_r($clientes);
    echo "<hr>";

    $totalClientes = count($clientes);
    echo "O total de clientes é: $totalClientes";
    echo "<hr>";

    foreach ($carros as $indice => $valor) {
        echo "O carro $indice é um: $valor";
        echo "<br>";
    }

    $times = array(
        "Cariocas" => array("Campeao" => "Vasco", "vice" => "Flamengo", "terceiro" => "Botafogo"),
        "Paulistas" => array("Campeao" => "São Paulo", "terceiro" => "Palmeiras", "vice" => "Santos"),
        "Mineiros" => array("Campeao" => "Corinthians", "vice" => "Cruzeiro", "terceiro"=>"Fluminense")
    );
    echo "<hr>";
    //imprimir cada indice do array;
    foreach($times["Cariocas"] as $indice => $valor){
        echo "O $indice é: $valor";
        echo "<br>";
    }
    foreach($times["Paulistas"] as $indice => $valor){
        echo "O $indice é: $valor";
        echo "<br>";
    }
    foreach($times["Mineiros"] as $indice => $valor){
        echo "O $indice é: $valor";
        echo "<br>";
    }
?>