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

console.log(lsc("ABAZDC", "BACBAD"));