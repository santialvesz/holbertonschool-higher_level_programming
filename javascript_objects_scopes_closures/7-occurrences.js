#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach(i => {
    if (i === searchElement) counter++;
  });
  return counter;
};
