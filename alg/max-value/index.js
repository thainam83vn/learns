class Solution {
  constructor() {
    this.cache = {};
  }

  maxValue(arr, n, minus = false) {
    if (n === 0) return 0;
    if (this.cache[`${minus ? "-" : "+"}${n}`]) {
      return this.cache[`${minus ? "-" : "+"}${n}`];
    }
    const include =
      this.maxValue(arr, n - 1, !minus) + arr[n - 1] * (minus ? -1 : 1);
    const exclude = this.maxValue(arr, n - 1, minus);
    // console.log({ arr, include, exclude });
    this.cache[`${minus ? "-" : "+"}${n}`] = Math.max(include, exclude);
    return this.cache[`${minus ? "-" : "+"}${n}`];
  }
}

const sol = new Solution();
console.log(sol.maxValue([3, 9, 10, 1, 30, 40], 6));
// console.log(sol.maxValue([3, 9], 2));
console.log(sol.cache);
