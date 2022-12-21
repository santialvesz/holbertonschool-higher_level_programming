#!/usr/bin/node
const argv = require('process').argv;

if (isNaN(argv[2] && argv[3])) {
  console.log('NaN');
} else {
  console.log(+argv[2] + +argv[3]);
}
/*
Alternative
console.log(+argv[2] + +argv[3])
*/
