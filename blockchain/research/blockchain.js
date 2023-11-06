// yarn add crypto-js
const hash = require('crypto-js/sha256')

class Block {
    constructor(prevHash, data) {
        this.prevHash = prevHash;
        this.data = data;
        this.timeStamp = new Date();
        this.hash = this.caculateHash()
    }

    caculateHash() {
        return hash(this.prevHash, JSON.stringify(this.data), this.timeStamp).toString();
    }
}

const block = new Block('', {
    hello: 'world',
})

console.log(block)