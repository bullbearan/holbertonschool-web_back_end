const cleanSet = (set, startString) => {
  let res = '';
  if (!startString) return '';
  set.forEach((e) => {
    if (e && e.startsWith(startString)) res += `${e.slice(startString.length)}-`;
  });
  return res.slice(0, res.length - 1);
};
export default cleanSet;
