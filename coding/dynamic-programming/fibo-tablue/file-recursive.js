dp = {};
function fibo(n) {
    if (n <= 1) {
        return n;
    }
    if (!dp[`${n}`]) {
        dp[n] = fibo(n - 1) + fibo(n - 2);
    }
    return dp[`${n}`];
}


console.log(fibo(3), dp);