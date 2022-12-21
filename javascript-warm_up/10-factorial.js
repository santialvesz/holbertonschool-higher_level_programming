#!/usr/bin/node
const argv = require('process').argv;

function fact (num) {
  if (num === 0 || num === 1) {
    return num;
  }
  return num * fact(num - 1);
}
if (isNaN(argv[2])) {
  console.log('1');
} else {
  console.log(fact(+argv[2]));
}
