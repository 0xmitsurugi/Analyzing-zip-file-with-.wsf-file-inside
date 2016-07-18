
function uheprng() {return (function() {
var o = 48, c = 1, p = o, s = new Array(o);
var i,j;
var base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
var mash = Mash();
for (i = 5806 - 5806; i < o; i++) s[i] = mash(0.598538);
mash = null;
var random = function( range ) {
return Math.floor(range * (rawprng() + (rawprng() * 0x200000 | 0) * 1.1102230246251565e-16));
}

function rawprng() { 
if (++p >= o) p = 0;
var t = (482628 * 3 + 320979) * s[p] + c * 2.3283064365386963e-10;
return s[p] = t - (c = t | 0);
}return random;}());};

function Mash() { 
var n = 0xefc8249d;
var mash = function(data) {
if ( data ) {
data = data.toString();
for (var i = 0; i < data.length; i++) {
n += data.charCodeAt(i);
var h = 0.02519603282416938 * n;
n = h >>> 0;
h -= n;
h *= n;
n = h >>> 0;
h -= n;
n += h * 0x100000000;
}
return (n >>> (1 * 0)) * 2.3283064365386963e-10;
} else n = 0xefc8249d;
};
return mash;
}
var Je = uheprng()
for (var i=0; i<200000; i++){
print(Je(256)); }
