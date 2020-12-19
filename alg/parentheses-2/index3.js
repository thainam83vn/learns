var generateParenthesis = function (n) {
  let result = [];
  const backtrack = (s = "", left = 0, right = 0) => {
    if (s.length === 2 * n) {
      result.push(s);
      return;
    }

    if (left < n) {
      backtrack(s + "(", left + 1, right);
    }
    if (right < left) {
      backtrack(s + ")", left, right + 1);
    }
  };
  backtrack();
  return result;
};

console.log(generateParenthesis(4));
