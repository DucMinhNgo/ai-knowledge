const bitcore = require('bitcore-lib');

const privateKeyWIF = 'cVqMRB1KAL9MrficYcfF8Xk8hRx7HbwAY88mp58B9xXw5KrEJQYG';

const privateKey = bitcore.PrivateKey.fromWIF(privateKeyWIF);
const address = privateKey.toAddress();
console.log(address.toString()); // tb1qw2c3lxufxqe2x9s4rdzh65tpf4d7fssjgh8nv6