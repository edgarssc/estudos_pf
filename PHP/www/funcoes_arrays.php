<?php
//princpais funções php de array
/*
is_array($array) = verifica se é um array
is_array($valor, $array) = verifica se o valor está dentro do array
array_push($array, $valor) = adiciona um valor ao final do array
array_keys($array) = retorna um array com as chaves do array
array_values($array) = retorna um array com os valores do array
array_merge($array1, $array2) = junta dois arrays
array_pop($array) = remove o último elemento do array
array_shift($array) = remove o primeiro elemento do array
array_unshift($array, $valor) = adiciona um valor no inicio do array
array_combine($chaves, $valores) = mescla dois arrays, denominando um como chave e outro como valor
array_reverse($array) = inverte o array
array_search($valor, $array) = retorna o indice do valor no array
array_sum($array) = soma todos os valores do array
explode("/","20/01/2001") = divide uma string em um array
implode("-",$arr) = transforma um array em uma string
*/
$nomes = array("chefe"=>"Edgar", "empregado"=>"João", "Analista"=>"Maria", "Porteiro"=>"Pedro", "Operário"=>"José");
$teste = "novo teste";
echo is_array($teste);
echo "<br>";
if (is_array($teste)){
    echo "é um array";
    echo "<br>";
}
else{
    echo "não é um array";
    echo "<br>";
}
var_dump(is_array($nomes));
echo "<hr>";

$novo = array_keys($nomes);
var_dump($novo);
echo "<hr>";

?>