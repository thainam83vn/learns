const { hashIndex } = require("../lib/commons");
const _ = require("lodash");

var longestPalindrome = function (s) {
  if (s.length <= 1) return s;
  let n = s.length;
  let dp = {};
  let dic = {};
  let q = [];
  let addToQueue = (i, j) => {
    let index = hashIndex(i, j);
    if (dp[index] === undefined) {
      q.push({ i, j });
    }
  };
  let removeFromQueue = () => {
    do {
      let { i, j } = q[0];
      q.splice(0, 1);
      return { i, j };
    } while (q.length > 0);
  };
  addToQueue(0, n - 1);
  let max = [1, 1];
  let q2 = [];
  while (q.length > 0) {
    let { i, j } = removeFromQueue();
    let index = hashIndex(i, j);
    if (dp[index] === undefined) {
      if (i < 0 || i > n - 1 || j < 0 || j > n - 1) {
        dp[index] = 0;
      } else if (i === j) {
        dp[index] = 1;
      } else if (j - i === 1) {
        if (s[i] === s[j]) {
          dp[index] = 1;
          if (j - i > max[1] - max[0]) {
            max = [i, j];
          }
        } else {
          dp[index] = 0;
        }
      } else if (i > j) {
        dp[index] = 0;
      } else if (s[i] === s[j]) {
        if (dp[hashIndex(i + 1, j - 1)] === undefined) {
          addToQueue(i + 1, j - 1);
        }
        if (dp[hashIndex(i + 1, j - 1)] === undefined) {
          q2.push({ i, j });
        } else {
          dp[index] = dp[hashIndex(i + 1, j - 1)];
          if (dp[index]) {
            if (j - i > max[1] - max[0]) {
              max = [i, j];
            }
          } else {
            addToQueue(i, j - 1);
            addToQueue(i + 1, j);
          }
        }
      } else {
        dp[index] = 0;
        addToQueue(i, j - 1);
        addToQueue(i + 1, j);
      }
    }
    if (q.length === 0 && q2.length > 0) {
      for (let k = q2.length - 1; k >= 0; k--) q.push(q2[k]);
      q2 = [];
    }
    // console.log(q.length);
  }

  // console.log(
  //   "========================================================================"
  // );
  // console.log(dp, max);
  return s.substring(max[0], max[1] + 1);
};

let tests = [
  // "ccd",
  // "ccc",
  // "cbbd",
  // "bb",
  // "babad",
  // "abcda",
  // "babada",
  // "babadada",
  // "babaddtattarrattatddetartrateedredividerb",
  // "bb",
  // "aaabaaaa",
  "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth",
];
tests.forEach((test) => console.log(`${test} => ${longestPalindrome(test)}`));
