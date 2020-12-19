const { hashIndex } = require("../lib/commons");
const _ = require("lodash");

var longestPalindrome = function (s) {
  if (s.length <= 1) return s;
  let n = s.length;
  let dp = [];
  dp.push(_.fill(Array(n + 1), 0));
  for (let i = 1; i < n + 1; i++) {
    dp.push(_.fill(Array(n + 1), 0));
  }
  let max = [1, 1];

  let dic = {};
  let q = [];
  let addToQueue = (i, j) => {
    if (!dic[hashIndex(i, j)]) {
      dic[hashIndex(i, j)] = 1;
      q.push({ i, j });
    }
  };
  addToQueue(1, 1);
  let spread = (i, j) => {
    addToQueue(i, j + 1);
    addToQueue(i + 1, j + 1);
    addToQueue(i + 1, j);
  };
  let updateMax = (i, j) => {
    if (dp[i][j] && j - i > max[1] - max[0]) {
      max = [i, j];
    }
  };
  while (q.length > 0) {
    let { i, j } = q[0];
    q.splice(0, 1);
    if (i <= n && j <= n) {
      if (i === j) {
        dp[i][j] = 1;
      } else if (i > j) {
        dp[i][j] = 0;
      } else if (s[i - 1] === s[j - 1]) {
        dp[i][j] = dp[i + 1][j - 1] || dp[i][j - 1];
        updateMax(i, j);
      } else {
        dp[i][j] = 0;
      }
      spread(i, j);
    }
  }

  console.log(
    "========================================================================"
  );
  console.log(max, s.substring(max[0] - 1, max[1]));
  console.log(dp.join("\n"));
  return s.substring(max[0] - 1, max[1]);
};

let tests = [
  // "ccd",
  // "ccc",
  // "cbbd",
  // "bb",
  // "babad",
  // "abcda",
  // "babadada",
  // "babaddtattarrattatddetartrateedredividerb",
  // "bb",
  "aaabaaaa",
];
tests.forEach((test) => console.log(`${test} => ${longestPalindrome(test)}`));
