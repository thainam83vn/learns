const { has } = require("lodash");

var longestPalindrome = function (s) {
  if (s.length <= 1) return s;
  let dp = {};
  function hashIndex(n, cap) {
    return `${n}_${cap}`;
  }
  let count = 0;
  let lp = (s, i, j) => {
    if (i > j) return true;
    if (i === j) return true;
    // if (i === j - 1) return s[i] + s[j];
    let index = hashIndex(i, j);
    if (dp[index]) return dp[index];
    count++;
    if (s[i] === s[j]) {
      let mr = dp[hashIndex(i + 1, j - 1)] || lp(s, i + 1, j - 1);
      // if (!mr) {
      //   dp[hashIndex(i + 1, j)] || lp(s, i + 1, j);
      //   dp[hashIndex(i, j - 1)] || lp(s, i, j - 1);
      // }
      dp[index] = mr;
    } else {
      lp(s, i + 1, j);
      lp(s, i, j - 1);
      dp[index] = false;
    }
    return dp[index];
  };
  lp(s, 0, s.length - 1);
  console.log(
    "===================================================================="
  );
  console.log(dp);
  let r = Object.keys(dp)
    .filter((key) => dp[key] === true)
    .reduce((max, value) => {
      let indices = value.split("_");
      let start = parseInt(indices[0]),
        end = parseInt(indices[1]);
      if (end - start + 1 > max.length) {
        return s.substring(start, end + 1);
      }
      return max;
    }, "");
  return r.length > 0 ? r : s[0];
};

let tests = [
  // "ccd",
  // "ccc",
  // "cbbd",
  // "bb",
  // "babad",
  // "abcda",
  // "babadada",
  "babaddtattarrattatddetartrateedredividerb",
  // "bb",
  // "aaabaaaa",
];
tests.forEach((test) => console.log(`${test} => ${longestPalindrome(test)}`));
