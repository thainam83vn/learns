var _ = require('lodash');

function lsc(s, l) {
    let n = s.length, m = l.length;
    let dp = [];
    for(let i = 0; i <= n; i++) {
        dp.push(_.fill(Array(m + 1), 0));
    }
    for(let i = 1; i <= n; i++) {
        for(let j = 1; j <= m; j++) {
            if (s[i - 1] !== l[j - 1]) {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            } else {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            }
        }
    }
    return dp[n][m];
}

dp2 = {}
function lscSub(s, n, l, m) {
    if (n <= 0 || m <= 0)
        return 0;
    if (dp2[n * s.length + m]) {
        return dp2[n * s.length + m];
    }
    let r;
    if (s[n - 1] === l[m - 1]) {
        r = 1 + lscSub(s, n - 1, l, m - 1);
    } else {
        r = Math.max(lscSub(s, n - 1, l, m), lscSub(s, n, l, m - 1));
    }
    dp2[n*s.length + m] = r;
    return r;
}
//time O(nm)
//space O(nm)

let s = "ABAZDC", l = "BACBAD";

console.log(lsc(s, l));
console.log(lscSub(s, s.length, l, l.length));