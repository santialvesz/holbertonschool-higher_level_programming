#!/usr/bin/node
const argv = process.argv.slice();
argv.shift();
argv.shift();
argv.sort(function (a, b) { return a - b; });
if (argv.length === 0 || argv.length === 1) {
  console.log(0);
} else if (argv[argv.length - 2]) {
  console.log(argv[argv.length - 2]);
}
