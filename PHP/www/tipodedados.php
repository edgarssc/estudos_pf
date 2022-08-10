<?php
    echo "<h1>Funcionando o PHP</h1>";
    echo "<hr>";
    
    //string
    $nome = "Edgar Souza Siqueira";
    echo "<hr>";
    var_dump($nome);
    if (is_string($nome)) {
        echo "<br>É uma string";
        echo "<hr>";
    }
    else{
        echo "<br>Não é uma string";
        echo "<hr>";
    }

    //int
    $numero = 12345;
    echo "<hr>";
    var_dump($numero);
    if (is_int($numero)) {
        echo "<br>É um número";
        echo "<hr>";
    }
    else{
        echo "<br>Não é um número";
        echo "<hr>";
    }

    //float
    $altura = 1.80;
    echo "<hr>";
    var_dump($altura);
    if (is_float($altura)) {
        echo "<br>É um float";
        echo "<hr>";
    }
    else{
        echo "<br>Não é um float";
        echo "<hr>";
    }

    //boolean
    $fato = true;
    echo "<hr>";
    var_dump($fato);
    if (is_bool($fato)) {
        echo "<br>verdadeiro";
        echo "<hr>";
    }
    else{
        echo "<br>falso";
        echo "<hr>";
    }

    //array
    $carros = array("Gol", "Uno", "Fiesta",12,20.5,true);
    var_dump($carros);
    echo "<hr>";

?>