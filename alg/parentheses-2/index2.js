var generateParenthesis = function (n) {
  let merge = (l, arr, r) => arr.map((item) => `${l}${item}${r}`);
  let m = {};
  const f = (i) => {
    if (i === 0) return;
    if (i === 1) {
      m[i] = ["()"];
    } else {
      let r = [
        ...merge("()", m[`${i - 1}`], ""),
        ...merge("(", m[`${i - 1}`], ")"),
        ...merge("", m[`${i - 1}`], "()"),
        // ...(i % 2 === 0 ? [m[`${i / 2}`], ...m[`${i / 2}`]] : []),
      ];
      if (i % 2 === 0) {
        m[i / 2].forEach((halfArr) => r.push(`${halfArr}${halfArr}`));
      }
      m[i] = [];
      r.forEach((item) => {
        if (m[i].indexOf(item) < 0) m[i].push(item);
      });
    }
  };
  for (let i = 1; i <= n; i++) {
    f(i);
  }
  return m[`${n}`];
};

console.log(generateParenthesis(4));

[
  "()()()()()",
  "()()()(())",
  "()()(()())",
  "()()((()))",
  "()()(())()",
  "()(()()())",
  "()(()(()))",
  "()((()()))",
  "()(((())))",
  "()((())())",
  "()(()())()",
  "()((()))()",
  "()(())()()",
  "()(())(())",
  "(()()()())",
  "(()()(()))",
  "(()(()()))",
  "(()((())))",
  "(()(())())",
  "((()()()))",
  "((()(())))",
  "(((()())))",
  "((((()))))",
  "(((())()))",
  "((()())())",
  "(((()))())",
  "((())()())",
  "((())(()))",
  "(()()())()",
  "(()(()))()",
  "((()()))()",
  "(((())))()",
  "((())())()",
  "(()())()()",
  "((()))()()",
  "(())()()()",
  "(())(())()",
][
  ("((((()))))",
  "(((()())))",
  "(((())()))",
  "(((()))())",
  "(((())))()",
  "((()(())))",
  "((()()()))",
  "((()())())",
  "((()()))()",
  "((())(()))",
  "((())()())",
  "((())())()",
  "((()))(())",
  "((()))()()",
  "(()((())))",
  "(()(()()))",
  "(()(())())",
  "(()(()))()",
  "(()()(()))",
  "(()()()())",
  "(()()())()",
  "(()())(())",
  "(()())()()",
  "(())((()))",
  "(())(()())",
  "(())(())()",
  "(())()(())",
  "(())()()()",
  "()(((())))",
  "()((()()))",
  "()((())())",
  "()((()))()",
  "()(()(()))",
  "()(()()())",
  "()(()())()",
  "()(())(())",
  "()(())()()",
  "()()((()))",
  "()()(()())",
  "()()(())()",
  "()()()(())",
  "()()()()()")
];
