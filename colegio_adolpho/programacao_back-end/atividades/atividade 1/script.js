// exercicio 01
let nome = "Pedro", idade = 16, cidade = "Astorga";
console.log(nome, idade, cidade);

// exercicio 02

let apresentacao = 'Meu nome é ' + nome + ' e eu moro em ' + cidade;
console.log(apresentacao);

// exercício 03

const anoNascimento = 2008;
let anoAtual = 2025;
console.log('Minha idade é ', anoAtual - anoNascimento);

// exercicio 04

let a = 5, b = 10;
let c = a;
a = b;
b = c;
console.log("Valor de a: " + a + "\nValor de b: " + b);

// exercicio 05

let numero1 = 8;
let numero2 = 3;

let adicao = numero1 + numero2;
let subtracao = numero1 - numero2;
let multiplicacao = numero1 * numero2;
let divisao = numero1 / numero2;

console.log("A subtração é ", subtracao, "\na adição é", adicao, "\na multiplicação é ", multiplicacao, "\ne a divisão é ", divisao);

// exercicio 06

let meuPesoEmKilos = 72;
let minhaAltura = 1.81;
let IMC = meuPesoEmKilos / (minhaAltura * minhaAltura);

console.log("Meu IMC é: ", IMC);