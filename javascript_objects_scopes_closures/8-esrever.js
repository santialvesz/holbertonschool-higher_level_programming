#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0, j = list.length - 1; i < j; i++, j--) {
    const tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
  }
  return list;
};
