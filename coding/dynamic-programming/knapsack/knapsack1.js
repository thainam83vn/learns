var dp = {};
var count = 0;
function hashIndex(n, cap) {
  return `${n}_${cap}`;
}

function knapsack(values, sizes, n, cap) {
  if (n === 0) return 0;
  let index = hashIndex(n, cap);
  if (dp[index]) {
    return dp[index];
  }
  count++;
  if (sizes[n - 1] > cap) {
    dp[index] = knapsack(values, sizes, n - 1, cap);
  } else {
    dp[index] = Math.max(
      values[n - 1] + knapsack(values, sizes, n - 1, cap - sizes[n - 1]),
      knapsack(values, sizes, n - 1, cap)
    );
  }
  return dp[index];
}

let values = [7, 9, 5, 12, 14, 6, 12];
let sizes = [3, 4, 2, 6, 7, 3, 5];
console.log(knapsack(values, sizes, values.length, 15));
console.log({ dp, count, size: values.length });
