const bitcore = require('bitcore-lib');
const rand_buffer = bitcore.crypto.Random.getRandomBuffer(32);
const rand_number = bitcore.crypto.BN.fromBuffer(rand_buffer);
const address = new bitcore.PrivateKey(rand_number).toAddress('testnet');
console.log(rand_number.toString());
console.log(address.toString());

console.log(bitcore.PrivateKey('testnet').toWIF());