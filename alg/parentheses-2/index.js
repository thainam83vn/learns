var generateParenthesis = function (n) {
  const merge = (l, arr, r = "") => arr.map((item) => l + item + r);
  const f = (i, j) => {
    if (i === 0 && j === 0) {
      return [""];
    }
    if (j === 0) {
      return merge("(", f(i - 1, j + 1));
    } else {
      if (i === 0) {
        return merge(")", f(i, j - 1));
      } else {
        return [...merge("(", f(i - 1, j)), ...merge(")", f(i, j - 1))];
      }
    }
  };

  return f(n, 0);
};

console.log(generateParenthesis(2));
